from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.models.user import User
from app.db.deps import get_db
from app.core.security import hash_password , verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)

    db_user = User(email=user.email, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User registered successfully"}

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(form_data.password, db_user.password):
        return {"error": "Invalid password"}

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

from app.core.auth import get_current_user

@router.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {"email": current_user}

from app.schemas.interview import InterviewCreate
from app.models.interview import InterviewSession

@router.post("/start-interview")
def start_interview(
    data: InterviewCreate,
    db: Session = Depends(get_db),
    
):
    # find user
    user = db.query(User).first()

    session = InterviewSession(
        user_id=user.id,
        role=data.role,
        level=data.level
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "message": "Interview started",
        "session_id": session.id
    }

from app.services.question_service import generate_questions

@router.get("/generate-questions/{session_id}")
def get_questions(
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.query(InterviewSession).filter(
        InterviewSession.id == session_id
    ).first()

    if not session:
        return {"error": "Session not found"}

    questions = generate_questions(session.role, session.level)

    return {
        "session_id": session_id,
        "questions": questions
    }
from app.services.evaluation_service import evaluate_answer


from pydantic import BaseModel

class AnswerRequest(BaseModel):
    question: str
    answer: str

@router.post("/evaluate-answer")
def evaluate(data: AnswerRequest):
    result = evaluate_answer(data.question, data.answer)
    return {"result": result}