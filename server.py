import socket
from pydantic import BaseModel
from time import sleep
import json



SERVER_ADDRESS = ('localhost', 8686)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')


class TCPPacket(BaseModel):
    id: int
    message: str

class TCPPackets(BaseModel):
    packets: TCPPacket



if __name__ == '__main__':
    while True:

        connection, address = server_socket.accept()
        print("new connection from {address}".format(address=address))


        while True:
            try: 
                # data = TCPPacket(json.loads(str(connection.recv(1024).decode())))e
                foo = str(connection.recv(1024).decode()).split('\n')
                if not foo:
                    continue
                print('\n\n\n\n\n\n')

                print(foo)

                print('\n\n\n\n\n\n')


                for i in range(0, len(foo)-1):
                    print(json.loads(foo[i]))
                    print(i)
                    data = TCPPacket.model_validate(json.loads(foo[i]))
                    print(data)

                connection.send(bytes('Hello from server!', encoding='UTF-8'))
                print(data.id)
                if data.id == 9:
                    raise socket.error
            except socket.error:
                print('client disconnected')
                # connection.shutdown(socket.SHUT_RDWR)
                connection.close()
                break
            # except Exception as e:
            #     print('client disconnected')
            #     print('\n\n\n\n\n\n')
            #     print(e)
            #     # connection.shutdown(socket.SHUT_RDWR)
            #     connection.close()
            #     break

    