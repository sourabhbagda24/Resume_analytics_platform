import pandas as pd

from config import FOLDER_ID
from drive_manager import download_files
from pdf_parser import extract_text
from resume_parser import parse_resume


def main():

    print("=" * 50)
    print("Resume Analytics Platform Started")
    print("=" * 50)
    print("Folder ID:", FOLDER_ID)

    try:
        pdf_files = download_files(FOLDER_ID)
        print("\nPDF Files Found:")
        print(pdf_files)
        print("Total Files:", len(pdf_files))

    except Exception as e:
        print("Drive Error:", e)
        return

    data = []

    for pdf in pdf_files:
        try:
            print(f"\nProcessing: {pdf}")
            text = extract_text(pdf)
            row = parse_resume(text)
            print("Extracted:", row)
            data.append(row)

        except Exception as e:
            print(f"Error processing {pdf}: {e}")

    print("\nTotal Records Extracted:", len(data))

    df = pd.DataFrame(data)

    cols = [
        "Name", "Email", "Phone",
        "Graduation", "Post Graduation",
        "Experience", "Experience Level",
        "Skills", "Projects"
    ]
    df = df.reindex(columns=cols)

    print("\nDataFrame Preview:")
    print(df.head())

    if not df.empty:
        df.to_csv("resume_output.csv", index=False)
        print("\nCSV Exported Successfully -> resume_output.csv")
    else:
        print("\nNo data found. CSV not created.")


if __name__ == "__main__":
    main()