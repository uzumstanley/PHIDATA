from phi.agent import Agent
from phi.tools.email import EmailTools

receiver_email = "<receiver_email>"
sender_email = "<sender_email>"
sender_name = "<sender_name>"
sender_passkey = "<sender_passkey>"

agent = Agent(
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
        )
    ]
)
agent.print_response("send an email to <receiver_email>")
