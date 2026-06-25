import re


def extract_projects(text):

    projects = []

    # Section dhundo — "Projects" heading ke baad
    match = re.search(
        r'(?:PROJECTS?|PROJECT EXPERIENCE)(.*?)(?:EDUCATION|EXPERIENCE|SKILLS|CERTIFICATIONS|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return projects

    section = match.group(1)

    # Har line check karo — bold/title-case headings project names hoti hain
    for line in section.split("\n"):
        line = line.strip()

        if not line:
            continue

        # Skip karo bullet points aur short lines
        if line.startswith(("•", "-", "–", "*")):
            continue

        # Project name: Title Case ya ALL CAPS, kam se kam 2 words
        if re.match(r'^[A-Z][A-Za-z0-9\s&/\-]{5,60}$', line):
            projects.append(line)

    return projects[:5]  # Max 5 projects return karo