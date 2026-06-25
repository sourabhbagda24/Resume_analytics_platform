import re


def extract_experience(text):

    experiences = []

    # Experience section dhundo
    match = re.search(
        r'(?:EXPERIENCE|WORK EXPERIENCE|PROFESSIONAL EXPERIENCE|INTERNSHIP|EMPLOYMENT)(.*?)'
        r'(?:EDUCATION|PROJECTS|SKILLS|CERTIFICATIONS|ACHIEVEMENTS|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return "Not Found"

    section = match.group(1).strip()

    # Har line check karo
    for line in section.split("\n"):

        line = line.strip()

        if not line:
            continue

        # Skip bullets
        if line.startswith(("•", "-", "–", "*")):
            continue

        # Skip bahut choti lines
        if len(line) < 5:
            continue

        # Job title + company line: Title Case ya ALL CAPS, pipe/comma/at se company alag
        if re.match(r'^[A-Z][A-Za-z\s,&.\-|@]{5,80}$', line):
            experiences.append(line)

    # Max 3 entries return karo
    return " | ".join(experiences[:3]) if experiences else "Not Found"


def extract_experience_years(text):
    """
    Total kitne saal ka experience hai wo nikalo
    e.g. "2 years", "6 months", "1.5 years"
    """

    # Pattern: "X years of experience" ya "X+ years"
    patterns = [
        r'(\d+\.?\d*)\+?\s*years?\s*of\s*(?:work\s*)?experience',
        r'(\d+\.?\d*)\+?\s*years?\s*experience',
        r'experience\s*of\s*(\d+\.?\d*)\+?\s*years?',
        r'(\d+)\s*months?\s*of\s*(?:work\s*)?experience',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group().strip()

    return "Fresher"