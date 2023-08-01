import sys

def read_exact(length):
    buf = b''
    while len(buf) < length:
        data = sys.stdin.buffer.read(length - len(buf))
        if not data:
            return None
        buf += data
    return buf

def write_exact(data):
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()

def read_cmd():
    len_bytes = read_exact(2)
    if len_bytes is None:
        return None
    length = int.from_bytes(len_bytes, byteorder='big')
    data_bytes = read_exact(length)
    return data_bytes

def write_cmd(data_bytes):
    length = len(data_bytes)
    len_bytes = length.to_bytes(2, byteorder='big')
    write_exact(len_bytes)
    write_exact(data_bytes)
