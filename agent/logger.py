def log_step(state, reasoning, action, result):

    state.trace_logs.append({
        "reasoning": reasoning,
        "action": action,
        "result": result
    })