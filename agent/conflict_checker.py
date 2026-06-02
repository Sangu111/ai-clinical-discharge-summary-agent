def check_conflicts(data):
    conflicts = []

    meds = data.get("medications", [])

    med_text = " ".join(meds).lower()

    if "ondem" in med_text and "emeset" in med_text:
        conflicts.append(
            "Duplicate Ondansetron medications detected"
        )

    if "rabeprazole" in med_text and "pantoprazole" in med_text:
        conflicts.append(
            "Multiple Proton Pump Inhibitors detected"
        )

    if not data.get("patient_name"):
        conflicts.append(
            "Missing patient name"
        )

    if not data.get("age"):
        conflicts.append(
            "Missing age"
        )

    if not data.get("gender"):
        conflicts.append(
            "Missing gender"
        )

    return conflicts