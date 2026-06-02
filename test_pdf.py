from agent.extractor import read_pdf

text = read_pdf("data/Patient 2.pdf")

with open(
    "output_patient2.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

print("OCR Complete")
print("Saved to output_patient2.txt")