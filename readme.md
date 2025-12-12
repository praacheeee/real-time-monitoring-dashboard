# 💻 Real-Time Monitoring Dashboard  

A fully interactive, visually rich dashboard that displays **real-time system monitoring metrics**, including:

- 🔥 **Live CPU Usage**
- 🧠 **Live Memory Usage**
- 📊 **Animated 60-second CPU History Graph**
- 📁 **Top Processes (with search filter)**
- 🌙 **Dark/Light Mode Toggle**
- ✨ **Neon UI & Smooth Animations**

This project uses:

- **Flask (Python)** → Backend API  
- **psutil** → Reading live system stats  
- **Chart.js** → Graphs and visualizations  
- **HTML/CSS/JS** → Frontend UI  

---

## 🚀 Features

### ✔ Real-Time System Stats  
Fetches live CPU & memory usage every second.

### ✔ Beautiful Donut Charts  
Interactive doughnut charts to display live usage values.

### ✔ Neon CPU History Graph  
60-second animated CPU usage history with gradient glow.

### ✔ Searchable Process Table  
Displays the top processes and allows keyword filtering.

### ✔ Modern Dark Mode (Default)  
Toggle between **Dark Mode** and **Light Mode** instantly.

### ✔ Smooth UI Animations  
Cards enlarge slightly on hover with neon highlights.

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Backend | Flask (Python) |
| System Stats | psutil |
| Communication | REST API (JSON) |

---

## 📂 Project Structure

Real-time Monitoring Dashboard project/
│
├── backend/
│ └── app.py # Flask backend API
│
├── frontend/
│ └── index.html # Dashboard UI
│
└── README.md # Project documentation

---

## ⚙️ Setup & Installation

### 1️⃣ Install Dependencies

Open terminal inside the project folder:

pip install flask flask_cors psutil

---

### 2️⃣ Run the Backend (Flask)

python backend/app.py


It will start at:



http://127.0.0.1:5000/stats


---

### 3️⃣ Run the Frontend

Option A — Open the HTML file:
frontend/index.html


Option B — Use VS Code Live Server (recommended).  
Your UI will open at:



http://127.0.0.1:5500/frontend/index.html


---

## 🌍 Sharing the Project

### ✔ If someone wants to monitor **their own system**  
They must:

1. Clone your repo  
2. Install dependencies  
3. Run `app.py`  
4. Open the frontend  

### ✔ If you want to make a PUBLIC online dashboard  
You need to deploy:

- Backend → Render/Railway  
- Frontend → GitHub Pages/Netlify  

(Hosted backend will show **server stats**, not your laptop.)

---

## 🧪 Future Enhancements

- GPU usage monitoring  
- RAM usage per process  
- Network upload/download graphs  
- System temperature tracking  
- Email/SMS alerts on high CPU usage  

---

## 📝 License  
This project is free to use for educational purposes.

---

## 🎉 Author  
Made by **Prachee** (GitHub: @praacheeee)  