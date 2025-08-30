from typing import Iterator  # noqa
from phi.agent import Agent, RunResponse  # noqa
from phi.model.together import Together

agent = Agent(model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"), markdown=True)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
