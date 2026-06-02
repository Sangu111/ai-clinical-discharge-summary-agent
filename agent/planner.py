from agent.state import AgentState
from agent.logger import log_step

def run_agent():

    state = AgentState()

    log_step(
        state,
        "Need patient information",
        "OCR extraction",
        "Completed"
    )

    return state