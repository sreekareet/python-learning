import socket
from exceptions import FastKVSConnectionError, FastKVSTimeoutError, FastKVSProtocolError, FastKVSKeyError

class FastKVSClient:
    def __init__(self, host="127.0.0.1", port=7379, timeout=30):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.host, self.port))
        except ConnectionRefusedError:
            raise FastKVSConnectionError(f"could not connect to {self.host}:{self.port} - is the server running?")
        except socket.timeout:
            raise FastKVSTimeoutError(f"connection timed out after {self.timeout}s")

    def close(self):
        if self.socket:
            self.socket.close()
            self.socket = None

    def send_command(self, command):
        try:
            self.socket.sendall((command + "\n").encode("utf-8"))
            response = self.socket.recv(4096).decode("utf-8").strip()
            return response
        except socket.timeout:
            raise FastKVSTimeoutError("server did not respond in time")
        except OSError:
            raise FastKVSConnectionError("connection lost")            

    def get(self, key):
        response = self.send_command(f"GET {key}")
        if response == "NULL":
            return None
        return response

    def set(self, key, value):
        response = self.send_command(f"SET {key} {value}")
        if response != "OK":
            raise FastKVSProtocolError(f"unexpected response: {response}")
        return True

    def delete(self, key):
        response = self.send_command(f"DEL {key}")
        if response != "OK":
            raise FastKVSProtocolError(f"unexpected response: {response}")
        return True

    def stats(self):
        try:
            self.socket.sendall("STATS\n".encode("utf-8"))
            response = self.socket.recv(4096).decode("utf-8").strip()
            
            result = {}
            for line in response.split("\n"):
                line = line.strip()
                if ":" in line:
                    key, value = line.split(":", 1)
                    result[key.strip()] = value.strip()
            return result
        except socket.timeout:
            raise FastKVSTimeoutError("server did not respond in time")
        except OSError:
            raise FastKVSConnectionError("connection lost")