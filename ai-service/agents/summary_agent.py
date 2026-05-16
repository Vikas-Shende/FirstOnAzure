from typing import Dict
def summary_agent(state: Dict):

    root_cause = state.get("root_cause")

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

    state["recommendations"] = recommendations

    return state