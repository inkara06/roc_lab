import socket
import json
import uuid
import time

SERVER_IP = "server_ip"
PORT = 5000
TIMEOUT = 2
RETRIES = 3

def call_rpc(method, params):
    request_id = str(uuid.uuid4())

    request = {
        "request_id": request_id,
        "method": method,
        "params": params
    }

    for attempt in range(RETRIES):
        try:
            print(f"Attempt {attempt+1} sending request...")

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(TIMEOUT)
            s.connect((SERVER_IP, PORT))
            s.send(json.dumps(request).encode())

            data = s.recv(1024).decode()
            s.close()

            response = json.loads(data)

            if response["request_id"] == request_id:
                print("Response:", response)
                return

        except:
            print("Timeout or connection error. Retrying...")

    print("RPC failed after retries")


# TEST CALL
call_rpc("add", {"a": 10, "b": 5})
