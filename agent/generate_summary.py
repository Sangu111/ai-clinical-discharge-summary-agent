import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)


def generate_discharge_summary(patient_data):

    prompt = f"""
You are an expert clinical discharge-summary generator.

Using the structured patient information below,
generate a professional discharge summary.

Patient Data:

{json.dumps(patient_data, indent=2)}

Output format:

# DISCHARGE SUMMARY

## Patient Demographics

## Primary Diagnosis

## Secondary Diagnoses

## Hospital Course

## Procedures

## Medications at Discharge

## Follow-up Instructions

## Pending Results

## Discharge Condition

## Clinician Review Flags

Important Rules:
- Do not hallucinate.
- Mention missing information clearly.
- Use professional medical language.
- Mention medication conflicts if present.
- Mention missing demographics if absent.
- Generate a complete clinician-ready summary.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("\nGemini API Error:")
        print(str(e))

        return f"""
# DISCHARGE SUMMARY

## Patient Demographics
Information not available.

## Primary Diagnosis
{chr(10).join(['- ' + d for d in patient_data.get('primary_diagnosis', [])])}

## Secondary Diagnoses
{chr(10).join(['- ' + d for d in patient_data.get('secondary_diagnosis', [])])}

## Procedures
{chr(10).join(['- ' + p for p in patient_data.get('procedures', [])])}

## Medications at Discharge
{chr(10).join(['- ' + m for m in patient_data.get('medications', [])])}

## Hospital Course
Automatically generated fallback summary because Gemini service was unavailable.

## Follow-up Instructions
Clinician review required.

## Pending Results
Not provided.

## Discharge Condition
Stable.

## Clinician Review Flags
Gemini API unavailable during execution.
"""