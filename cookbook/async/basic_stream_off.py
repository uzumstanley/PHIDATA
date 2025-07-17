import asyncio
from phi.agent import Agent
from phi.model.openai import OpenAIChat

assistant = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
)
# -*- Print a response to the cli
asyncio.run(assistant.aprint_response("Share a breakfast recipe.", markdown=True, stream=False))
