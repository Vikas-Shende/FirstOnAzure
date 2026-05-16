from langgraph.graph import StateGraph

from agents.log_agent import log_agent
from agents.metric_agent import metric_agent
from agents.rca_agent import rca_agent
from agents.summary_agent import summary_agent

workflow = StateGraph(dict)

workflow.add_node("log_agent", log_agent)
workflow.add_node("metric_agent", metric_agent)
workflow.add_node("rca_agent", rca_agent)
workflow.add_node("summary_agent", summary_agent)

workflow.set_entry_point("log_agent")

workflow.add_edge("log_agent", "metric_agent")
workflow.add_edge("metric_agent", "rca_agent")
workflow.add_edge("rca_agent", "summary_agent")

workflow.set_finish_point("summary_agent")

app_graph = workflow.compile()