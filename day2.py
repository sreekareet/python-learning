#---lists---
servers = ["fastkvs", "redis", "memcached"]
print(servers[0]) 
print(len(servers))
servers.append("custom")
print(servers)

#------dictionaries---
config = {"host": "127.0.0.1", "port": 7379, "max_connections": 10}
print(config["port"])
print(config.get("timeout", 30)) #only prints the default value if the key is not found doesnt add to config

config["timeout"] = 30 #adds a new key-value pair to the dictionary, overwrites the value if the key already exists
config.setdefault("max_connections", 20) #does not overwrite the value if the key already exists, only adds the key-value pair if the key does not exist

#---loop over dictionaries---
for key, value in config.items():
    print(f"{key} = {value}")

# --- tuples and sets ---
point = (7379, "localhorst") #tuples are immutable, cannot be changed after creation
print(point[0])

ports = {7379, 7379, 8080, 8080, 9090} #sets are unordered collections of unique elements
print(ports)

#practice
# FastKVS fake data - you write the code
kv_store = {"user:1": "alice", "user:2": "bob", "user:3": "charlie"}

# 1. print the value for "user:2" 
print(kv_store["user:2"])
# 2. add a new key "user:4" with value "diana"
kv_store["user:4"] = "diana"
# 3. print how many keys are in the dict
print(len(kv_store))
# 4. loop and print all keys and values
for key, value in kv_store.items():
    print(f"{key} = {value}")