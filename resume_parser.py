from ner_extractor import extract_name, extract_email, extract_phone
from skill_extractor import extract_skills
from education_extractor import extract_graduation, extract_post_graduation
from experience_extractor import extract_experience, extract_experience_years
from project_extractor import extract_projects


def parse_resume(text):
    return {
        "Name":             extract_name(text),
        "Email":            extract_email(text),
        "Phone":            extract_phone(text),
        "Graduation":       extract_graduation(text),
        "Post Graduation":  extract_post_graduation(text),
        "Experience":       extract_experience(text),
        "Experience Level": extract_experience_years(text),
        "Skills":           ", ".join(extract_skills(text)),
        "Projects":         ", ".join(extract_projects(text)),
    }