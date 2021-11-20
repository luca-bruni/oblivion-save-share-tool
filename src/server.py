from socket import *
import ssl

class Server:
    def __init__(self, peer_address, peer_port, password):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True
        context.load_default_certs()

        sock = socket.socket(AF_INET, SOCK_STREAM)
        sock.bind((peer_address, peer_port))
        sock.listen()
    
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            self.connection = conn

    def listen_for_file(self):
        pass
    
    def send_file(self):
        pass
        