import logging
logging.basicConfig(level=logging.INFO)

from client import FastKVSClient
from exceptions import FastKVSConnectionError, FastKVSError

try:
    with FastKVSClient("127.0.0.1", 7379) as client:
        client.set("user:1", "alice")
        client.set("user:2", "bob")
        client.get("user:1")
        client.get("user:99")
        client.delete("user:1")
        
        stats = client.stats()
        print("=== Server Stats ===")
        for key, value in stats.items():
            print(f"  {key}: {value}")

except FastKVSConnectionError as e:
    print(f"connection error: {e}")
except FastKVSError as e:
    print(f"fastkvs error: {e}")