from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.cli.console import console

task = "9.11 and 9.9 -- which is bigger?"

regular_agent = Agent(model=OpenAIChat(id="gpt-4o"), markdown=True)
reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True)

console.rule("[bold green]Regular Agent[/bold green]")
regular_agent.print_response(task, stream=True)
console.rule("[bold yellow]Reasoning Agent[/bold yellow]")
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
