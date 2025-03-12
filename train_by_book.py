import pdfplumber
import re
from transformers import pipeline

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Replace 'jeff1ps.pdf' with the path to your PDF file
pdf_path = "wonderland-story.pdf"
text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a file
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text extracted and saved to 'extracted_text.txt'")

def clean_text(text):
    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters (optional)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()

# Load the extracted text
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    extracted_text = f.read()

# Clean the text
cleaned_text = clean_text(extracted_text)

# Save the cleaned text
with open("cleaned_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Text cleaned and saved to 'cleaned_text.txt'")



# Load a pre-trained question-answering model
qa_pipeline = pipeline("question-answering")

# Define a question and context (cleaned text)
question = "What realization did Jack come to during the tea party?"
context = cleaned_text  # Use the cleaned text from the PDF

# Get the answer
answer = qa_pipeline(question=question, context=context)
print("Answer:", answer['answer'])



