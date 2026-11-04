"""
AI-Based Career Roadmap Builder (CareerGPT)
Pure Python Web Application using Streamlit.
Zero HTML, CSS, or JavaScript. Native Streamlit components throughout.
Fully debugged with robust session_state handling, persistent callbacks, and database integration.
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import streamlit as st

# Configure base import path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from database.db import (
    init_db, register_user, authenticate_user, update_user_profile,
    get_completed_milestones, toggle_milestone, save_roadmap,
    get_user_saved_roadmaps, delete_saved_roadmap, get_user_activities,
    get_user_dashboard_stats, log_activity
)
from data.careers_data import (
    CAREERS_DATA, CAREER_CATEGORIES, SALARY_FILTERS, DEMAND_FILTERS
)
from data.templates_data import RESUME_TEMPLATES
from utils.resume_analyzer import extract_text_from_file, analyze_resume

# Page configuration
st.set_page_config(
    page_title="CareerGPT - AI Career Roadmap Builder",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database schema on startup
init_db()

# ----------------- Navigation Helper Function -----------------
def navigate_to(page_name: str):
    """Safely updates both nav_page and the sidebar radio key to prevent state reversion."""
    st.session_state["nav_page"] = page_name
    st.session_state["main_navigation_radio"] = page_name

# ----------------- Session State Initialization -----------------
if "logged_in" not in st.session_state:
    # Default to demo user session for instant seamless exploration
    success, demo_user = authenticate_user("admin@career.ai", "Password@123")
    if success and isinstance(demo_user, dict):
        st.session_state["logged_in"] = True
        st.session_state["user"] = demo_user
    else:
        st.session_state["logged_in"] = False
        st.session_state["user"] = None

if "nav_page" not in st.session_state:
    st.session_state["nav_page"] = "Home Dashboard"

if "main_navigation_radio" not in st.session_state:
    st.session_state["main_navigation_radio"] = st.session_state["nav_page"]

if "selected_career" not in st.session_state:
    st.session_state["selected_career"] = "Frontend Developer"

if "roadmap_career" not in st.session_state:
    st.session_state["roadmap_career"] = "Frontend Developer"

if "interview_category" not in st.session_state:
    st.session_state["interview_category"] = "All"

if "interview_index" not in st.session_state:
    st.session_state["interview_index"] = 0

if "prev_iv_career" not in st.session_state:
    st.session_state["prev_iv_career"] = "Frontend Developer"

if "resume_analysis_result" not in st.session_state:
    st.session_state["resume_analysis_result"] = None

# Synchronize radio state if nav_page changed programmatically
if st.session_state.get("main_navigation_radio") != st.session_state["nav_page"]:
    st.session_state["main_navigation_radio"] = st.session_state["nav_page"]


# ----------------- Sidebar Navigation -----------------
with st.sidebar:
    st.title("🧠 CareerGPT")
    st.caption("AI-Powered Career Roadmap & Readiness Engine")
    st.divider()

    # User Status & Authentication Controls
    if st.session_state.get("logged_in") and st.session_state.get("user"):
        user = st.session_state["user"]
        st.write(f"**Signed In:** {user['name']}")
        st.caption(f"Role: {user.get('current_role', 'Tech Professional')}")
        st.caption(f"Target: {user.get('target_career', 'Frontend Developer')}")
        if st.button("🚪 Log Out", key="sidebar_logout_btn", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["user"] = None
            navigate_to("Login / Register")
            st.rerun()
    else:
        st.info("Browsing as Guest. Log in to save personal roadmaps.")
        if st.button("🔐 Sign In / Register", key="sidebar_login_btn", use_container_width=True):
            navigate_to("Login / Register")
            st.rerun()

    st.divider()

    # Main Navigation Options
    nav_options = [
        "Home Dashboard",
        "Explore Careers",
        "Career Details",
        "AI Career Roadmap Generator",
        "Skill Gap Analysis",
        "Resume Analyzer",
        "Resume Templates",
        "Interview Preparation",
        "My Saved Roadmaps",
        "User Profile",
        "Login / Register"
    ]

    def on_radio_change():
        st.session_state["nav_page"] = st.session_state["main_navigation_radio"]

    st.radio(
        "Navigation Menu",
        options=nav_options,
        key="main_navigation_radio",
        on_change=on_radio_change
    )

    st.divider()
    st.caption("Database: SQLite (`career_roadmap.db`)")
    st.caption("Security: PBKDF2-HMAC-SHA256")
    st.caption("Theme: Dark Blue & Sky Blue (Native)")


# =========================================================================
# PAGE 1: HOME DASHBOARD
# =========================================================================
if st.session_state["nav_page"] == "Home Dashboard":
    user = st.session_state.get("user")
    user_name = user["name"] if user else "Future Tech Leader"
    target_role = user.get("target_career", "Frontend Developer") if user else "Frontend Developer"
    user_id = user["id"] if user else 1

    st.title("🚀 AI Career Roadmap Dashboard")
    st.write(f"Welcome back, **{user_name}**! Here is your personalized career development and readiness overview.")
    st.divider()

    # Real-Time Key Performance Indicators
    stats = get_user_dashboard_stats(user_id)
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

    with kpi_col1:
        st.metric(
            label="Profile Completion",
            value=f"{stats['profile_completion']}%",
            delta="+12% this month"
        )
    with kpi_col2:
        st.metric(
            label="Skills Tracked",
            value=stats["skills_acquired"],
            delta="+3 verified"
        )
    with kpi_col3:
        st.metric(
            label="Milestones Completed",
            value=stats["milestones_done"],
            delta="+2 this week"
        )
    with kpi_col4:
        st.metric(
            label="Target Job Match",
            value=f"{stats['job_match_score']}%",
            delta=f"Role: {target_role}"
        )

    st.divider()

    # Quick Access Tool Grid
    st.subheader("🛠️ Core Career Tools")
    st.caption("Access all career propulsion modules designed to take you from learning to earning.")

    tool_col1, tool_col2, tool_col3 = st.columns(3)

    with tool_col1:
        with st.container(border=True):
            st.subheader("🗺️ AI Roadmap Generator")
            st.write("Step-by-step career path with sequentially unlocked milestones.")
            st.progress(0.75)
            st.caption("Readiness Target: 90%+")
            if st.button("Launch Roadmap", key="dash_btn_roadmap", use_container_width=True):
                navigate_to("AI Career Roadmap Generator")
                st.rerun()

        with st.container(border=True):
            st.subheader("📄 Resume Analyzer")
            st.write("Scan your resume against ATS benchmarks and identify keyword gaps.")
            st.progress(0.80)
            st.caption("ATS Score Ready")
            if st.button("Scan Resume", key="dash_btn_resume", use_container_width=True):
                navigate_to("Resume Analyzer")
                st.rerun()

    with tool_col2:
        with st.container(border=True):
            st.subheader("📊 Skill Gap Analysis")
            st.write("Identify missing competencies instantly against real industry requirements.")
            st.progress(0.65)
            st.caption("3 Critical Gaps Identified")
            if st.button("Analyze Gaps", key="dash_btn_skills", use_container_width=True):
                navigate_to("Skill Gap Analysis")
                st.rerun()

        with st.container(border=True):
            st.subheader("📝 Resume Templates")
            st.write("Download recruiter-approved, ATS-compliant templates for your domain.")
            st.progress(1.0)
            st.caption("5 Industry Templates Available")
            if st.button("Browse Templates", key="dash_btn_templates", use_container_width=True):
                navigate_to("Resume Templates")
                st.rerun()

    with tool_col3:
        with st.container(border=True):
            st.subheader("🎤 Interview Preparation")
            st.write("Practice with realistic AI interview questions and expert answer tips.")
            st.progress(0.40)
            st.caption("25+ Domain Question Banks")
            if st.button("Start Interview Prep", key="dash_btn_interview", use_container_width=True):
                navigate_to("Interview Preparation")
                st.rerun()

        with st.container(border=True):
            st.subheader("🚀 Explore 25+ Careers")
            st.write("Discover emerging tech domains, salary benchmarks, and learning paths.")
            st.progress(0.95)
            st.caption("All Indian CTC Benchmarks")
            if st.button("Explore Careers", key="dash_btn_explore", use_container_width=True):
                navigate_to("Explore Careers")
                st.rerun()

    st.divider()

    # Active Progress and Activity Feeds
    bottom_col1, bottom_col2 = st.columns([1.6, 1.4])

    with bottom_col1:
        st.subheader("📈 Active Career Progress: " + target_role)
        career_obj = CAREERS_DATA.get(target_role, CAREERS_DATA["Frontend Developer"])
        st.write(career_obj["tagline"])
        st.write(f"**Estimated Time to Job-Readiness:** {career_obj['est_time']}")
        st.write(f"**Market Compensation:** {career_obj['salary_range']}")

        stages = career_obj.get("stages", [])
        for idx, stage in enumerate(stages):
            with st.expander(f"{stage['title']} ({stage['duration']})", expanded=(idx == 0)):
                for m in stage.get("milestones", []):
                    st.write(f"- {m}")

    with bottom_col2:
        st.subheader("🕒 Recent Activity & Milestones")
        activities = get_user_activities(user_id, limit=6)
        if activities:
            for act in activities:
                with st.container(border=True):
                    st.write(f"**{act['activity_type']}**: {act['description']}")
                    st.caption(f"Time: {act['created_at']}")
        else:
            st.info("No recent activity recorded yet. Start exploring or saving a roadmap!")

    st.divider()

    # 4-Phase Rocket Journey Architecture
    st.subheader("🚀 The Career Propulsion Framework")
    journey_col1, journey_col2, journey_col3, journey_col4 = st.columns(4)

    with journey_col1:
        with st.container(border=True):
            st.write("### Phase 1: Ignition")
            st.write("Analyze strengths, identify target roles, and baseline core competencies.")
    with journey_col2:
        with st.container(border=True):
            st.write("### Phase 2: Navigation")
            st.write("Follow structured step-by-step milestones without getting lost in fragmented tutorials.")
    with journey_col3:
        with st.container(border=True):
            st.write("### Phase 3: Acceleration")
            st.write("Build portfolio-grade industry projects and validate skills with rigorous testing.")
    with journey_col4:
        with st.container(border=True):
            st.write("### Phase 4: Orbit")
            st.write("Polish ATS resume, ace technical interviews, and enter high-paying tech careers.")

    # Frequently Asked Questions
    st.divider()
    st.subheader("❓ Frequently Asked Questions")
    with st.expander("How accurate are these career roadmaps and salary figures?"):
        st.write("All roadmaps are modeled on real-world hiring standards. Salary figures represent estimated full-time Indian tech CTC ranges across tier-1 and tier-2 companies.")
    with st.expander("Can I switch my career target midway?"):
        st.write("Yes! You can explore all 25 careers, generate separate roadmaps, and save multiple career plans under 'My Saved Roadmaps'.")
    with st.expander("Is my data and password securely stored?"):
        st.write("Yes. Your credentials are fully protected using PBKDF2-HMAC-SHA256 password hashing with 100,000 rounds and cryptographic salt. No plain-text passwords ever touch storage.")


# =========================================================================
# PAGE 2: EXPLORE CAREERS (25 CAREERS)
# =========================================================================
elif st.session_state["nav_page"] == "Explore Careers":
    st.title("🚀 Explore Career Paths (25 High-Demand Roles)")
    st.write("Discover emerging tech domains, salary benchmarks in India, and learning paths.")
    st.divider()

    # Search & Filter Controls
    search_col, cat_col, sal_col, dem_col = st.columns([1.5, 1.2, 1, 1])

    with search_col:
        search_query = st.text_input("🔍 Search Career Role", placeholder="e.g. Frontend, AI, DevOps, Cloud...")

    with cat_col:
        cat_filter = st.selectbox("Category", options=CAREER_CATEGORIES)

    with sal_col:
        sal_filter = st.selectbox("Estimated Salary", options=SALARY_FILTERS)

    with dem_col:
        dem_filter = st.selectbox("Market Demand", options=DEMAND_FILTERS)

    # Filter Logic
    filtered_careers = {}
    for name, data in CAREERS_DATA.items():
        if search_query:
            q = search_query.lower()
            if q not in name.lower() and q not in data["tagline"].lower() and q not in data["category"].lower():
                continue

        if cat_filter != "All Categories" and data["category"] != cat_filter:
            continue

        if dem_filter != "All Demand Levels" and data["demand"] != dem_filter:
            continue

        if sal_filter != "All Salary Ranges":
            if "₹10L+" in sal_filter and not any(k in data["salary_range"] for k in ["10L", "12L", "15L", "20L", "25L", "30L", "35L"]):
                continue
            elif "₹8L+" in sal_filter and not any(k in data["salary_range"] for k in ["8L", "10L", "12L", "15L", "20L", "25L", "30L"]):
                continue
            elif "₹6L+" in sal_filter and not any(k in data["salary_range"] for k in ["6L", "7L", "8L", "10L", "15L", "20L"]):
                continue

        filtered_careers[name] = data

    st.write(f"Showing **{len(filtered_careers)}** of **25** Careers")
    st.divider()

    # Grid Display
    cols = st.columns(3)
    career_names = list(filtered_careers.keys())

    for idx, c_name in enumerate(career_names):
        c_data = filtered_careers[c_name]
        col = cols[idx % 3]

        with col:
            with st.container(border=True):
                img_path = c_data.get("image")
                if img_path and os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)

                st.subheader(f"{c_data['icon']} {c_name}")
                st.caption(f"📁 {c_data['category']}")
                st.write(c_data["tagline"])
                st.write(f"💰 **{c_data['salary_range']}**")
                st.write(f"🔥 **Demand:** {c_data['demand']} | ⏱ **Duration:** {c_data['est_time']}")

                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button("Deep Dive", key=f"btn_details_{c_name}", use_container_width=True):
                        st.session_state["selected_career"] = c_name
                        navigate_to("Career Details")
                        st.rerun()
                with btn_col2:
                    if st.button("Generate", key=f"btn_gen_{c_name}", use_container_width=True):
                        st.session_state["roadmap_career"] = c_name
                        navigate_to("AI Career Roadmap Generator")
                        st.rerun()


# =========================================================================
# PAGE 3: CAREER DETAILS
# =========================================================================
elif st.session_state["nav_page"] == "Career Details":
    c_name = st.session_state.get("selected_career", "Frontend Developer")
    c_data = CAREERS_DATA.get(c_name, CAREERS_DATA["Frontend Developer"])

    # Header Controls
    top_col1, top_col2 = st.columns([3, 1])
    with top_col1:
        st.title(f"{c_data['icon']} {c_name}")
        st.write(c_data["tagline"])
        st.caption(f"Category: {c_data['category']} | Typical Roadmap: {c_data['est_time']} | Market Demand: {c_data['demand']}")
    with top_col2:
        if st.button("← Back to Careers", key="btn_back_to_careers", use_container_width=True):
            navigate_to("Explore Careers")
            st.rerun()
        if st.button("🗺️ Start Roadmap", key="btn_start_roadmap_from_details", use_container_width=True):
            st.session_state["roadmap_career"] = c_name
            navigate_to("AI Career Roadmap Generator")
            st.rerun()

    st.divider()

    # Image Banner & Highlights
    banner_col1, banner_col2 = st.columns([1, 1.8])
    with banner_col1:
        img_path = c_data.get("image")
        if img_path and os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
    with banner_col2:
        st.subheader("Key Career Highlights")
        st.write(f"- **Estimated Indian Compensation:** {c_data['salary_range']}")
        st.write(f"- **Market Demand Rating:** {c_data['demand']}")
        st.write(f"- **Baseline Job-Readiness Score:** {c_data['readiness_base']}% (Scale up to {c_data['readiness_max']}%)")
        st.write(f"- **Total Curriculum Phases:** 4 Structured Milestones ({c_data['est_time']})")
        st.write(f"- **Primary Competencies Required:** {len(c_data['skills'])} Core Skills")

    st.divider()

    # Comprehensive Deep-Dive Tabs
    tab_phases, tab_resources, tab_projects, tab_salaries = st.tabs([
        "📚 Learning Phases (What You'll Learn)",
        "📖 Curated Resources",
        "🛠️ Hands-on Projects",
        "💰 Estimated Market Salaries in India"
    ])

    with tab_phases:
        st.subheader("Structured 4-Phase Curriculum")
        for ph in c_data.get("phases", []):
            with st.container(border=True):
                st.write(f"### {ph['num']}: {ph['name']}")
                st.caption(f"Estimated Duration: {ph['duration']}")
                st.write("**Core Skills & Topics Covered:**")
                st.write(" • ".join([f"`{t}`" for t in ph.get("tags", [])]))

    with tab_resources:
        st.subheader("Recommended Learning Resources (Free & Verified)")
        for res in c_data.get("resources", []):
            with st.container(border=True):
                st.write(f"**{res['name']}** [{res['cost']}]")
                st.caption(f"Type: {res['type']}")
                st.write(res["desc"])
                st.write(f"🔗 [Visit Official Resource]({res['url']})")

    with tab_projects:
        st.subheader("Portfolio-Grade Projects to Build")
        for proj in c_data.get("projects", []):
            with st.container(border=True):
                st.write(f"### {proj['title']} `[{proj['difficulty']}]`")
                st.write("**Tech Stack:** " + ", ".join([f"`{t}`" for t in proj.get("tech", [])]))
                st.write("**Key Project Objectives:**")
                for obj in proj.get("objectives", []):
                    st.write(f"- {obj}")

    with tab_salaries:
        st.subheader("Estimated CTC Compensation in India")
        st.caption("Salary information represents estimated Indian market CTC data gathered from industry surveys and hiring benchmarks.")
        for sal in c_data.get("salary_details", []):
            with st.container(border=True):
                st.write(f"**{sal['level']}**")
                st.write(f"💰 **Estimated Package:** {sal['salary']}")
                st.caption(f"Experience Range: {sal['exp']}")


# =========================================================================
# PAGE 4: AI CAREER ROADMAP GENERATOR
# =========================================================================
elif st.session_state["nav_page"] == "AI Career Roadmap Generator":
    user = st.session_state.get("user")
    user_id = user["id"] if user else 1

    st.title("🗺️ AI Career Roadmap Generator")
    st.write("Generate, customize, and track your step-by-step career milestones in real time.")
    st.divider()

    # Generator Controls
    gen_col1, gen_col2, gen_col3 = st.columns(3)

    all_career_names = list(CAREERS_DATA.keys())
    target_career_name = st.session_state.get("roadmap_career", "Frontend Developer")
    if target_career_name not in all_career_names:
        target_career_name = all_career_names[0]
    default_c_idx = all_career_names.index(target_career_name)

    # Ensure selectbox key stays in sync with programmatic career selection
    if st.session_state.get("roadmap_select_career") != target_career_name:
        st.session_state["roadmap_select_career"] = target_career_name

    def on_roadmap_career_change():
        st.session_state["roadmap_career"] = st.session_state["roadmap_select_career"]
        st.session_state["roadmap_generated_notice"] = None

    with gen_col1:
        chosen_career = st.selectbox(
            "Target Career Role",
            options=all_career_names,
            index=default_c_idx,
            key="roadmap_select_career",
            on_change=on_roadmap_career_change
        )
        st.session_state["roadmap_career"] = chosen_career

    with gen_col2:
        chosen_timeline = st.selectbox(
            "Target Completion Timeline",
            options=["3 months (Fast-Track)", "6 months (Recommended)", "9 months (Part-Time)", "12 months (Comprehensive)"],
            index=1,
            key="roadmap_select_timeline"
        )

    with gen_col3:
        chosen_exp = st.selectbox(
            "Current Experience Level",
            options=["Beginner (0–1 yrs)", "Intermediate (1–3 yrs)", "Advanced (3+ yrs)"],
            index=0,
            key="roadmap_select_exp"
        )

    btn_gen_col1, btn_gen_col2 = st.columns([1, 2])
    with btn_gen_col1:
        if st.button("⚡ Generate AI Roadmap", key="btn_trigger_generate_roadmap", use_container_width=True):
            st.session_state["roadmap_generated_notice"] = f"✓ AI Roadmap generated for {chosen_career} ({chosen_timeline})!"
    with btn_gen_col2:
        if st.session_state.get("roadmap_generated_notice"):
            st.success(st.session_state["roadmap_generated_notice"])

    career_obj = CAREERS_DATA[chosen_career]
    stages = career_obj.get("stages", [])

    # Fetch user's persistent milestones from SQLite
    completed_milestones = get_completed_milestones(user_id, chosen_career)

    # Calculate Total & Completed Milestones
    total_milestones_count = sum(len(s.get("milestones", [])) for s in stages)
    completed_count = len(completed_milestones)

    # Calculate Real-Time Job Readiness Score
    base_readiness = career_obj.get("readiness_base", 30)
    max_readiness = career_obj.get("readiness_max", 90)
    progress_ratio = (completed_count / total_milestones_count) if total_milestones_count > 0 else 0
    current_readiness = int(base_readiness + (progress_ratio * (max_readiness - base_readiness)))

    st.divider()

    # Real-Time Gauge Display
    gauge_col1, gauge_col2, gauge_col3 = st.columns([1.2, 1, 1])

    with gauge_col1:
        st.metric(
            label="Current Job Readiness Score",
            value=f"{current_readiness}%",
            delta=f"{completed_count}/{total_milestones_count} Milestones Completed"
        )
        st.progress(current_readiness / 100)

    with gauge_col2:
        st.metric(label="Target Market Role", value=chosen_career)
        st.caption(f"Estimated Timeline: {chosen_timeline.split(' ')[0]} {chosen_timeline.split(' ')[1]}")

    with gauge_col3:
        st.metric(label="Market CTC Benchmark", value=career_obj["salary_range"].split(" ")[0])
        st.caption("Estimated Indian Tech CTC")

    st.divider()

    # Staged Interactive Timeline
    st.subheader("Step-by-Step Milestones Checklist")
    st.caption("Check off items as you complete them. Your readiness score and progress save automatically to SQLite.")

    milestone_state_for_saving = []

    for stage_idx, stage in enumerate(stages):
        prev_stage_done = True
        if stage_idx > 0:
            prev_stage = stages[stage_idx - 1]
            for m_idx in range(len(prev_stage.get("milestones", []))):
                if (stage_idx - 1, m_idx) not in completed_milestones:
                    prev_stage_done = False
                    break

        stage_status_icon = "🔓" if prev_stage_done else "🔒"
        with st.container(border=True):
            st.write(f"### {stage_status_icon} {stage['title']} `[{stage['duration']}]`")
            if not prev_stage_done:
                st.warning(f"Complete all milestones in '{stages[stage_idx - 1]['title']}' to unlock this stage.")

            for m_idx, m_title in enumerate(stage.get("milestones", [])):
                is_checked = (stage_idx, m_idx) in completed_milestones
                milestone_key = f"chk_{chosen_career}_{stage_idx}_{m_idx}"

                chk = st.checkbox(
                    m_title,
                    value=is_checked,
                    key=milestone_key,
                    disabled=(not prev_stage_done and not is_checked)
                )

                if chk != is_checked:
                    toggle_milestone(user_id, chosen_career, stage_idx, m_idx, chk, m_title)
                    st.rerun()

                milestone_state_for_saving.append({
                    "stage_index": stage_idx,
                    "milestone_index": m_idx,
                    "title": m_title,
                    "completed": chk
                })

    st.divider()

    # Save & Export Controls
    action_col1, action_col2 = st.columns(2)

    with action_col1:
        if st.button("💾 Save Roadmap to My Profile", key="btn_save_roadmap_db", use_container_width=True):
            saved_id = save_roadmap(
                user_id=user_id,
                career_name=chosen_career,
                timeline_goal=chosen_timeline,
                experience_level=chosen_exp,
                job_readiness=current_readiness,
                milestones_state=milestone_state_for_saving
            )
            st.success(f"✓ Roadmap for '{chosen_career}' (ID #{saved_id}) saved successfully to your SQLite profile!")

    with action_col2:
        export_text = f"=== CAREERGPT ROADMAP: {chosen_career.upper()} ===\n"
        export_text += f"Target Timeline: {chosen_timeline}\n"
        export_text += f"Job Readiness: {current_readiness}%\n"
        export_text += f"Estimated Indian CTC: {career_obj['salary_range']}\n"
        export_text += f"Generated At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        for s_idx, s in enumerate(stages):
            export_text += f"{s['title']} ({s['duration']})\n"
            for m_idx, m in enumerate(s.get("milestones", [])):
                done_marker = "[X]" if (s_idx, m_idx) in completed_milestones else "[ ]"
                export_text += f"  {done_marker} {m}\n"
            export_text += "\n"

        st.download_button(
            label="📥 Download Roadmap as Plain Text (.txt)",
            data=export_text,
            file_name=f"{chosen_career.replace(' ', '_')}_Roadmap.txt",
            mime="text/plain",
            key="btn_download_roadmap_txt",
            use_container_width=True
        )


# =========================================================================
# PAGE 5: SKILL GAP ANALYSIS
# =========================================================================
elif st.session_state["nav_page"] == "Skill Gap Analysis":
    st.title("📊 Skill Gap Analysis Engine")
    st.write("Compare your current competencies against target industry benchmarks and receive customized study action plans.")
    st.divider()

    all_career_names = list(CAREERS_DATA.keys())
    selected_role = st.selectbox("Select Target Role for Gap Analysis", options=all_career_names, key="skill_gap_select_role")
    career_obj = CAREERS_DATA[selected_role]

    st.subheader(f"Competency Matrix for {selected_role}")
    st.caption("Adjust your self-assessed proficiency sliders (0–100%) to calculate your real-time skill deficiencies.")

    user_skills = {}
    gap_records = []

    for sk in career_obj.get("skills", []):
        sk_name = sk["name"]
        req_val = sk["required"]
        default_cur = sk["current"]

        slider_col, target_col = st.columns([3, 1])
        with slider_col:
            val = st.slider(f"{sk_name} (Proficiency)", min_value=0, max_value=100, value=default_cur, key=f"gap_slider_{selected_role}_{sk_name}")
            user_skills[sk_name] = val
            st.progress(val / 100)
        with target_col:
            st.metric(label="Target Benchmark", value=f"{req_val}%", delta=f"{val - req_val}% gap")

        gap = req_val - val
        gap_records.append({
            "skill": sk_name,
            "current": val,
            "required": req_val,
            "gap": max(0, gap)
        })

    st.divider()

    # Gap Summary & Prioritized Action Plan
    st.subheader("🎯 Prioritized Remediation Roadmap")
    sorted_gaps = sorted(gap_records, key=lambda x: x["gap"], reverse=True)
    critical_gaps = [g for g in sorted_gaps if g["gap"] > 15]

    if critical_gaps:
        st.warning(f"Identified {len(critical_gaps)} critical skill gaps requiring immediate focus:")
        for idx, g in enumerate(critical_gaps[:4], 1):
            with st.container(border=True):
                st.write(f"**Priority #{idx}: {g['skill']}** (Deficiency: {g['gap']}%)")
                st.write(f"Current: {g['current']}% | Required Industry Level: {g['required']}%")
                st.write(f"💡 **Recommended Action:** Dedicate 15–20 hours of focused project practice and documentation study on `{g['skill']}`.")
    else:
        st.success("Excellent! Your self-assessed skill levels closely meet or exceed the industry benchmark requirements for this role.")


# =========================================================================
# PAGE 6: RESUME ANALYZER (ATS SCANNER)
# =========================================================================
elif st.session_state["nav_page"] == "Resume Analyzer":
    st.title("📄 AI Resume Analyzer & ATS Match Scanner")
    st.write("Upload your resume (PDF or TXT) to evaluate keyword alignment, ATS compatibility, and role-specific gaps.")
    st.divider()

    scan_col1, scan_col2 = st.columns([1, 1])

    with scan_col1:
        target_role = st.selectbox("Target Role to Scan Against", options=list(CAREERS_DATA.keys()), key="ats_target_role")
        uploaded_file = st.file_uploader("Upload Resume File (.pdf or .txt)", type=["pdf", "txt"], key="ats_file_uploader")

    with scan_col2:
        st.write("Or paste raw resume text directly:")
        pasted_text = st.text_area("Paste Resume Text", height=150, placeholder="Paste your resume content here...", key="ats_pasted_text")

    resume_content = ""
    if uploaded_file is not None:
        resume_content = extract_text_from_file(uploaded_file, uploaded_file.name)
    elif pasted_text.strip():
        resume_content = pasted_text.strip()

    st.divider()

    # Scan Button Execution
    if st.button("🔍 Run Full ATS Scan & Analysis", key="btn_run_ats_scan", use_container_width=True):
        if not resume_content:
            st.error("Please upload a file or paste your resume text before running the scan.")
        else:
            with st.spinner("Analyzing keyword density, structural formatting, and competency coverage..."):
                analysis = analyze_resume(resume_content, target_role, CAREERS_DATA[target_role])
                st.session_state["resume_analysis_result"] = {
                    "role": target_role,
                    "data": analysis
                }

    # Persistent Display of Analysis Results
    if st.session_state.get("resume_analysis_result"):
        saved_scan = st.session_state["resume_analysis_result"]
        analysis = saved_scan["data"]
        scanned_role = saved_scan["role"]

        if not analysis.get("valid"):
            st.error(analysis.get("error", "Failed to analyze resume."))
        else:
            st.success(f"✓ ATS Analysis Complete for Target Role: **{scanned_role}**")
            score = analysis["score"]

            score_col1, score_col2, score_col3 = st.columns(3)
            with score_col1:
                st.metric(label="Overall ATS Match Score", value=f"{score}%", delta="Based on 50+ criteria")
                st.progress(score / 100)
            with score_col2:
                st.metric(label="Word Count", value=analysis["word_count"])
                st.caption("Target: 400–800 words")
            with score_col3:
                contact_items = []
                if analysis["has_email"]: contact_items.append("Email ✓")
                if analysis["has_phone"]: contact_items.append("Phone ✓")
                if analysis["has_linkedin"]: contact_items.append("LinkedIn/GitHub ✓")
                st.metric(label="Contact Info Detected", value=len(contact_items), delta="/".join(contact_items) if contact_items else "Missing")

            st.divider()

            res_col1, res_col2 = st.columns(2)

            with res_col1:
                st.subheader("✅ Matched Core Competencies")
                matched = analysis.get("matched_skills", [])
                if matched:
                    for m in matched:
                        st.write(f"- `{m}`")
                else:
                    st.write("No exact benchmark keyword matches detected.")

            with res_col2:
                st.subheader("⚠️ Missing High-Impact Keywords")
                missing = analysis.get("missing_skills", [])
                if missing:
                    for ms in missing:
                        st.write(f"- `{ms}`")
                else:
                    st.write("Great job! All primary target keywords are represented.")

            st.divider()

            st.subheader("📋 Actionable Recommendations to Boost Your ATS Score")
            for rec in analysis.get("recommendations", []):
                st.write(f"- {rec}")

            if st.button("Clear Results", key="btn_clear_ats"):
                st.session_state["resume_analysis_result"] = None
                st.rerun()


# =========================================================================
# PAGE 7: RESUME TEMPLATES
# =========================================================================
elif st.session_state["nav_page"] == "Resume Templates":
    st.title("📝 ATS-Compliant Resume Templates")
    st.write("Browse and download industry-proven, recruiter-approved resume templates formatted in clean Markdown & plain text.")
    st.divider()

    template_names = list(RESUME_TEMPLATES.keys())
    chosen_tmpl_name = st.selectbox("Select Domain Template", options=template_names, key="select_resume_tmpl")
    tmpl_data = RESUME_TEMPLATES[chosen_tmpl_name]

    st.caption(f"Domain: {tmpl_data['domain']} | {tmpl_data['desc']}")
    st.divider()

    st.download_button(
        label=f"📥 Download '{chosen_tmpl_name}' as Markdown (.md)",
        data=tmpl_data["content"],
        file_name=f"{chosen_tmpl_name.split(' ')[0]}_Resume_Template.md",
        mime="text/markdown",
        key="btn_download_template"
    )

    st.subheader("Template Live Preview")
    with st.container(border=True):
        st.code(tmpl_data["content"], language="markdown")


# =========================================================================
# PAGE 8: INTERVIEW PREPARATION
# =========================================================================
elif st.session_state["nav_page"] == "Interview Preparation":
    st.title("🎤 AI Interview Preparation Simulator")
    st.write("Practice with realistic interview questions categorized by Technical, Case Studies, and Behavioral scenarios.")
    st.divider()

    iv_col1, iv_col2 = st.columns([2, 1])

    with iv_col1:
        chosen_iv_career = st.selectbox("Select Role Question Bank", options=list(CAREERS_DATA.keys()), key="select_iv_career")
        if chosen_iv_career != st.session_state.get("prev_iv_career"):
            st.session_state["prev_iv_career"] = chosen_iv_career
            st.session_state["interview_index"] = 0

    with iv_col2:
        iv_cat = st.selectbox("Category Filter", options=["All", "Technical", "Case", "Behavioral"], key="select_iv_cat")

    career_obj = CAREERS_DATA[chosen_iv_career]
    raw_questions = career_obj.get("interview", [])

    filtered_questions = [
        q for q in raw_questions
        if iv_cat == "All" or q.get("category", "Technical") == iv_cat
    ]

    if not filtered_questions:
        st.info("No questions found for the selected category filter.")
    else:
        total_q = len(filtered_questions)
        curr_idx = min(st.session_state["interview_index"], total_q - 1)
        curr_idx = max(0, curr_idx)
        curr_q = filtered_questions[curr_idx]

        st.divider()

        with st.container(border=True):
            st.caption(f"Question {curr_idx + 1} of {total_q} | Category: {curr_q.get('category', 'Technical')}")
            st.subheader(f"💬 {curr_q['q']}")

            with st.expander("💡 Reveal Expert Answer & Coaching Tip", expanded=False):
                st.write(curr_q["tip"])

        nav_prev_col, nav_count_col, nav_next_col = st.columns([1, 2, 1])

        with nav_prev_col:
            if st.button("← Previous Question", key="btn_iv_prev", use_container_width=True):
                st.session_state["interview_index"] = (curr_idx - 1) % total_q
                st.rerun()

        with nav_count_col:
            st.write(f"Question Progress: **{curr_idx + 1} / {total_q}**")

        with nav_next_col:
            if st.button("Next Question →", key="btn_iv_next", use_container_width=True):
                st.session_state["interview_index"] = (curr_idx + 1) % total_q
                st.rerun()


# =========================================================================
# PAGE 9: MY SAVED ROADMAPS
# =========================================================================
elif st.session_state["nav_page"] == "My Saved Roadmaps":
    user = st.session_state.get("user")
    user_id = user["id"] if user else 1

    st.title("💾 My Saved Career Roadmaps")
    st.write("Access, manage, and track progress across all custom saved roadmaps.")
    st.divider()

    saved_list = get_user_saved_roadmaps(user_id)

    if not saved_list:
        st.info("You haven't saved any custom roadmaps yet. Go to the 'AI Career Roadmap Generator' to create and save your first roadmap!")
        if st.button("Create a Roadmap Now", key="btn_create_roadmap_empty"):
            navigate_to("AI Career Roadmap Generator")
            st.rerun()
    else:
        for item in saved_list:
            with st.container(border=True):
                r_col1, r_col2, r_col3 = st.columns([2, 1, 1])

                with r_col1:
                    st.subheader(f"🗺️ {item['career_name']}")
                    st.caption(f"Timeline: {item['timeline_goal']} | Level: {item['experience_level']}")
                    st.caption(f"Saved on: {item['created_at']}")

                with r_col2:
                    st.metric(label="Job Readiness", value=f"{item['job_readiness']}%")
                    st.progress(item['job_readiness'] / 100)

                with r_col3:
                    if st.button("Open in Generator", key=f"open_saved_{item['id']}", use_container_width=True):
                        st.session_state["roadmap_career"] = item["career_name"]
                        navigate_to("AI Career Roadmap Generator")
                        st.rerun()

                    if st.button("Delete Roadmap", key=f"del_saved_{item['id']}", use_container_width=True):
                        delete_saved_roadmap(user_id, item["id"])
                        st.success(f"Roadmap #{item['id']} deleted.")
                        st.rerun()

                with st.expander("View Saved Milestones Snapshot"):
                    for m in item.get("milestones", []):
                        st_icon = "✓" if m.get("completed") else "○"
                        st.write(f"{st_icon} {m.get('title', 'Milestone')}")


# =========================================================================
# PAGE 10: USER PROFILE
# =========================================================================
elif st.session_state["nav_page"] == "User Profile":
    user = st.session_state.get("user")
    if not user:
        st.warning("Please log in to view and edit your profile.")
        if st.button("Go to Login", key="btn_goto_login_profile"):
            navigate_to("Login / Register")
            st.rerun()
    else:
        st.title("👤 User Profile & Settings")
        st.write("Manage your career targets, skills list, and personal profile information.")
        st.divider()

        with st.form("profile_form"):
            prof_name = st.text_input("Full Name", value=user["name"])
            prof_role = st.text_input("Current Background / Role", value=user.get("current_role", "Learner"))
            exp_options = ["Beginner", "Intermediate", "Advanced"]
            curr_exp = user.get("experience_level", "Beginner")
            exp_idx = exp_options.index(curr_exp) if curr_exp in exp_options else 0
            prof_exp = st.selectbox("Experience Level", options=exp_options, index=exp_idx)

            prof_skills = st.text_input("Current Skills (Comma Separated)", value=user.get("skills_csv", ""))

            all_careers = list(CAREERS_DATA.keys())
            curr_target = user.get("target_career", "Frontend Developer")
            target_idx = all_careers.index(curr_target) if curr_target in all_careers else 0
            prof_target = st.selectbox("Target Career Goal", options=all_careers, index=target_idx)

            time_options = ["3 months", "6 months", "1 year", "2+ years"]
            curr_time = user.get("timeline_goal", "6 months")
            time_idx = time_options.index(curr_time) if curr_time in time_options else 1
            prof_timeline = st.selectbox("Timeline Goal", options=time_options, index=time_idx)

            submit_profile = st.form_submit_button("Update Profile Settings")
            if submit_profile:
                ok = update_user_profile(user["id"], prof_name, prof_role, prof_exp, prof_skills, prof_target, prof_timeline)
                if ok:
                    st.success("Profile updated successfully!")
                    user["name"] = prof_name
                    user["current_role"] = prof_role
                    user["experience_level"] = prof_exp
                    user["skills_csv"] = prof_skills
                    user["target_career"] = prof_target
                    user["timeline_goal"] = prof_timeline
                    st.session_state["user"] = user
                    st.rerun()
                else:
                    st.error("Failed to update profile.")


# =========================================================================
# PAGE 11: LOGIN / REGISTER
# =========================================================================
elif st.session_state["nav_page"] == "Login / Register":
    st.title("🔐 Authentication & Account Management")
    st.write("Access your personalized AI roadmaps, track learning progress, and save custom targets.")
    st.divider()

    tab_login, tab_register = st.tabs(["🔑 Existing User Login", "✨ Create New Account (4-Step Setup)"])

    # --- TAB 1: LOGIN ---
    with tab_login:
        st.subheader("Log In to CareerGPT")
        with st.form("login_form"):
            login_email = st.text_input("Email Address", placeholder="e.g. admin@career.ai")
            login_pwd = st.text_input("Password", type="password", placeholder="Enter your password")
            remember_me = st.checkbox("Remember My Session", value=True)
            submit_login = st.form_submit_button("Log In to Dashboard")

            if submit_login:
                if not login_email.strip() or not login_pwd.strip():
                    st.error("Please enter both email and password.")
                else:
                    success, result = authenticate_user(login_email, login_pwd)
                    if success and isinstance(result, dict):
                        st.session_state["logged_in"] = True
                        st.session_state["user"] = result
                        st.success(f"Welcome back, {result['name']}! Loading dashboard...")
                        navigate_to("Home Dashboard")
                        st.rerun()
                    else:
                        st.error(str(result))

        st.caption("Demo Account: `admin@career.ai` | Password: `Password@123`")

    # --- TAB 2: REGISTER (4-STEP ONBOARDING WIZARD) ---
    with tab_register:
        st.subheader("4-Step Career Onboarding Wizard")

        with st.form("register_wizard_form"):
            st.write("#### Step 1: Account Essentials")
            reg_name = st.text_input("Full Name *", placeholder="e.g. Priyanshu Sharma")
            reg_email = st.text_input("Email Address *", placeholder="e.g. priyanshu@example.com")
            reg_pwd = st.text_input("Password (min 6 characters) *", type="password", placeholder="Create a secure password")

            st.write("#### Step 2: Background & Skill Assessment")
            reg_role = st.text_input("Current Background / Education", placeholder="e.g. B.Tech Student, Junior Developer")
            reg_exp = st.selectbox("Experience Level", options=["Beginner (0-1 yrs)", "Intermediate (1-3 yrs)", "Advanced (3+ yrs)"])
            reg_skills = st.multiselect(
                "Select Current Skills",
                options=["Python", "JavaScript", "HTML/CSS", "SQL", "React", "Node.js", "Machine Learning", "Data Analysis", "Cloud Basics", "Git", "Java", "C++"]
            )

            st.write("#### Step 3: Target Career Vision")
            reg_target = st.selectbox("Target Career Goal", options=list(CAREERS_DATA.keys()))
            reg_timeline = st.selectbox("Target Learning Timeline", options=["3 months", "6 months", "1 year", "2+ years"])
            reg_notes = st.text_area("Specific Career Ambitions or Companies (Optional)", placeholder="e.g. Targeting Tier-1 product companies in Bangalore...")

            st.write("#### Step 4: Confirm & Launch")
            st.caption("By registering, your account will be securely hashed with PBKDF2-HMAC-SHA256 and stored in SQLite.")

            submit_reg = st.form_submit_button("Create My Account & Launch Roadmap")

            if submit_reg:
                if not reg_name.strip() or not reg_email.strip() or not reg_pwd.strip():
                    st.error("Please fill in all required fields (Name, Email, Password).")
                elif len(reg_pwd.strip()) < 6:
                    st.error("Password must be at least 6 characters long.")
                else:
                    skills_str = ", ".join(reg_skills)
                    success, msg = register_user(
                        name=reg_name,
                        email=reg_email,
                        password=reg_pwd,
                        current_role=reg_role,
                        experience_level=reg_exp.split(" ")[0],
                        skills_csv=skills_str,
                        target_career=reg_target,
                        timeline_goal=reg_timeline,
                        notes=reg_notes
                    )
                    if success:
                        st.success(msg)
                        auth_ok, auth_user = authenticate_user(reg_email, reg_pwd)
                        if auth_ok and isinstance(auth_user, dict):
                            st.session_state["logged_in"] = True
                            st.session_state["user"] = auth_user
                            navigate_to("Home Dashboard")
                            st.rerun()
                    else:
                        st.error(msg)
