#functions
from sqlite3 import connect


def connect1(host, port):
    print(f"Connecting to {host}:{port}...")
    return True

result  = connect1("127.0.0.1", 7379)
print (result)

def connect(host, port = 7379, timeout = 30):
    print(f"Connecting to {host}:{port} with timeout {timeout}...")
    return True

connect("127.0.0.1")            #uses both defaults
connect("127.0.0.1", 8080)      #overrides port, uses default timeout
connect("127.0.0.1", timeout=5)  #overrides timeout by name, uses default port and its called KEYWORD ARGUMENT

#mutable default arguments
def add_server(name, servers = []):
    servers.append(name)
    return servers

print(add_server("fastkvs"))  # returns ['fastkvs']
print(add_server("redis"))  # returns ['fastkvs', 'redis'] 
print(add_server("memcached"))  # returns ['fastkvs', 'redis', 'memcached']

def add_server1(name, server_list=None):
    if server_list is None:
        server_list = []
    server_list.append(name)
    return server_list

print(add_server1("fastkvs"))
print(add_server1("redis"))
print(add_server1("memcached"))

#multiple return values
def get_server_info(name):
    host = "127.0.0.1"
    port = 7379
    return host, port #returns a tuple

host, port = get_server_info("fastkvs")
print(f"host={host} port={port}")

# variable-length arguments
def log(*args, **kwargs):
    for arg in args:
        print(f"arg: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

log("fastkvs", "started", host="127.0.0.1", port=7379)
