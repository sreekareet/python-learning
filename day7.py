def get_value2(kv_store, key):
    try:
        return kv_store[key]
    except KeyError:
        return None

store = {"user:1": "alice"}
result = get_value2(store, "user:1")
print(result)

result = get_value2(store, "user:99")
print(result)


# exception handling with custom exceptions
class FastKVSError(Exception):
    pass

class FastKVSConnectionError(FastKVSError):
    pass

class FastKVSKeyError(FastKVSError):
    pass

def get_value(kv_store, key):
    if not kv_store:
        raise FastKVSConnectionError("store is not available")
    if key not in kv_store:
        raise FastKVSKeyError(f"key '{key}' not found")
    return kv_store[key]

store = {"user:1": "alice"}

try:
    print(get_value(store, "user:1"))
    print(get_value(store, "user:99"))
except FastKVSKeyError as e:
    print(f"key error: {e}")
except FastKVSConnectionError as e:
    print(f"connection error: {e}")
except FastKVSError as e:
    print(f"general error: {e}")

#finally block
def read_from_store(kv_store, key):
    try:
        value = kv_store[key]
        return value
    except KeyError:
        raise FastKVSKeyError(f"key '{key}' not found")
    finally:
        print("cleanup always runs here")

try:
    print(read_from_store(store, "user:1"))
    print(read_from_store(store, "user:99"))
except FastKVSKeyError as e:
    print(f"caught: {e}")    