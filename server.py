import socket, json, time

HOST = "server_ip"
PORT = 5000

def add(a, b): return a + b
def get_time(): return time.ctime()
def reverse_string(s): return s[::-1]

methods = {"add": add, "get_time": get_time, "reverse_string": reverse_string}

print(f"RPC Server running on {HOST}:{PORT}")

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen(10)

while True:
    conn, addr = srv.accept()
    print("Connected from", addr)

    data = conn.recv(4096).decode()
    if not data:
        conn.close()
        continue

    req = json.loads(data)
    rid = req.get("request_id")
    method = req.get("method")
    params = req.get("params", {})

    try:
        result = methods[method](**params)
        resp = {"request_id": rid, "result": result, "status": "OK"}
    except Exception as e:
        resp = {"request_id": rid, "result": None, "status": "ERROR", "error": str(e)}

    conn.sendall(json.dumps(resp).encode())
    conn.close()
