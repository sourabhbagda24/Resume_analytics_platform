# test_name.py — ye file banao aur run karo
from pdf_parser import extract_text

pdfs = [
    "output/Akash_Nagar_ML_Engineer_Resume.pdf",
    "output/Mahipal_Singh_Rajpurohit_Resume.pdf",
    "output/Gaurav_Gocher.pdf",
    "output/yash_jain (1).pdf",
    "output/Resume_2_Priya_Verma.pdf",
]

for pdf in pdfs:
    print(f"\n===== {pdf} =====")
    text = extract_text(pdf)
    print(repr(text[:300]))  # pehle 300 characters dikhao