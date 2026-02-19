# RAJ-Sahayak AI Assistant 🤖

> An intelligent multilingual AI chatbot for college students — Smart India Hackathon (SIH) Project

![RAJ-Sahayak Banner](https://img.shields.io/badge/SIH-2024-purple?style=for-the-badge)
![React](https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge&logo=react)
![Node.js](https://img.shields.io/badge/Node.js-Express-339933?style=for-the-badge&logo=node.js)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb)

---

## 📌 Overview

**RAJ-Sahayak** is a multilingual AI-powered assistant designed to help college students get instant answers to their queries — about admissions, exams, fees, hostel, counselling, and more. It features a powerful admin dashboard for managing FAQs, staff, and analytics.

---

## ✨ Features

### 🌐 Chatbot (Student-Facing)
- Multilingual support: **English, Hindi, Tamil, Telugu, Gujarati, Marathi** and more
- Natural language Q&A powered by AI
- Clean, accessible chat interface
- Real-time responses

### 🛠️ Admin Panel
- **Dashboard** — Total students, total queries, quick actions
- **PDF FAQ Generator** — Upload PDFs and auto-generate Q&A pairs using AI
- **Staff Management** — Add, edit, activate/deactivate staff members
- **Analytics Dashboard** — Language distribution, query categories, accuracy rate, escalations
- **Admin Settings** — Manage account email/password

---

## 📊 Analytics Highlights

| Metric | Value |
|--------|-------|
| Total Users | 238 |
| Total Queries | 545 |
| AI Accuracy Rate | 88.51% |
| Human Escalations | 87 |
| Languages Supported | 9 |

**Top Query Categories:** Management, Exams, Counselling, Hostel, Fees, Library, Admission

---

## 🗂️ Project Structure

```
SIH_FINAL-Code/
├── final/
│   ├── Backend/               # Node.js + Express API
│   │   ├── routes/            # API routes
│   │   ├── uploaded/          # Uploaded PDF storage
│   │   ├── server.js          # Main server entry
│   │   ├── app.py             # Python AI processing
│   │   ├── main.py            # FAQ extraction logic
│   │   ├── .env               # Environment variables
│   │   └── package.json
│   └── dist/                  # Frontend build output
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** v18+
- **Python** 3.10+
- **MongoDB** (local or Atlas)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd SIH_FINAL-Code/final
   ```

2. **Install backend dependencies**
   ```bash
   cd Backend
   npm install
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the `Backend/` folder:
   ```env
   MONGO_URI=your_mongodb_connection_string
   PORT=5000
   JWT_SECRET=your_jwt_secret
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Run the backend server**
   ```bash
   node server.js
   ```

6. **Run the frontend (development)**
   ```bash
   # From the project root
   npm install
   npm run dev
   ```

   Frontend runs at: `http://localhost:5173`  
   Backend API runs at: `http://localhost:5000`

---

## 🔐 Admin Access

| Role | Email | Password |
|------|-------|----------|
| Admin | `admin@college.edu` | `(set in .env)` |
| Staff | `staff@college.edu` | `(set in .env)` |

> Quick demo access buttons are available on the login screen.

---

## 📄 PDF FAQ Generator Workflow

1. Admin uploads one or more PDF files (brochures, circulars, handbooks)
2. PDFs are dragged into the **AI Processing Hub**
3. Click **"Process All Files"** — AI extracts intelligent Q&A pairs
4. Review generated FAQs
5. Click **"Sync to Chatbot"** — FAQs are instantly available to students

---

## 🧑‍💼 Staff Management

- Add staff with full name, email, department, role, phone, and join date
- Departments: Computer Science, Administration, Examination, Mathematics, Library
- Toggle staff active/inactive status
- View, edit, or remove staff members

---

## 🌍 Supported Languages

| Language | Code |
|----------|------|
| English | en |
| Hindi | hi |
| Tamil | ta |
| Telugu | te |
| Gujarati | gu |
| Marathi | mr |
| Kannada | kn |
| Bengali | bn |
| Malayalam | ml |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React (Vite) |
| Backend | Node.js + Express |
| Database | MongoDB |
| AI/ML | Python (Gemini API / LLM) |
| Styling | CSS / Tailwind |
| Auth | JWT |

---

## 📸 Screenshots

| Feature | Description |
|---------|-------------|
| Chatbot | Multilingual student-facing AI assistant |
| Admin Login | Secure dashboard sign-in |
| Dashboard | Overview of students, queries, and quick actions |
| FAQ Generator | PDF-to-FAQ AI pipeline |
| Staff Management | Add and manage staff members |
| Analytics | Language distribution and query category insights |

---

## 🏆 Built For

**Smart India Hackathon (SIH) 2025**  
Theme: Education / AI for Students  

