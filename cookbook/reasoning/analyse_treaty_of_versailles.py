from phi.agent import Agent
from phi.model.openai import OpenAIChat

task = (
    "Analyze the key factors that led to the signing of the Treaty of Versailles in 1919. "
    "Discuss the political, economic, and social impacts of the treaty on Germany and how it "
    "contributed to the onset of World War II. Provide a nuanced assessment that includes "
    "multiple historical perspectives."
)

reasoning_agent = Agent(model=OpenAIChat(id="gpt-4o"), reasoning=True, markdown=True, structured_outputs=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
