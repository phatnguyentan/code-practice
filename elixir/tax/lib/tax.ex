# iex -S mix
# Tax.start
defmodule Tax do
  # Module calculate tax from product and quantity
  defmodule TaxCalculator do
    @precision 0.05

    def calculate(products) do
      products_with_tax = products
      |> Enum.map(fn product ->
        calculate_product(product)
      end)
      tax = Enum.reduce(products_with_tax, %{"tax" => 0, "total" => 0}, fn(item, acc) ->
        acc = Map.merge(acc, %{"tax" => display_round(acc["tax"] + item["tax"]), "total" => display_round(acc["total"] + item["total_price_after_tax"]) })
        acc
      end)
      %{"products" => products_with_tax, "result" => tax}
    end

    defp calculate_product(product) do
      product = Map.put(product, "price", String.to_float(product["price"]))
      product = Map.put(product, "quantity", String.to_integer(product["quantity"]))
      product = Map.put(product, "total_price", product["price"] * product["quantity"])
      product = Map.put(product, "tax", tax_round(product["total_price"] * product["rate"], @precision))
      product = Map.put(product, "total_price_after_tax", display_round(product["total_price"] + product["tax"]))
      product
    end

    defp tax_round(num, precision) do
      num = Float.ceil(num, 2)
      # Round until precision
      num = if rem(round(num*100), round(precision*100)) > 0 do
        ((precision*100 - rem(round(num*100), round(precision*100))) + num*100)/100
      else
        num
      end
      num
    end

    def display_round(num) do
      Float.round(num, 2)
    end
  end

  # Module detect and add rate, some info into product
  defmodule ProductGenerator do
    # Kind of products and rate
    # product required
    # rate required
    # type optionnal
    @kinds_of_product [
      %{"product" => "book", "type" => "book", "rate" => 0},
      %{"product" => "music cd", "type" => "other", "rate" => 0.1},
      %{"product" => "chocolate", "type" => "food", "rate" => 0},
      %{"product" => "perfume", "type" => "other", "rate" => 0.1},
      %{"product" => "headache pills", "type" => "medical", "rate" => 0},
    ]
    @imported_rate 0.05

    def generate_product(map) do
      map = Enum.reduce(@kinds_of_product, map, fn(item, acc) ->
        # Add basic rate into product
        acc = if String.match?(map["product"], ~r/#{item["product"]}/) do
          Map.merge(acc, %{"rate" => item["rate"]})
        else
          acc
        end
        acc
      end)
      if Map.has_key?(map, "rate") do
        map
      else
        raise ArgumentError, message: "Please add product into @kinds_of_product (note: without prefix imported), ex: %{\"product\" => \"book\", \"type\" => \"book\", \"rate\" => 0, \"imported\" => false},"
      end
      # add additional rate into imported product
      map = if String.match?(map["product"], ~r/imported/) do
        Map.merge(map, %{"imported" => true, "rate" => TaxCalculator.display_round(map["rate"] + @imported_rate)})
      else
        Map.merge(map, %{"imported" => false})
      end
      map
    end
  end

  # Module generate receipt from csv data
  defmodule ReceiptGenerator do
    def generate_receipt_from_csv(data) do
      # get header and content from data
      [header | content] = data
      # generate maps from data
      maps = content
      |> Enum.reduce([], fn(v, acc) ->
          List.insert_at(acc, -1,
          header
            |> Enum.with_index
            |> Enum.reduce(%{}, fn({h, i}, acc) ->
                acc = Map.merge(acc, %{String.downcase(h) => Enum.at(v, i)})
                acc
               end))
         end)
      # generate products from data
      products = maps
      |> Enum.map(fn(map) ->
        ProductGenerator.generate_product(map)
      end)
      # calculate taxes from list products
      TaxCalculator.calculate(products)
    end
  end

  # Main function to get tax from CSV
  def get_tax_from_csv(path) do
    File.stream!(Path.absname(path)) |> CSV.decode! |> Enum.take_every(1) |> ReceiptGenerator.generate_receipt_from_csv
  end

  # Test function to print output
  def print_output(path \\ "resources/input1.csv") do
    receipt = get_tax_from_csv(path)
    IO.inspect("# OUTPUT (to stdout)")
    IO.inspect("Quantity, Product, Price")
    format = &(:erlang.float_to_binary(&1, [decimals: 2]))
    receipt["products"]
    |> Enum.each(fn r ->
      IO.inspect("#{r["quantity"]}, #{r["product"]}, #{format.(r["total_price_after_tax"])}")
    end)
    IO.inspect("Sales Taxes: #{format.(receipt["result"]["tax"])}")
    IO.inspect("Total: #{format.(receipt["result"]["total"])}")
  end
end
