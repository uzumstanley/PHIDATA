from mem0 import MemoryClient
from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat
from phi.utils.pprint import pprint_run_response

client = MemoryClient()

user_id = "phi"
messages = [
    {"role": "user", "content": "My name is John Billings."},
    {"role": "user", "content": "I live in NYC."},
    {"role": "user", "content": "I'm going to a concert tomorrow."},
]
# Comment out the following line after running the script once
client.add(messages, user_id=user_id)

agent = Agent(model=OpenAIChat(), context={"memory": client.get_all(user_id=user_id)}, add_context=True)
run: RunResponse = agent.run("What do you know about me?")

pprint_run_response(run)

messages = [{"role": i.role, "content": str(i.content)} for i in (run.messages or [])]
client.add(messages, user_id=user_id)
