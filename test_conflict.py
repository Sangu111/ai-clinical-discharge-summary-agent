import json
from agent.conflict_checker import check_conflicts

with open("structured_patient.json", "r") as f:
    data = json.load(f)

conflicts = check_conflicts(data)

print("Conflicts Found:")
print(conflicts)