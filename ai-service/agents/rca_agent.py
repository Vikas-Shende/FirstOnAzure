from typing import Dict


def rca_agent(state: Dict):

    log_findings = state.get("log_findings", [])
    metric_findings = state.get("metric_findings", [])

    all_findings = log_findings + metric_findings

    if "Connection pool exhaustion" in all_findings:

        state["root_cause"] = "Database connection pool exhausted"
        state["confidence"] = 94

    elif "High memory usage" in all_findings:

        state["root_cause"] = "Memory leak detected"
        state["confidence"] = 89

    else:

        state["root_cause"] = "Unknown issue"
        state["confidence"] = 40

    return state