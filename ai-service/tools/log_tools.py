from langchain.tools import tool

@tool
def search_logs(query: str):

    return f"Relevant logs found for: {query}"