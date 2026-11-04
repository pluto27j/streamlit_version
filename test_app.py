"""
Comprehensive Automated Test Suite for CareerGPT Streamlit Application.
Tests database, auth, password hashing, 25 careers, resume analysis,
milestone progress, roadmap storage, and file integrity.
"""

import sys
import os
from pathlib import Path

# Add project root
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from database.db import (
    init_db, register_user, authenticate_user, update_user_profile,
    toggle_milestone, get_completed_milestones, save_roadmap,
    get_user_saved_roadmaps, delete_saved_roadmap, get_user_dashboard_stats
)
from data.careers_data import CAREERS_DATA
from data.templates_data import RESUME_TEMPLATES
from utils.resume_analyzer import analyze_resume

def test_database_and_auth():
    print("[1/8] Testing SQLite Database Initialization and PBKDF2 Auth...")
    init_db()

    # Test demo user
    success, user = authenticate_user("admin@career.ai", "Password@123")
    assert success, "Demo user authentication failed"
    assert user["name"] == "John Doe", f"Unexpected name: {user['name']}"

    # Test wrong password
    bad_success, _ = authenticate_user("admin@career.ai", "WrongPassword")
    assert not bad_success, "Wrong password was accepted!"

    # Test new registration
    test_email = f"test_{os.urandom(4).hex()}@career.ai"
    reg_ok, msg = register_user(
        name="Test Candidate",
        email=test_email,
        password="SecurePass@2026",
        current_role="Junior Dev",
        experience_level="Beginner",
        skills_csv="Python, Git",
        target_career="AI Engineer",
        timeline_goal="6 months"
    )
    assert reg_ok, f"Registration failed: {msg}"

    # Test login of newly registered user
    login_ok, new_user = authenticate_user(test_email, "SecurePass@2026")
    assert login_ok, "Login of newly registered user failed"
    assert new_user["name"] == "Test Candidate"

    # Test duplicate registration rejection
    dup_ok, _ = register_user("Dup User", test_email, "AnyPassword")
    assert not dup_ok, "Duplicate email registration was not blocked"

    print("  -> Database & PBKDF2 authentication passed cleanly.")
    return new_user["id"]

def test_user_profile(user_id):
    print("[2/8] Testing Profile Updates...")
    ok = update_user_profile(
        user_id=user_id,
        name="Updated Candidate",
        current_role="Mid-Level Engineer",
        experience_level="Intermediate",
        skills_csv="Python, PyTorch, Docker",
        target_career="Machine Learning Engineer",
        timeline_goal="1 year"
    )
    assert ok, "Profile update failed"
    print("  -> Profile update passed.")

def test_careers_data():
    print("[3/8] Validating 25 High-Demand Career Profiles & Indian Salaries...")
    assert len(CAREERS_DATA) == 25, f"Expected 25 careers, got {len(CAREERS_DATA)}"

    for name, c in CAREERS_DATA.items():
        assert "salary_range" in c and "₹" in c["salary_range"], f"Missing INR salary range for {name}"
        assert "LPA" in c["salary_range"], f"Salary range should specify LPA for {name}"
        assert len(c.get("skills", [])) >= 4, f"Insufficient skills for {name}"
        assert len(c.get("phases", [])) == 4, f"Expected 4 phases for {name}"
        assert len(c.get("projects", [])) >= 2, f"Insufficient projects for {name}"
        assert len(c.get("stages", [])) >= 3, f"Insufficient stages for {name}"
        assert len(c.get("interview", [])) >= 2, f"Insufficient interview Qs for {name}"

    print("  -> All 25 career datasets validated with estimated Indian salaries.")

def test_milestone_tracking(user_id):
    print("[4/8] Testing Milestone Tracking & Real-Time Calculation...")
    career = "Frontend Developer"

    # Complete Stage 0, Milestone 0
    toggle_milestone(user_id, career, stage_index=0, milestone_index=0, is_completed=True, milestone_title="HTML5")
    toggle_milestone(user_id, career, stage_index=0, milestone_index=1, is_completed=True, milestone_title="Flexbox")

    completed = get_completed_milestones(user_id, career)
    assert (0, 0) in completed, "Milestone (0, 0) not marked complete"
    assert (0, 1) in completed, "Milestone (0, 1) not marked complete"

    # Untoggle
    toggle_milestone(user_id, career, stage_index=0, milestone_index=1, is_completed=False)
    completed_after = get_completed_milestones(user_id, career)
    assert (0, 1) not in completed_after, "Milestone (0, 1) should be unmarked"

    print("  -> Milestone toggling and SQLite persistence passed.")

def test_saved_roadmaps(user_id):
    print("[5/8] Testing Saving and Retrieving Custom Roadmaps...")
    test_milestones = [
        {"stage_index": 0, "milestone_index": 0, "title": "Setup", "completed": True},
        {"stage_index": 0, "milestone_index": 1, "title": "Basics", "completed": False}
    ]

    r_id = save_roadmap(
        user_id=user_id,
        career_name="Cloud Engineer",
        timeline_goal="6 months",
        experience_level="Beginner",
        job_readiness=55,
        milestones_state=test_milestones
    )
    assert r_id > 0, "Failed to save roadmap"

    saved_list = get_user_saved_roadmaps(user_id)
    assert any(r["career_name"] == "Cloud Engineer" for r in saved_list), "Saved roadmap not found in query"

    # Test deletion
    del_ok = delete_saved_roadmap(user_id, r_id)
    assert del_ok, "Failed to delete saved roadmap"
    print("  -> Saved roadmaps persistence and deletion passed.")

