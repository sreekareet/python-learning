class FastKVSClient:
    def get(self, key):
        return f"fastkvs:get:{key}"
    
    def set(self, key, value):
        return f"fastkvs:set:{key}={value}"

class MockClient:
    def get(self, key):
        return f"mock:get:{key}"
    
    def set(self, key, value):
        return f"mock:set:{key}={value}"

def run_benchmark(client, keys):
    for key in keys:
        result = client.get(key)
        print(result)

real = FastKVSClient()
mock = MockClient()

run_benchmark(real, ["user:1", "user:2"])
run_benchmark(mock, ["user:1", "user:2"])

class TestClient:
    def __init__(self): #constructor method
        self.store = {}
    
    def get(self, key): #self is a reference to the instance of the class(like this in c++)
        return self.store.get(key, "NULL")
    
    def set(self, key, value):
        self.store[key] = value
        return "OK"

test = TestClient()   # __init__ runs, self.store = {} created
test.set("user:1", "alice")
print(test.get("user:1"))
print(test.get("user:99"))