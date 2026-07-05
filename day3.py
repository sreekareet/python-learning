port = 6370
if port == 7379:
    print("Port is set to 7379")
elif port == 6379:
    print("Port is set to 6379")
else:
    print("unknown port")

servers = ["fastkvs", "redis", "memcached"]

for server in servers:
    print(server)

#for loop with index
for index, server in enumerate(servers):
    print(f"Server {index}: {server}")

#for ranege loop
for i in range(5):
    print(i)
for i in range(1, 6):
    print(i)
for i in range(0, 10, 2):
    print(i)

kv_store = {"user:1": "alice", "user:2": "bob", "user:3": "charlie"}
for key, value in kv_store.items():
    if value .startswith("a") or value.startswith("b"):
        print(key)

#while loop
attempts = 0
while attempts < 3:
    print(f"connecting... attempt {attempts + 1}")
    attempts += 1

print("done")
 