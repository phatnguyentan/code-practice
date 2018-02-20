# iex -S mix
# Tax.start
# import Product
defmodule Tax do
  defmodule Product do
    # defstruct name: "", price: 0, type: "", rate: 0
    defstruct [:name, :price, :type, :rate]
  end
  defmodule Receipt do
    # defstruct name: "", price: 0, type: "", rate: 0
    defstruct [:quality, :product]
  end
  def hello do
    :world
  end

  def sample() do
    data = File.stream!(Path.absname("./resources/sample1.csv")) |> CSV.decode! |> Enum.take(10)
    # IO.inspect(%Product{name: " book"})
    product = %Product{name: " book"}
    receipt = %Receipt{quality: 1, product: product}
  end
end
