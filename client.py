import socket
from pydantic import BaseModel
from time import sleep
import sys

class TCPPacket(BaseModel):
    id: int
    message: str

sock = socket.socket()
sock.connect(('localhost', 8686))

for i in range(0,10):
    package = TCPPacket(id=i, message=f'message number {i}').model_dump_json().encode() + b'\n'
    # if sys.getsizeof(package) < 1024:
    #     package = package + b'0'*(1024-sys.getsizeof(package))
    sock.send(package)
    # sleep(3)

data = sock.recv(1024)
sock.close()

print(data)
