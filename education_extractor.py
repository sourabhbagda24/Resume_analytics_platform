import re


# ── Degree patterns ───────────────────────────────────────────────
GRADUATION = [
    "Bachelor of Technology", "Bachelor of Engineering",
    "Bachelor of Computer Applications", "Bachelor of Science",
    "Bachelor of Commerce", "Bachelor of Arts", "Bachelor of Business Administration",
    "B.Tech", "B.E", "BCA", "B.Sc", "B.Com", "B.A", "BBA", "BE",
]

POST_GRADUATION = [
    "Master of Technology", "Master of Engineering",
    "Master of Computer Applications", "Master of Science",
    "Master of Business Administration", "Master of Commerce",
    "Master of Arts",
    "M.Tech", "M.E", "MCA", "M.Sc", "MBA", "M.Com", "M.A", "ME",
    "Ph.D", "PhD", "Doctorate",
]


# ── Helper: degree line extract karo ─────────────────────────────
def _find_degree_line(text, degree):
    pattern = re.compile(
        rf'{re.escape(degree)}[^\n]*',
        re.IGNORECASE
    )
    match = pattern.search(text)
    return match.group().strip() if match else degree


# ── Graduation ───────────────────────────────────────────────────
def extract_graduation(text):
    for degree in GRADUATION:
        if degree.lower() in text.lower():
            return _find_degree_line(text, degree)
    return "Not Found"


# ── Post Graduation ──────────────────────────────────────────────
def extract_post_graduation(text):
    for degree in POST_GRADUATION:
        if degree.lower() in text.lower():
            return _find_degree_line(text, degree)
    return "Not Found"


# ── Education (combined — purana function bhi kaam kare) ─────────
def extract_education(text):
    grad = extract_graduation(text)
    pg = extract_post_graduation(text)

    if grad != "Not Found" and pg != "Not Found":
        return f"{grad} | {pg}"
    elif grad != "Not Found":
        return grad
    elif pg != "Not Found":
        return pg
    return "Not Found"