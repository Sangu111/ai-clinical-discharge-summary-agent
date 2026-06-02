import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("output_patient2.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunk = text[:30000]

prompt = f"""
You are a clinical information extraction system.

Extract the following information from the medical record.

Return JSON only.

{{
  "patient_name":"",
  "age":"",
  "gender":"",
  "admission_date":"",
  "discharge_date":"",
  "primary_diagnosis":[],
  "secondary_diagnosis":[],
  "allergies":[],
  "medications":[],
  "procedures":[]
}}

Medical Record:

{chunk}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)