import random
from langchain_core.tools import tool
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI

@tool
def get_email_by_name(name: str) -> float:
    """Returns the email of a person"""
    return f"{name.lower()}@idat.pe"

@tool
def send_email(email: str, content: str) -> str:
    """Send an email with a content"""
    return f"email sent succesfully to {email}, the content of the message was: {content}"

@tool
def get_weather(location: str) -> float:
    """get weather of a city"""
    return random.randint(20, 30)

tools = [get_email_by_name, send_email, get_weather]

prompt = hub.pull("hwchase17/openai-tools-agent")

llm = ChatOpenAI(model="gpt-4o")
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)