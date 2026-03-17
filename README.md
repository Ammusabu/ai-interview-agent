# AI Interview Assistant

> An AI agent that simulates real technical interviews — generates role-based questions, evaluates your answers with an LLM, and returns structured scores and feedback. Built to demonstrate backend engineering, AI integration, and system design.

<img width="1600" height="951" alt="image" src="https://github.com/user-attachments/assets/269be6e9-38dc-466c-a31f-93fd2e7336a7" />

<br>

## What It Does

You pick a role and difficulty level. The agent takes it from there: asks you interview questions, listens to your answers, and evaluates them like a real interviewer — giving you a score, specific feedback, and suggestions to improve. Every session is dynamic, non-repetitive, and tailored to your level.

<br>

## Features

| Feature | Details |
|---|---|
| **AI Question Generation** | Role-aware, level-aware questions generated fresh by LLM — no static question banks |
| **Answer Evaluation** | Returns score (X/10), written feedback, and improvement suggestions per answer |
| **Async Background Tasks** | Celery workers handle heavy AI workloads asynchronously |
| **Caching Layer** | Redis caches responses and acts as the Celery message broker |
| **JWT Authentication** | Secure login, registration, and session management |
| **Modern UI** | Particle-animated background, glassmorphism cards, smooth interactions |

<br>

## System Architecture

```
Frontend (HTML / CSS / JS)
        ↓
FastAPI Backend  ──→  JWT Auth
        ↓
Service Layer (AI Logic)
        ↓
Groq LLM API (Inference)
        ↓
SQLite / PostgreSQL
        ↓
Redis (Cache + Message Broker)
        ↓
Celery Workers (Async Tasks)
```

<br>

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI, Python, SQLAlchemy |
| **Database** | SQLite (dev) → PostgreSQL (prod) |
| **AI Inference** | Groq API (OpenAI-compatible SDK) |
| **Queue & Cache** | Redis + Celery |
| **Frontend** | HTML, CSS, JavaScript, Particles.js |
| **Auth** | JWT (JSON Web Tokens) |

<br>

## Project Structure

```
AI_Interview_Evaluation_System/
│
├── app/
│   ├── api/           # Route handlers
│   ├── core/          # Security & auth logic
│   ├── db/            # Database setup & connection
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic request/response schemas
│   ├── services/      # AI question generation & evaluation
│   └── main.py        # Application entry point
│
├── static/            # CSS & assets
├── templates/         # HTML templates
├── workers/           # Celery worker definitions
├── requirements.txt
└── README.md
```

<br>

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-interview-agent.git
cd ai-interview-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Start Redis

```bash
brew services start redis   # macOS
# sudo service redis start  # Linux

redis-cli ping              # Should return: PONG
```

### 6. Run the backend

```bash
uvicorn app.main:app --reload
```

### 7. Run the Celery worker *(optional but recommended)*

```bash
celery -A workers.celery_worker worker --loglevel=info
```

### 8. Open in your browser

```
http://127.0.0.1:8000
```

<br>

## API Reference

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/register` | Create a new user account |
| `POST` | `/login` | Authenticate and receive JWT token |
| `GET` | `/me` | Get current user profile |

### Interview

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/start-interview` | Create a new interview session |
| `GET` | `/generate-questions/{session_id}` | Generate questions for a session |
| `POST` | `/evaluate-answer` | Submit an answer for AI evaluation |

<br>

## How It Works

```
1. User selects role & difficulty level
2. Backend creates an interview session
3. AI generates a contextual question
4. User submits their answer
5. AI evaluates the response
6. System returns score + feedback
7. Repeat until session complete
```

<br>

## Scalability

- **Stateless API** — horizontally scalable by design
- **Redis caching** — reduces redundant LLM calls
- **Celery workers** — offloads async AI tasks, scales independently
- **Modular architecture** — swap SQLite → PostgreSQL, Groq → OpenAI with minimal changes

<br>

## Deployment

Deploys cleanly on **Render**, **Railway**, or **AWS/GCP**.

### Render

| Setting | Value |
|---|---|
| **Build command** | `pip install -r requirements.txt` |
| **Start command** | `uvicorn app.main:app --host 0.0.0.0 --port 10000` |
| **Environment variable** | `GROQ_API_KEY = your_key` |

> Note: Add a Redis instance (Render or Upstash) and set `REDIS_URL` if using Celery in production.

<br>

## Roadmap

- [ ] 🎤 Voice-based interview mode
- [ ] 📊 Performance analytics dashboard across sessions
- [ ] 📄 Resume-based question generation
- [ ] 🧠 Adaptive follow-up questioning based on previous answers
- [ ] 🌍 Multi-language support

<br>

## Author

**Ammu S** — B.Tech Computer Science Engineering

<br>

## License

Built for educational and portfolio purposes.

---

*If this helped you prep for interviews — star the repo, fork it, or pass it on.*
