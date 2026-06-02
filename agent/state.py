from dataclasses import dataclass, field

@dataclass
class AgentState:
    patient_name: str = ""
    age: str = ""
    gender: str = ""

    diagnoses: list = field(default_factory=list)
    medications: list = field(default_factory=list)
    procedures: list = field(default_factory=list)
    allergies: list = field(default_factory=list)

    conflicts: list = field(default_factory=list)
    pending_results: list = field(default_factory=list)

    trace_logs: list = field(default_factory=list)