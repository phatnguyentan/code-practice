defmodule Tax do

  def hello do
    :world
  end

  def start(_a, _b) do
    IO.puts("aaaaaaaaaaaa")
    NimbleCSV.define(MyParser, separator: "\t", escape: "\"")
    # Parse the data
    IO.inspect MyParser.parse_string "name\tage\njohn\t27"
  end
end
