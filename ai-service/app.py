from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class LogEntry(BaseModel):
    timestamp: str
    service: str
    level: str
    message: str


class IncidentRequest(BaseModel):
    incidentId: str
    logs: List[LogEntry]


@app.post("/analyze")
def analyze(request: IncidentRequest):

    root_cause = "Unknown issue"
    confidence = 40

    for log in request.logs:

        message = log.message.lower()

        if "database" in message or "timeout" in message:

            root_cause = "Database connection issue"
            confidence = 92

        elif "memory" in message or "heap" in message:

            root_cause = "Memory issue"
            confidence = 88

    recommendations = []

    if "Database" in root_cause:

        recommendations = [
            "Increase DB connection pool",
            "Optimize SQL queries",
            "Enable autoscaling"
        ]

    elif "Memory" in root_cause:

        recommendations = [
            "Check heap dumps",
            "Optimize memory usage",
            "Increase JVM heap"
        ]

    else:

        recommendations = [
            "Manual investigation required"
        ]

    return {
        "incidentId": request.incidentId,
        "rootCause": root_cause,
        "confidence": confidence,
        "recommendations": recommendations
    }