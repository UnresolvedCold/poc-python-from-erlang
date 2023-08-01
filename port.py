from erl_comm import read_cmd, write_cmd

num = 0

def foo(x):
    global num
    num = 5
    return x * 2

def bar(y):
    return y * 3 + num

while True:
    cmd = read_cmd()
    if cmd is None:
        break

    fn = cmd[0]
    arg = cmd[1]

    if fn == 1:
        res = foo(arg)
    elif fn == 2:
        res = bar(arg)
    else:
        res = 0

    write_cmd(bytes([res]))
