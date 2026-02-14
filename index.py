from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Study Tracker API"}

@app.get("/sessions")
def get_sessions():
    sessions = [
        {"id": 1, "subject": "Info104", "duration_minutes": 90},
        {"id": 2, "subject": "Info110", "duration_minutes": 90},
    ]
    return sessions

@app.post("/sessions")
def create_sessions(subject: str, duration: int):
    return{"created": True}


