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
        print(f"connecting to {self.host}:{self.port}")
        # real socket code comes next week
        pass

    def close(self):
        print("closing connection")
        # real socket cleanup comes next week
        pass

    def get(self, key):
        print(f"GET {key}")
        # real implementation comes next week
        pass

    def set(self, key, value):
        print(f"SET {key} {value}")
        # real implementation comes next week
        pass

    def delete(self, key):
        print(f"DEL {key}")
        # real implementation comes next week
        pass