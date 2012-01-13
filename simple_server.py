from gevent import server


class MyServer(server.StreamServer):
    def __init__(self, listener_addr):
        server.StreamServer.__init__(self, listener_addr, self.my_handler)
        self.active_sockets = []
        self.conn_number = 0

    def my_handler(self, client_socket, client_addr):
        data = client_socket.recv(1024)
        self.conn_number += 1
        client_socket.sendall(str(self.conn_number))

server = MyServer(('127.0.0.1', 56789))

server.serve_forever()

