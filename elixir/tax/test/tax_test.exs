defmodule TaxTest do
  use ExUnit.Case
  doctest Tax

  test "test input 1" do
    receipt = Tax.get_tax_from_csv("resources/input1.csv")
    assert receipt["result"]["tax"] == 1.50
    assert receipt["result"]["total"] == 29.83
  end

  test "test input 2" do
    receipt = Tax.get_tax_from_csv("resources/input2.csv")
    assert receipt["result"]["tax"] == 7.65
    assert receipt["result"]["total"] == 65.15
  end

  test "test input 3" do
    receipt = Tax.get_tax_from_csv("resources/input3.csv")
    assert receipt["result"]["tax"] == 6.70
    assert receipt["result"]["total"] == 74.68
  end

  test "test print output" do
    Tax.print_output("resources/input3.csv")
  end
end
