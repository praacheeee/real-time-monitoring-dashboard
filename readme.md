💻 Real-Time Monitoring Dashboard

A fully interactive, real-time system monitoring dashboard with a modern neon UI, WebSocket live updates, and rich visual analytics.

It provides continuous monitoring of:

🔥 CPU Usage (Live + Per-Core)
🧠 Memory Usage (Live + Usage Summary)
🌐 Network Throughput (Upload/Download Rate)
💽 Disk I/O Rate (Read/Write)
📁 Top Processes (with search, sort, and modal details)
📊 4 Live Animated Charts (CPU, Memory, Network, Disk)
🌙 Dark/Light Mode Toggle
⚡ Real-time updates every second via WebSocket

This project uses:

Backend (Python)

⚙️ FastAPI — High-performance ASGI backend

🔄 WebSockets — Live streaming updates

📡 psutil — System metrics

🔧 uvicorn — ASGI server

Frontend

🎨 HTML / CSS (Custom Neon UI)

🧠 JavaScript

📊 Chart.js for animated graphs

🚀 Features
✔ Real-Time Live Metrics (WebSocket)

The backend pushes system stats every second:

CPU %

Per-core CPU

Memory usage

Disk read/write rate

Network upload/download

Top running processes

✔ Interactive Neon UI

Smooth hover animations, modern cards, and a clean grid layout.

✔ 4 Live Charts

CPU usage chart

Memory usage chart

Network throughput graph

Disk I/O graph
All update in real time.

✔ Top Processes Table

Includes:

Sorting (PID, Name, CPU %, MEM %)

Searching (live filtering)

Modal popup with extra details (user, cmdline, etc.)

✔ Pause, Refresh & Export

⏸ Pause live feed

🔄 Refresh charts

📤 Export visible process list to CSV

✔ Theme Toggle

Dark mode by default → switch to light mode instantly.

🛠️ Tech Stack
Component	Technology
Frontend	HTML, CSS, JavaScript, Chart.js
Backend	FastAPI + WebSockets
System Stats	psutil
Server	uvicorn
Communication	WebSocket (live), REST (for process snapshots)
📂 Project Structure
Real-time Monitoring Dashboard project/
│
├── backend/
│   └── app.py               # FastAPI backend with WebSocket
│
├── frontend/
│   └── index.html           # Modern dashboard UI
│
├── venv/                    # Virtual environment (ignored by Git)
│
├── .gitignore
└── README.md

⚙️ Setup & Installation
1️⃣ Create Virtual Environment

Inside the project folder:

python -m venv venv


Activate it:

Windows PowerShell:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate

2️⃣ Install Dependencies
pip install fastapi uvicorn psutil websockets

3️⃣ Run the Backend Server

From inside:

Real-time Monitoring Dashboard project/backend


Run:

uvicorn app:app --reload --host 127.0.0.1 --port 8000


Backend WebSocket is now live at:

ws://127.0.0.1:8000/ws

4️⃣ Run the Frontend
Option A — Open the HTML file

Open:

frontend/index.html

Option B (Recommended) — Use VS Code Live Server

This gives correct CORS behavior and auto-reload.

Your UI will open at:

http://127.0.0.1:5500/frontend/index.html


🤝 The page will automatically connect to:

ws://127.0.0.1:8000/ws

🌍 Sharing the Project
✔ If someone wants to use your dashboard locally

They need to:

Clone your repo

Create virtual environment

Install FastAPI + psutil

Run backend

Open frontend

✔ Publishing it online

Front-end can be deployed anywhere (GitHub Pages, Netlify).
But backend must run on a server (Render, Railway, etc.)

⚠ Online backend will only monitor that server, not the user's computer.

🧪 Future Enhancements

GPU usage monitoring

System temperature

Process kill API (with authentication)

Docker support

Persistent logs

Alerts on high CPU/Memory

📝 License

This project is open for educational and academic use.

🎉 Author

Built with ❤️ by Prachee
GitHub: https://github.com/praacheeee/real-time-monitoring-dashboard
