def get_all_keys1(kv_store):
    result = []
    for key in kv_store:
        result.append(key)
    return result

store = {"user:1": "alice", "user:2": "bob", "user:3": "charlie"}
keys = get_all_keys1(store)
for key in keys:
    print(key)

# get all keys using a generator -- memory efficient
def get_all_keys(kv_store):
    for key in kv_store:
        yield key

store = {"user:1": "alice", "user:2": "bob", "user:3": "charlie"}
for key in get_all_keys(store):
    print(key)   

def big_log_reader(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

for line in big_log_reader("week01_project/server.log"):
    print(line)  

store = {"user:1": "alice", "user:2": "bob", "user:3": "charlie"}

gen = (key for key in store)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))  
print(next(gen))     #stopiteration error because there are no more items in the generator