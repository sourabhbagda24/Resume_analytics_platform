import re
import spacy

nlp = spacy.load("en_core_web_sm")


# ── Name ─────────────────────────────────────────────────────────
def extract_name(text):

    BLACKLIST = {
        "email", "phone", "skills", "education", "experience",
        "project", "projects", "summary", "profile", "objective",
        "professional summary", "career objective", "technical skills",
        "work experience", "internship", "certifications", "resume",
        "contact", "address", "linkedin", "github", "declaration",
    }

    lines = text.split("\n")

    for line in lines[:5]:

        line = line.strip()

        if not line:
            continue

        if line.lower() in BLACKLIST:
            continue

        # Skip karo agar @ ya numbers hain (email/phone/link)
        if re.search(r'[@0-9/|]', line):
            continue

        # Skip karo agar bahut lamba hai
        if len(line) > 50:
            continue

        words = line.split()

        # Kam se kam 2 words hone chahiye
        if len(words) < 2:
            continue

        # ALL CAPS — "AKASH NAGAR", "MAHIPAL SINGH RAJPUROHIT"
        if re.match(r'^[A-Z][A-Z\s]+$', line):
            return line.title()

        # Title Case — "Priya Verma"
        if re.match(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+)+$', line):
            return line

    return "Not Found"


# ── Email ─────────────────────────────────────────────────────────
def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


# ── Phone ─────────────────────────────────────────────────────────
def extract_phone(text):

    pattern = r'(?:\+91[\s\-]?)?[6-9]\d{9}'
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


# ── Organization ─────────────────────────────────────────────────
def extract_organizations(text):

    doc = nlp(text)
    orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return list(set(orgs))


# ── Location ─────────────────────────────────────────────────────
def extract_locations(text):

    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
    return list(set(locations))