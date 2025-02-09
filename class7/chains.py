from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI


SYSTEM_PROMPT = """
<PERSONA>
Eres un asistente de contact center
</PERSONA>

<TASK>
Tu tarea es refrasear la solicitud del usuario para genera una solicitud refraseada.

- Puedes corregir los errores gramaticales
- Puedes mejorar la semántica y orden léxico de la palabras para un mejor entendimiento
</TASK>
"""

USER_PROMPT = """{user_request}"""

prompt_template = ChatPromptTemplate([
    SystemMessage(content=SYSTEM_PROMPT),
    ("user", USER_PROMPT)
])

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
)


chain = prompt_template | llm | RunnableLambda(lambda x: x.content)