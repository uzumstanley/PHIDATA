from phi.agent import Agent
from phi.tools.baidusearch import BaiduSearch

agent = Agent(
    tools=[BaiduSearch()],
    description="You are a search agent that helps users find the most relevant information using Baidu.",
    instructions=[
        "Given a topic by the user, respond with the 3 most relevant search results about that topic.",
        "Search for 5 results and select the top 3 unique items.",
        "Search in both English and Chinese.",
    ],
    show_tool_calls=True,
)
agent.print_response("What are the latest advancements in AI?", markdown=True)
