from phi.agent import Agent
from phi.model.openai import OpenAIChat

task = "Give me steps to write a python script for fibonacci series"

reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
