-module(py_erlang_01).
-export([add/0]).

add() ->
    Command = "python3 -c \"import add; print(add.add(5, 6))\"",
    Result = os:cmd(Command),
    ProcessedResult = string:strip(Result, right, $\n),
    list_to_integer(ProcessedResult).
