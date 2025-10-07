from prompts import get_architect_prompt
from utils.llm import get_llm
from models import TaskPlan
from langchain.schema import SystemMessage, HumanMessage


def architect_agent(user_query):
    llm = get_llm()
    structured_llm = llm.with_structured_output(TaskPlan)
    system_prompt = get_architect_prompt()
    messages = [
        SystemMessage(content = system_prompt),
        HumanMessage(content=user_query)
    ]
    res = structured_llm.invoke(messages)
    return res



    


