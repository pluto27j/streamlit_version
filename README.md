# CareerGPT - AI-Based Career Roadmap Builder (Streamlit Edition)

A 100% pure Python web application built using **Streamlit**, converted from the original HTML/CSS/JavaScript project.

---

## 🌟 Key Features Preserved & Enhanced

1. **Authentication & User Management**:
   - SQLite database (`database/career_roadmap.db`) for persistent user state.
   - Secure PBKDF2-HMAC-SHA256 password hashing with 100,000 iterations and per-user salt.
   - 4-step interactive onboarding wizard (Account, Background, Career Goal, Confirmation).
   - Demo credentials seeded: `admin@career.ai` / `Password@123`.

2. **Home Dashboard**:
   - Real-time profile metrics (Profile completion, Skills tracked, Milestones completed, Job match score).
   - Dynamic progress bars across all 6 core career propulsion tools.
   - Live activity feed logged automatically in SQLite.
   - The 4-Phase Rocket Propulsion framework (Ignition, Navigation, Acceleration, Orbit).

3. **Explore 25 High-Demand Tech Careers**:
   - 25 complete career profiles with icons, high-res images, and tags.
   - Multi-attribute search and filtering by Category, Salary Bracket, and Market Demand.
   - Estimated Indian CTC packages clearly labeled for Junior, Mid, Senior, and Lead levels.

4. **Career Details Deep-Dive**:
   - 4-phase structured learning curricula with weekly duration estimates.
   - Curated free and paid learning resources with verified URLs.
   - Portfolio-grade projects with difficulty tags and actionable milestones.
   - Indian tech market salary tier breakdowns.

5. **AI Career Roadmap Generator**:
   - Staged sequentially unlocked milestones checklist.
   - Real-time Job Readiness Percentage calculation based on completed items.
   - One-click SQLite roadmap persistence.
   - One-click plain text roadmap export (`.txt`).

6. **Skill Gap Analysis Engine**:
   - Interactive sliders (0–100%) to assess proficiency against industry standards.
   - Visual deficiency tracking with real-time gap scoring.
   - Prioritized remedial action plan for high-impact gaps.

7. **Resume Analyzer & ATS Match Scanner**:
   - Supports both PDF and plain text file uploads, or direct text pasting.
   - Comprehensive ATS match score calculation against target role competencies.
   - Highlights matched skills, missing keywords, and actionable optimization tips.

8. **ATS Resume Templates**:
   - 5 recruiter-approved templates across major tech domains.
   - In-app markdown preview with instant `.md` download.

9. **Interview Preparation Simulator**:
   - Domain question banks categorized into Technical, Case Studies, and Behavioral.
   - Interactive question cards with Previous/Next controls and coaching hints.

10. **My Saved Roadmaps**:
    - Centralized view of all saved roadmaps for the logged-in user.
    - Persistent milestone checklist sync with SQLite.
    - Instant roadmap deletion or reopening in the generator.

---

## 🚀 How to Run the Application

Navigate to this directory and run:

```bash
cd d:\ai_based_roadmap\streamlit_version
python -m streamlit run app.py
```

Open your browser to `http://localhost:8501`.

---

## 🧪 Automated Test Suite

To run the complete automated test suite validating all 8 modules:

```bash
python d:\ai_based_roadmap\streamlit_version\test_app.py
```
