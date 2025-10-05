from utils.llm import get_llm
from prompts.planner import get_planner_prompt
from models import Plan
from langchain.schema import SystemMessage, HumanMessage



def planner_agent(user_query):
    llm = get_llm()

    structured_llm = llm.with_structured_output(Plan)
    system_prompt = get_planner_prompt()
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_query)
    ]
    res = structured_llm.invoke(messages)
    return res

