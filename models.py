#schema of all outputs
from pydantic import BaseModel,Field,ConfigDict
from typing import Optional



# workflow
class state(BaseModel):
    user_prompt: str
    plan:Optional[str] = None
    architect_plan:Optional[str] = None

#planner agent
# class plan(BaseModel):
#     name : str = Field(description='The name of application to be built')
#     description : str = Field(description='One line description of app to be built')
#     techstack : str = Field(description='Techstack of the application')
#     features : str = Field(description='All Features of the application')
#     files : str = Filed(description='A list of files to be created , each with a path and purpose')



class Plan(BaseModel):
    name: str = Field(description="The name of the application to be built (e.g., 'Smart Expense Tracker')")
    description: str = Field(description="One-line summary describing what the app does")
    objective: str = Field(description="Main goal or problem this application aims to solve")
    
    target_users: str = Field(description="Intended user group (e.g., students, developers, small businesses)")
    category: str = Field(description="App category (e.g., productivity, finance, AI tools, lifestyle, etc.)")
    value_proposition: str = Field(description="Why users would want to use this app over others")
    
    techstack: str = Field(description="Broad list of technologies likely to be used (frontend, backend, database, etc.)")
    features: str = Field(description=(
        "List of features with names and short descriptions. "
        "Example: '1. Goal Tracker: Track daily expenses and goals\n2. Reminder: Notify users of upcoming tasks'"
    ))
    
    ui_pages: str = Field(description="List of main UI pages or screens planned (e.g., 'Login', 'Dashboard', 'Settings')")
    user_flow: str = Field(description="Step-by-step overview of how a user interacts with the app")
    interactions: str = Field(description="How users interact with core features and navigate between sections")
    
    files: str = Field(description=(
        "List of files to be created, each with its relative path and purpose. "
        "Example: '1. src/components/Navbar.jsx: Top navigation bar of the app\n2. src/index.html: Root HTML file'"
    ))
    
    inspiration: str = Field(description="List of similar apps or inspirations to follow or improve upon")
    constraints: str = Field(description="Any design, ethical, or platform constraints (e.g., must be mobile-friendly, data privacy compliance)")


# architcture agent

class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified")
    task_description: str = Field(description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc.")
    
class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(description="A list of steps to be taken to implement the task")
    model_config = ConfigDict(extra="allow")  #the purpose of this is to allow extra elements