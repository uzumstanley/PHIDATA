from typing import Iterator
from rich.pretty import pprint
from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat
from phi.tools.dalle import Dalle

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[Dalle()],
    description="You are an AI agent that can create images using DALL-E.",
    instructions=[
        "When the user asks you to create an image, use the DALL-E tool to create an image.",
        "The DALL-E tool will return an image URL.",
        "Return the image URL in your response in the following format: `![image description](image URL)`",
    ],
    markdown=True,
)

run_stream: Iterator[RunResponse] = image_agent.run(
    "Create an image of a yellow siamese cat",
    stream=True,
    stream_intermediate_steps=True,
)
for chunk in run_stream:
    pprint(chunk.model_dump(exclude={"messages"}))
    print("---" * 20)
