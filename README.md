# AI-Powered Clinical Discharge Summary Agent

## Overview
This project was developed as part of the Dscribe AI Engineer take-home assignment.

The goal is to transform unstructured clinical source notes into a structured discharge summary while maintaining safety, transparency, and clinician oversight.

The system processes scanned PDF medical records using OCR, extracts relevant clinical information using Gemini, validates the extracted data, identifies potential issues requiring review, and generates a clinician-friendly discharge summary.

---

# Problem Statement
Clinical records are often stored as scanned documents containing fragmented information spread across multiple pages.

Manually reviewing these documents is time-consuming and prone to omission.

This project automates:

- OCR extraction
- Clinical information extraction
- Medication review
- Validation checks
- Escalation of missing information
- Discharge summary generation

while ensuring that uncertain information is explicitly flagged for clinician review.

---

# System Architecture
PDF Clinical Notes
↓
OCR Layer (Tesseract OCR + PyMuPDF)
↓
Text Extraction
↓
Clinical Information Extraction Agent (Gemini)
↓
Structured JSON Representation
↓
Validation Layer
↓
Medication Reconciliation Layer
↓
Clinician Escalation Layer
↓
Discharge Summary Generator
↓
Output Files

---

# Design Philosophy
The primary design goal was safety.

The system follows three principles:

1. Never invent patient information.
2. Clearly identify missing information.
3. Escalate uncertain cases for clinician review.

Whenever information cannot be confidently extracted, the system records:

"Information Not Provided"

instead of generating assumptions.

---

# Project Workflow

## Step 1: OCR Processing
The source PDF is processed using:

- PyMuPDF
- Tesseract OCR

This converts scanned pages into machine-readable text.

Output:

`output_patient2.txt`

---

## Step 2: Clinical Information Extraction
Gemini is used to extract:

- Patient demographics
- Diagnoses
- Medications
- Procedures
- Clinical findings

The extracted information is stored in structured JSON format.

Output:

`structured_patient.json`

---

## Step 3: Validation Layer
The validation component checks for:

- Missing patient name
- Missing age
- Missing gender
- Missing admission date
- Missing discharge date
- Missing diagnoses
- Missing medications

Detected issues are recorded for clinician review.

---

## Step 4: Medication Reconciliation
The medication review layer identifies:

- Duplicate medications
- Duplicate drug classes
- Missing medication details
- Potential conflicts

Example identified in the provided patient data:

- Ondansetron listed twice
- Multiple proton pump inhibitors listed

These findings are escalated for review.

---

## Step 5: Clinician Escalation
Certain situations automatically trigger clinician review:

- Missing demographics
- Missing encounter dates
- Medication ambiguities
- Incomplete discharge instructions

Output:

`clinician_review_flags.txt`

---

## Step 6: Discharge Summary Generation
Gemini generates a structured discharge summary containing:

- Patient demographics
- Diagnoses
- Procedures
- Hospital course
- Medications
- Follow-up instructions
- Pending results
- Clinician review flags

Output:

`discharge_summary.txt`

---

# Project Structure
`AI Engineer/`

`agent/` — Clinical workflow modules

`data/` — Input patient PDF files

`Output/`

- `discharge_summary.txt` — Final generated discharge summary
- `extracted_data.json` — Structured clinical data
- `trace.json` — Execution trace
- `clinician_review_flags.txt` — Issues requiring clinician review

- `main.py` — Application entry point
- `extract_structured.py` — Clinical data extraction
- `run_summary.py` — Discharge summary generation
- `ocr_test.py` — OCR verification utility
- `test_pdf.py` — PDF extraction utility
- `test_gemini.py` — Gemini connectivity test
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation

---

# Output Files

## `discharge_summary.txt`
Contains the final clinician-facing discharge summary.

---

## `extracted_data.json`
Structured representation of extracted clinical information.

---

## `trace.json`
Execution trace showing:

- OCR completion
- Extraction status
- Validation status
- Medication review status
- Summary generation status

---

## `clinician_review_flags.txt`
Contains issues that require human review before discharge sign-off.

---

# Safety Features
This project includes several safety mechanisms:

- Missing data detection
- Medication reconciliation
- Escalation rules
- Explicit uncertainty reporting
- Clinician review flags

The system avoids fabricating clinical information.

---

# Limitations
Current limitations include:

- OCR quality depends on source document quality.
- Medication interaction checking is rule-based.
- Some clinical context may require manual review.
- Demographics cannot be recovered if absent from source notes.

---

# Future Improvements
Given additional development time, I would implement:

1. Multi-patient batch processing
2. Source-level citation and provenance tracking
3. Retrieval-Augmented Generation (RAG)
4. Drug interaction checking
5. Confidence scoring
6. Human-in-the-loop approval workflow
7. FHIR-compatible output generation

---

# Technologies Used

- Python
- Gemini 2.5 Flash
- Tesseract OCR
- PyMuPDF
- JSON

---

# Running the Project
Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Outputs will be generated inside the `Output` folder.

---

# Conclusion
This project demonstrates an agentic workflow for converting unstructured clinical records into structured discharge summaries while prioritizing safety, transparency, and clinician oversight.

The system intentionally favors escalation and uncertainty reporting over unsupported assumptions, making it more suitable for healthcare-oriented workflows.
