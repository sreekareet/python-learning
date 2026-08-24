from client import FastKVSClient

with FastKVSClient("127.0.0.1", 7379) as client:
    client.set("user:1", "alice")
    client.set("user:2", "bob")
    
    print(client.get("user:1"))
    print(client.get("user:99"))
    
    client.delete("user:1")
    print(client.get("user:1"))