import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

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

Important:
- Do not hallucinate.
- Mention missing information.
- Use professional medical language.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text