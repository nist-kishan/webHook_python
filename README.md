# 🔔 GitHub Webhook Event Visualizer
##
A lightweight Flask + React app that listens to GitHub webhook events and displays them in real-time using a clean, modern UI.

---

## 📸 Screenshot
<img width="1123" height="441" alt="Screenshot 2025-07-14 190141" src="https://github.com/user-attachments/assets/7e06214e-d50c-4304-873e-09f8016c208e" />

<!-- Add your<img width="1123" height="441" alt="Screenshot 2025-07-14 190141" src="https://github.com/user-attachments/assets/48b5696c-5467-498f-a114-7d33d54b2824" />
 uploaded images here -->

---

## 🧩 Description

This project provides a visual way to monitor GitHub repository activity through webhook events like:

- **Pushes**
- **Pull Requests**
- **Merges**

The backend uses **Flask** with **MongoDB** to handle and store events, while the frontend uses **React** with **Tailwind CSS** and **lucide-react** icons for a smooth, minimal experience.

---

## 🚀 Features

- Real-time webhook listener (`/webhook`)
- Fetch latest events every 15 seconds (`/events`)
- Handles:
  - `push`
  - `pull_request`
  - `merge` (auto-detected via closed PRs)
- Responsive UI with icon badges and time formatting
- Easily deployable with **ngrok** or public server

---

## 🛠️ Tech Stack
```
| Layer       | Tech                          |
|------------|-------------------------------|
| Backend     | Flask, PyMongo, Python dotenv |
| Frontend    | React, Tailwind CSS, Axios    |
| Database    | MongoDB                       |
| Icons       | lucide-react                  |
| Dev Tools   | ngrok, Vite                   |
```
---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Backend Setup
```
cd backend/
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### 3. Create .env file
```
MONGO_URI=mongodb://localhost:27017/
MONGO_DB=github_webhooks
MONGO_COLLECTION=events
CORS_ORIGINS=http://localhost:5173
```

### 4. Run Backend
```
Run the server:
```


### 5. 
```
cd frontend/
npm install
npm run dev
```

### 5. Exposing Webhook (ngrok)
```
ngrok http 5000
```

## 📂 Folder Structure
```
📦 webhook-repo
├── app/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── views/
│   ├── __init__.py
│   └── main.py
├── frontend/
│   └── src/
├── .env
├── README.md
└── requirements.txt
```
