from client import FastKVSClient

# test that close() is called even when exception is thrown
try:
    with FastKVSClient("127.0.0.1", 7379) as client:
        client.get("user:1")
        raise Exception("something went wrong mid-operation")
        client.set("user:2", "bob")  # this should never run
except Exception as e:
    print(f"caught: {e}")

print("connection still closed cleanly")