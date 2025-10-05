from langgraph.graph import StateGraph

from models import state
#imports agents
from agents.planner import planner_agent


user_prompt = "build a simple ai based calculator"
def planner_node(state:state)->state:
    state['plan'] = planner_agent(state['user_prompt'])
    print(state['plan'])
    return state

graph = StateGraph(state)
graph.add_node('planner',planner_node)
graph.set_entry_point('planner')
agent = graph.compile()
result = agent.invoke({'user_prompt':user_prompt})
print(result)

    
    
    