from utils.llm import get_llm
from prompts.planner import get_planner_prompt
from models import Plan
from langchain.schema import SystemMessage, HumanMessage

llm = get_llm()


structured_llm = llm.with_structured_output(Plan)

# Prepare messages
system_prompt = get_planner_prompt()
messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content="Build a to-do list application")
]

# Invoke the model
res = structured_llm.invoke(messages)

# Print only the content as JSON
print(res)