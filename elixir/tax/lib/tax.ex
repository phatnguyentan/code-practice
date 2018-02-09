defmodule Tax do
  @moduledoc """
  Documentation for Tax.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Tax.hello
      :world

  """
  def hello do
    :world
  end

  def start(_a, _b) do
    IO.puts("aaaaaaaaaaaa")
    NimbleCSV.define(MyParser, separator: "\t", escape: "\"")

    # Parse the data
    IO.inspect MyParser.parse_string "name\tage\njohn\t27"
    #=> [["john","27"]]
    # List all child processes to be supervised
    children = [
      # Starts a worker by calling: A.Worker.start_link(arg)
      # {A.Worker, arg},
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: A.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