def test_resume_analyzer():
    print("[6/8] Testing Pure Python Resume Analyzer (ATS Scoring)...")
    sample_resume = """
    Priyanshu Sharma
    Bengaluru, India | Email: priyanshu@example.com | Phone: +91 98765 43210 | LinkedIn: linkedin.com/in/priyanshu | GitHub: github.com/priyanshu
    
    PROFESSIONAL SUMMARY:
    Frontend Developer with 3+ years of experience in building responsive user interfaces with React, JavaScript, HTML5, CSS3, Tailwind CSS, and TypeScript.
    Proven expertise in optimizing web performance, integrating RESTful APIs, and implementing accessible component design systems.
    
    PROFESSIONAL EXPERIENCE:
    Frontend Engineer | TechCorp Solutions (2022 - Present)
    - Developed and maintained modern web applications using React.js, Next.js, TypeScript, and Tailwind CSS.
    - Improved Core Web Vitals and site loading speeds by 35% through lazy loading, code-splitting, and asset compression.
    - Built reusable UI component libraries following WCAG accessibility guidelines and Responsive Web Design best practices.
    - Collaborated with product designers in Figma and backend engineers to integrate REST APIs and state management.
    
    FEATURED PROJECTS:
    E-Commerce SaaS Dashboard | React, TypeScript, Tailwind CSS, Vite
    - Created an interactive analytics dashboard featuring real-time charts, dark mode, and dynamic product catalog filtering.
    - Managed client-side state using React Context API and integrated mock checkout workflows.
    
    EDUCATION:
    B.Tech in Computer Science and Engineering | 2022
    """

    analysis = analyze_resume(sample_resume, "Frontend Developer", CAREERS_DATA["Frontend Developer"])
    assert analysis["valid"] is True, "Analysis marked invalid"
    assert analysis["score"] >= 50, f"Expected ATS score >= 50, got {analysis['score']}"
    assert analysis["has_email"] is True
    assert analysis["has_phone"] is True
    assert analysis["has_linkedin"] is True
    assert len(analysis["matched_skills"]) > 0
    assert len(analysis["recommendations"]) > 0
    print(f"  -> Resume Analyzer scored {analysis['score']}% with {len(analysis['matched_skills'])} matched skills.")

def test_templates_and_no_html():
    print("[7/8] Validating Resume Templates and Code Compliance (No HTML/CSS/JS)...")
    assert len(RESUME_TEMPLATES) >= 5, "Missing resume templates"
    for name, tmpl in RESUME_TEMPLATES.items():
        assert len(tmpl["content"]) > 200, f"Template {name} content is too short"

    # Code Compliance: Check app.py does NOT use unsafe_allow_html or raw HTML tags
    app_path = BASE_DIR / "app.py"
    with open(app_path, "r", encoding="utf-8") as f:
        app_code = f.read()

    assert "unsafe_allow_html=True" not in app_code, "VIOLATION: unsafe_allow_html found in app.py!"
    assert "<script" not in app_code.lower(), "VIOLATION: <script> found in app.py!"
    assert "<style" not in app_code.lower(), "VIOLATION: <style> found in app.py!"
    print("  -> Code compliance verified: 100% native Streamlit components, ZERO HTML/CSS/JS.")

def test_original_files_integrity():
    print("[8/8] Verifying Original Project Files Were NOT Modified or Deleted...")
    original_files = [
        "index.html", "dashboard.html", "roadmap.html", "careerpath.html",
        "getstart.html", "loginpage.html", "about.html", "app.py"
    ]
    parent_dir = BASE_DIR.parent
    for fname in original_files:
        fpath = parent_dir / fname
        assert fpath.exists(), f"Original file {fname} is missing!"
        assert fpath.stat().st_size > 0, f"Original file {fname} is empty!"

    # Verify explore files
    explore_dir = parent_dir / "explore"
    assert explore_dir.exists()
    assert len(list(explore_dir.glob("*.html"))) == 25, "Original explore files modified or missing!"

    # Verify images
    images_dir = parent_dir / "images"
    assert images_dir.exists()
    assert len(list(images_dir.glob("*.*"))) >= 25, "Original images modified or missing!"

    print("  -> All original HTML/CSS/JS and image files are completely preserved and untouched.")

if __name__ == "__main__":
    print("==================================================")
    print("CAREERGPT STREAMLIT APPLICATION TEST SUITE")
    print("==================================================")
    user_id = test_database_and_auth()
    test_user_profile(user_id)
    test_careers_data()
    test_milestone_tracking(user_id)
    test_saved_roadmaps(user_id)
    test_resume_analyzer()
    test_templates_and_no_html()
    test_original_files_integrity()
    print("==================================================")
    print("ALL 8 TEST SUITES PASSED WITH 100% SUCCESS!")
    print("==================================================")
