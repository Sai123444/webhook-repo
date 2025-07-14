# 🚀 GitHub Webhook Listener App

A full-stack application that listens to real-time GitHub events (Push, Pull Request, Merge), stores them in MongoDB, and displays them in a live updating frontend every 15 seconds.

---

## 💡 Project Overview

This project was built as part of a **developer assessment** for TechStaX. It showcases my ability to work with **webhooks**, **Flask**, **MongoDB**, and build a real-time **data-driven UI**.

It involves:

✅ Setting up GitHub Webhooks  
✅ Building a Flask backend to handle & parse webhook events  
✅ Storing data in MongoDB (Atlas)  
✅ Creating a clean frontend that refreshes every 15 seconds  
✅ Using ngrok to expose localhost for webhook testing  

---

## 🖼️ UI Preview

![Preview](https://via.placeholder.com/800x400?text=Live+GitHub+Webhook+Event+Stream)

---

## ⚙️ Technologies Used

| Tool           | Purpose                        |
|----------------|-------------------------------|
| Python + Flask | Webhook server backend         |
| MongoDB Atlas  | Cloud database for events      |
| HTML + JS      | Frontend polling UI            |
| Ngrok          | Public URL for local server    |
| GitHub Actions | Trigger webhook events         |

---

## 🧪 Webhook Events Captured

| Event         | Format Example |
|---------------|----------------|
| **Push**       | `"Sai123 pushed to main on Mon, 14 Jul 2025 10:30 AM UTC"` |
| **Pull Request** | `"Sai123 submitted a pull request from feature-1 to main on ..."` |
| **Merge** *(Bonus)* | `"Sai123 merged branch dev to main on ..."` |

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Sai123444/webhook-repo.git
   cd webhook-repo
Set up virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your MongoDB Atlas connection string in app.py

Run Flask server

bash
Copy
Edit
python app.py
Expose localhost with ngrok

bash
Copy
Edit
ngrok http 5000
Add webhook to your GitHub repo

Payload URL: https://<your-ngrok-subdomain>.ngrok-free.app/webhook

🧠 What I Learned
How to connect GitHub Webhooks to a live Flask server

Parsing and storing JSON payloads from real-time events

Polling a MongoDB collection in the frontend

Building full-stack systems with clean architecture

✉️ Contact
Feel free to connect if you want to discuss the project!

Sreesai Malli
📧 mallisreesai2004@gmail.com
🔗 GitHub

“Build real. Learn deep. Ship fast.”
