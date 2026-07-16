#to convert all the server names to uppercase and store them in a new list
servers = ["fastkvs", "redis", "memcached"]
upper_servers = []
for server in servers:
    upper_servers.append(server.upper())
print(upper_servers)

#alternative way using list comprehension
upper_servers_comp = [server.upper() for server in servers]
print(upper_servers_comp)

ports = [7379, 8080, 9090, 3000, 7380]

#filtering ports greater than 8000 using list comprehension
high_ports = [port for port in ports if port > 8000]
print(high_ports)

#filtering even ports using list comprehension
even_ports = [port for port in ports if port % 2 == 0]
print(even_ports)

kv_store = {"user1": "alice", "user2": "bob", "user3": "charlie"}
#filtering key-value pairs where the value starts with 'a' or 'b'
filtered = {key: value for key, value in kv_store.items() if value.startswith(("a", "b"))}
print(filtered)

lines = [
    "SET user:1 alice OK",
    "GET user:1 OK",
    "GET user:2 NULL",
    "DEL user:1 OK",
    "GET user:3 ERROR",
]

#filtering lines that end with "OK" using list comprehension
l = [line for line in lines if line.split()[-1] == "OK"]
print(l)