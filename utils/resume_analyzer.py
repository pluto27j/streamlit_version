"""
Pure Python ATS Resume Analyzer.
Extracts text from PDF/TXT documents, computes keyword density against career competency profiles,
and generates structured ATS match scores and prioritized recommendations.
"""

import re
import io
from typing import BinaryIO
import pypdf

def extract_text_from_file(file_obj: BinaryIO, filename: str) -> str:
    """Extracts plain text from an uploaded PDF or TXT file."""
    if not file_obj:
        return ""
    
    filename_lower = filename.lower()
    text = ""
    
    if filename_lower.endswith(".pdf"):
        try:
            reader = pypdf.PdfReader(file_obj)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        except Exception as e:
            text = f"Error reading PDF file: {str(e)}"
    else:
        try:
            content = file_obj.read()
            if isinstance(content, bytes):
                text = content.decode("utf-8", errors="ignore")
            else:
                text = str(content)
        except Exception as e:
            text = f"Error reading text file: {str(e)}"
            
    return text.strip()

def analyze_resume(resume_text: str, career_name: str, career_profile: dict) -> dict:
    """
    Performs comprehensive ATS keyword and competency matching on resume text
    against the target career profile.
    """
    if not resume_text or len(resume_text.strip()) < 50:
        return {
            "valid": False,
            "error": "The resume text is too short or empty. Please upload a valid resume with at least 50 characters."
        }

    lower_text = resume_text.lower()

    # 1. Contact Information Verification
    has_email = bool(re.search(r"[\w\.-]+@[\w\.-]+\.\w+", resume_text))
    has_phone = bool(re.search(r"(\+?\d{1,3}[-.\s]?)?(\d{5}[-.\s]?\d{5}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\b\d{10}\b)", resume_text))
    has_linkedin = "linkedin.com" in lower_text or "github.com" in lower_text

    # 2. Extract Career Benchmark Skills & Keyword Terms
    core_skills = [s["name"] for s in career_profile.get("skills", [])]
    project_tech = []
    for p in career_profile.get("projects", []):
        project_tech.extend(p.get("tech", []))
    phase_tags = []
    for ph in career_profile.get("phases", []):
        phase_tags.extend(ph.get("tags", []))

    all_supplementary = list(dict.fromkeys(project_tech + phase_tags))

    matched_core = []
    missing_core = []

    for sk in core_skills:
        clean_term = re.sub(r"\(.*?\)", "", sk).strip().lower()
        sub_tokens = [t.strip() for t in clean_term.split("/") if len(t.strip()) > 1]
        if not sub_tokens:
            sub_tokens = [clean_term]

        is_match = any(re.search(r"\b" + re.escape(tok) + r"\b", lower_text) or tok in lower_text for tok in sub_tokens)
        if is_match:
            matched_core.append(sk)
        else:
            missing_core.append(sk)

    matched_supp = []
    for term in all_supplementary:
        clean_term = term.strip().lower()
        if re.search(r"\b" + re.escape(clean_term) + r"\b", lower_text) or clean_term in lower_text:
            matched_supp.append(term)

    all_matched = list(dict.fromkeys(matched_core + matched_supp))
    all_missing = list(dict.fromkeys(missing_core + [t for t in all_supplementary if t not in matched_supp]))

    # 3. Calculate Realistic ATS Score
    core_ratio = len(matched_core) / max(1, len(core_skills))
    core_score = int(core_ratio * 45)

    supp_ratio = len(matched_supp) / max(1, min(10, len(all_supplementary)))
    supp_score = int(min(1.0, supp_ratio) * 25)

    word_count = len(resume_text.split())
    if word_count >= 200:
        length_score = 15
    elif word_count >= 100:
        length_score = 12
    elif word_count >= 50:
        length_score = 8
    else:
        length_score = 4

    contact_score = (5 if has_email else 0) + (5 if has_phone else 0) + (5 if has_linkedin else 0)

    total_ats_score = min(98, max(20, core_score + supp_score + length_score + contact_score))

    # 4. Actionable Recommendations
    recommendations = []
    if missing_core:
        top_missing = missing_core[:3]
        recommendations.append(f"Add bullet points showcasing core missing competencies: {', '.join(top_missing)}.")
    
    if not has_linkedin:
        recommendations.append("Include links to your public LinkedIn and GitHub profiles in your header contact section.")
    
    if word_count < 250:
        recommendations.append("Your resume is relatively concise. Aim for 350–700 words highlighting quantifiable outcomes (e.g. 'boosted query speed by 40%').")

    if not any(k in lower_text for k in ["project", "projects", "experience", "work"]):
        recommendations.append("Use standard uppercase section headers like 'EXPERIENCE' and 'PROJECTS' for accurate ATS parsing.")

    recommendations.append(f"Align your professional headline or summary specifically with '{career_name}'.")

    return {
        "valid": True,
        "score": total_ats_score,
        "word_count": word_count,
        "has_email": has_email,
        "has_phone": has_phone,
        "has_linkedin": has_linkedin,
        "matched_count": len(all_matched),
        "total_benchmark_count": len(core_skills) + len(all_supplementary),
        "matched_skills": all_matched[:12],
        "missing_skills": all_missing[:8],
        "recommendations": recommendations
    }
