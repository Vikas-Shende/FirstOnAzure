from typing import Dict


def metric_agent(state: Dict):

    findings = []

    metrics = state.get("metrics", {})

    cpu = metrics.get("cpu", 0)
    memory = metrics.get("memory", 0)

    if cpu > 90:
        findings.append("High CPU usage")

    if memory > 90:
        findings.append("High memory usage")

    state["metric_findings"] = findings

    return state