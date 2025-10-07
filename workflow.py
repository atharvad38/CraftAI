from langgraph.graph import StateGraph

from models import state
#imports agents
from agents.planner import planner_agent
from agents.architect import architect_agent

user_prompt = "build a simple ai based calculator"
def planner_node(state:state)->state:
    state.plan = planner_agent(state.user_prompt)
    print(state.plan)
    return state

def architect_node(state:state)->state:
    query = state.plan
    state.architect_plan = architect_agent(query)
    print(state.architect_plan)
    return state

graph = StateGraph(state)
graph.add_node('planner',planner_node)
graph.set_entry_point('planner')
agent = graph.compile()
result = agent.invoke({'user_prompt':user_prompt})
print(result)

    
    
    