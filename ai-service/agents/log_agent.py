from typing import Dict


def log_agent(state: Dict):

    logs = state["logs"]

    findings = []

    for log in logs:

        message = log.get("message", "")

        if "timeout" in message.lower():
            findings.append("Database timeout detected")

        if "pool exhausted" in message.lower():
            findings.append("Connection pool exhaustion")

        if "memory" in message.lower():
            findings.append("Memory issue detected")

    state["log_findings"] = findings

    return state