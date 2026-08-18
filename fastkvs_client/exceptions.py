class FastKVSError(Exception):
    pass

class FastKVSConnectionError(FastKVSError):
    pass

class FastKVSTimeoutError(FastKVSError):
    pass

class FastKVSKeyError(FastKVSError):
    pass

class FastKVSProtocolError(FastKVSError):
    pass

#FastKVSError — base class for everything. Caller can catch this one type to handle any FastKVS failure, or catch specific ones for fine-grained handling. Same design as C++ exception hierarchies.

#FastKVSConnectionError — raised when the TCP connection fails. Server not running, wrong host/port, network issue. You'll raise this in connect().

#FastKVSTimeoutError — raised when the server doesn't respond within the timeout window. Different from connection error — you connected fine but the server is slow or hung. Important distinction for a benchmark tool.

#FastKVSKeyError — raised when GET returns NULL and the caller needs to know the key didn't exist. Not always an error — sometimes you want None back instead. Caller decides.

#FastKVSProtocolError — raised when the server sends back something unexpected — malformed response, unknown format. Shouldn't happen with your server but defensive programming matters, especially for a systems engineer.