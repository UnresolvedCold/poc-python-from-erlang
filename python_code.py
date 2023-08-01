import sys

def foo(x):
    return x * 2

def bar(y):
    return y * 3

def read_cmd():
    len_bytes = sys.stdin.buffer.read(2)
    if not len_bytes:
        return None
    length = int.from_bytes(len_bytes, byteorder='big')
    data_bytes = sys.stdin.buffer.read(length)
    return data_bytes

def write_cmd(data_bytes):
    length = len(data_bytes)
    len_bytes = length.to_bytes(2, byteorder='big')
    sys.stdout.buffer.write(len_bytes)
    sys.stdout.buffer.write(data_bytes)
    sys.stdout.buffer.flush()

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
