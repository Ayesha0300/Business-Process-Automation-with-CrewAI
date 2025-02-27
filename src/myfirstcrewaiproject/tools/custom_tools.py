from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

def get_search_tool():
    search = GoogleSearchAPIWrapper()
    
    return Tool(
        name="Search",
        func=search.run,
        description="Useful for searching information on the internet."
    )