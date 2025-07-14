# 🧠 CoolGuru – AI Learning Assistant for CBSE (Class 6–8)

> **For Every Student. In Every Language. An Invisible Guru.**

---

![CoolGuru Flowchart](https://raw.githubusercontent.com/YourUsername/coolguru/main/assets/coolguru_flowchart.png)

---

## 🚀 Project Overview
**CoolGuru** is an open-source, modular EdTech platform, focused on **CBSE Class 6–8** students. The goal is to combine **AI assistance**, **curriculum mastery**, and **local language support** to create an inclusive and impactful learning experience.

CoolGuru is designed as a **three-way handshake** between students, teachers, and parents — ensuring all stakeholders are part of the child's learning journey.

> ⚠️ Note: While CoolGuru’s foundation is open and transparent, the full-featured platform will be offered as a **paid subscription service** in order to sustain growth, content development, and future innovation.

---

## 🎯 Key Features (MVP)
- 📚 **Subject-wise Quiz Assistant** (Science, Social Science, Maths, English)
- 💬 **Topic Explainer Chatbot** – "Explain Chapter 3 of Class 6 SST"
- 🧾 **Worksheet Generator** (MCQs, FITB, Short answers)
- 🌐 **Subject Switcher** (via Gradio or Telegram)
- 🗣️ **Local Language Support** (Kannada/Hindi – Phase 2)

---

## 📊 Parent & Teacher Dashboard (Mockup Features)
CoolGuru envisions a user-friendly dashboard for teachers and parents to gain real-time insight into student progress.

### 👨‍🏫 Teacher Dashboard
- 📈 Class-wide quiz analytics (accuracy, participation)
- ✍️ Assign worksheets by chapter/topic
- 📂 Upload custom questions or resources
- 🎓 Track students needing additional support

### 👨‍👩‍👧 Parent Dashboard
- 📊 View child’s weekly learning progress
- 🧠 Receive personalized tips for home practice
- 🔔 Notification alerts (quizzes completed, topics covered)
- 📥 Download printable worksheets to reinforce learning offline

---

## 🧱 Project Structure
```
coolguru/
├── app/
│   ├── chatbot.py              # Core chatbot logic
│   ├── quiz_engine.py          # Handles quiz/answer checking
│   ├── worksheet_generator.py  # Builds custom worksheets
│   └── ncert_loader.py         # Loads structured JSON from /data
├── data/
│   ├── class6_science.json
│   ├── class6_maths.json
│   └── ... (per subject)
├── templates/                  # For printable worksheets (PDF/HTML)
├── static/                     # Optional UI assets
├── requirements.txt
├── README.md
└── run_app.py                  # Launch Gradio or FastAPI app
```

---

## 📦 Installation
```bash
# Clone the repo
https://github.com/YourUsername/coolguru.git
cd coolguru

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python run_app.py
```

---

## 📘 Usage Examples
- Type `quiz` to begin a multiple choice quiz
- Type `subject:maths` to switch topic
- Type `Explain Chapter 4 of Class 6 Science` to get a simple explanation
- Type `worksheet:Science Chapter 1` to generate a worksheet (coming soon)

---

## 📋 GitHub Project Boards

### 🔹 Phase 1 – MVP
- ✅ Build chatbot & subject switcher
- ✅ Load JSON data
- 🚧 quiz_engine.py & worksheet_generator.py
- ✅ Gradio interface with chatbot interaction

### 🔹 Phase 2 – Dashboards & Expansion
- 🔧 Build parent/teacher dashboards
- 🔧 Add PDF worksheet export
- 🔧 Enable Kannada/Hindi explanations
- 📲 Prepare mobile or Telegram app version

---

## 🌍 Vision for Phase 2
- Offline support (preload content)
- Teacher login for custom worksheet generation
- Parent portal for tracking progress and reinforcement
- PDF worksheet export
- Kannada / Hindi explanations
- Real-time Telegram/WhatsApp interface

---

## 🤝 Contributions Welcome
If you're passionate about **AI in Indian education**, please contribute:
- Add new questions to JSON sets
- Improve translations or explanations
- Build web or mobile interfaces
- Build integrations for teachers and parent-facing dashboards

---

## 📜 License
MIT License – Free to use, modify, and redistribute core logic. Final platform features and dashboards may be offered under a commercial license.

---

## 👤 Project by Malathi Kamath
Connect on [LinkedIn](https://www.linkedin.com/in/malathi-kamath-92430720) | [GitHub](https://github.com/MalathiKamath)

Let’s reimagine CBSE learning – for every student, in every language. 🇮🇳✨

