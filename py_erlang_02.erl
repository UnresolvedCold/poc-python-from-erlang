-module(py_erlang_02).
-export([add/0]).

add() ->
    add(5, 7).

add(A, B) ->
    Command = "python3 -c 'from add import add; import sys; result = add(" ++ integer_to_list(A) ++ ", " ++ integer_to_list(B) ++ "); sys.stdout.write(str(result))'",
    Port = open_port({spawn, Command}, []),
    Result = get_result(Port),
    port_close(Port),
    list_to_integer(Result).

get_result(Port) ->
    receive
        {Port, {data, Data}} -> Data
    after
        5000 -> error
    end.
