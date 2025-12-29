LAB DEMO : https://youtu.be/sCyoKeAUzxY
# RPC Lab 1 — Distributed Computing

Simple RPC implementation using Python sockets (TCP) and JSON.

## Files
- `server.py` — RPC server
- `client.py` — RPC client with timeout + retries

## Run (EC2)
### Server
```bash
python3 server.py

Client

Edit SERVER_IP in client.py, then:
python3 client.py
Failure demo

Example (server side):
sudo ufw deny 5000
Client will show timeouts + retries, demonstrating at-least-once semantics.
