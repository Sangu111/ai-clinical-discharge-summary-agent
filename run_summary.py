import json

from agent.generate_summary import (
    generate_discharge_summary
)

with open(
    "structured_patient.json",
    "r",
    encoding="utf-8"
) as f:
    patient_data = json.load(f)

summary = generate_discharge_summary(
    patient_data
)

print(summary)

with open(
    "summary.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(summary)

print("\nSaved to summary.txt")