SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Power BI",
    "Tableau",
    "Excel",
    "Pandas",
    "NumPy",
    "Scikit-Learn",
    "TensorFlow",
    "PyTorch",
    "AWS",
    "Snowflake",
    "Flask",
    "Django",
    "n8n",
    "Zapier",
    "MySQL",
    "Git",
]


def extract_skills(text):

    found = []
    text_lower = text.lower()

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found.append(skill)

    return found