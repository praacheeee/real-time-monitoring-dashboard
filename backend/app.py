# app.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import psutil
import asyncio
import uvicorn
import time
import json

app = FastAPI()

# Allow frontend served from file:// or localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def sample_system():
    """
    Returns a dict with CPU, memory, disk_io, net_io and top processes.
    """
    # system
    cpu_percent = psutil.cpu_percent(interval=None)
    cpu_per_cpu = psutil.cpu_percent(interval=None, percpu=True)
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_io_counters()
    net = psutil.net_io_counters()

    # top processes by cpu
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'create_time']):
        try:
            info = p.info
            procs.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    # sort and pick top 15
    procs_sorted = sorted(procs, key=lambda x: x.get('cpu_percent', 0), reverse=True)[:15]

    return {
        "timestamp": time.time(),
        "cpu_percent": cpu_percent,
        "cpu_per_cpu": cpu_per_cpu,
        "mem_total": mem.total,
        "mem_available": mem.available,
        "mem_used": mem.used,
        "mem_percent": mem.percent,
        "swap_total": swap.total,
        "swap_used": swap.used,
        "swap_percent": swap.percent,
        "disk_read": disk.read_bytes if disk else 0,
        "disk_write": disk.write_bytes if disk else 0,
        "net_bytes_sent": net.bytes_sent if net else 0,
        "net_bytes_recv": net.bytes_recv if net else 0,
        "processes": procs_sorted
    }

@app.get("/api/processes")
async def get_processes():
    """Return current process list (lightweight REST endpoint)."""
    data = sample_system()
    # return only processes to keep size reasonable
    return {"timestamp": data["timestamp"], "processes": data["processes"]}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Push system metrics every second over WebSocket."""
    await websocket.accept()
    try:
        # prime psutil CPU counters
        psutil.cpu_percent(interval=None)
        for p in psutil.process_iter(['pid']):
            try:
                p.cpu_percent(interval=None)
            except Exception:
                pass

        prev_disk = psutil.disk_io_counters() or None
        prev_net = psutil.net_io_counters() or None

        while True:
            data = sample_system()
            # Compute deltas for nicer network/disk rates
            disk = psutil.disk_io_counters() or None
            net = psutil.net_io_counters() or None
            if prev_disk and disk:
                data["disk_read_rate"] = max(0, disk.read_bytes - prev_disk.read_bytes)
                data["disk_write_rate"] = max(0, disk.write_bytes - prev_disk.write_bytes)
            else:
                data["disk_read_rate"] = 0
                data["disk_write_rate"] = 0
            if prev_net and net:
                data["net_sent_rate"] = max(0, net.bytes_sent - prev_net.bytes_sent)
                data["net_recv_rate"] = max(0, net.bytes_recv - prev_net.bytes_recv)
            else:
                data["net_sent_rate"] = 0
                data["net_recv_rate"] = 0
            prev_disk = disk
            prev_net = net

            await websocket.send_text(json.dumps(data, default=str))
            await asyncio.sleep(1)  # push every 1 second
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print("WebSocket error:", e)
        await websocket.close()

if __name__ == "__main__":
    # Run with: uvicorn app:app --reload --host 0.0.0.0 --port 8000
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
