"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent, RunResponse  # noqa
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=Ollama(id="llama3.1:8b"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)

# Get the response in a variable
# run: RunResponse = agent.run("What is the stock price of NVDA and TSLA")
# print(run.content)

# Print the response in the terminal
agent.print_response("What is the stock price of NVDA and TSLA")
