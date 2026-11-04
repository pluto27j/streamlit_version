import os
import sqlite3
import hashlib
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "career_roadmap.db"

def get_connection():
    """Returns a connection to the SQLite database."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str, salt: bytes = None) -> tuple[str, str]:
    """Hashes a password using PBKDF2-HMAC-SHA256 with 100,000 iterations."""
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return hashed.hex(), salt.hex()

def verify_password(stored_hash: str, stored_salt_hex: str, password_attempt: str) -> bool:
    """Verifies a password against the stored PBKDF2 hash and salt."""
    salt = bytes.fromhex(stored_salt_hex)
    computed_hash = hashlib.pbkdf2_hmac("sha256", password_attempt.encode("utf-8"), salt, 100_000).hex()
    return computed_hash == stored_hash

def init_db():
    """Initializes SQLite schema and populates default demo data if needed."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        current_role TEXT DEFAULT 'Learner',
        experience_level TEXT DEFAULT 'Beginner',
        skills_csv TEXT DEFAULT '',
        target_career TEXT DEFAULT 'Frontend Developer',
        timeline_goal TEXT DEFAULT '6 months',
        notes TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saved_roadmaps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        career_name TEXT NOT NULL,
        timeline_goal TEXT DEFAULT '6 months',
        experience_level TEXT DEFAULT 'Beginner',
        job_readiness INTEGER DEFAULT 0,
        milestones_json TEXT DEFAULT '[]',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_milestones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        career_name TEXT NOT NULL,
        stage_index INTEGER NOT NULL,
        milestone_index INTEGER NOT NULL,
        is_completed INTEGER DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (user_id, career_name, stage_index, milestone_index),
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        activity_type TEXT NOT NULL,
        description TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    """)

    conn.commit()

    # Seed demo user if not present
    cursor.execute("SELECT id FROM users WHERE email = ?", ("admin@career.ai",))
    if not cursor.fetchone():
        pwd_hash, salt_hex = hash_password("Password@123")
        cursor.execute("""
            INSERT INTO users (
                name, email, password_hash, salt, current_role,
                experience_level, skills_csv, target_career, timeline_goal, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "John Doe",
            "admin@career.ai",
            pwd_hash,
            salt_hex,
            "Aspiring AI Engineer",
            "Intermediate",
            "Python, Data Analysis, Machine Learning, SQL",
            "AI Engineer",
            "6 months",
            "Targeting tech leadership in AI solutions."
        ))
        user_id = cursor.lastrowid

        # Seed initial activities
        seed_activities = [
            ("Quiz", "Completed Python OOP & Data Structures Quiz with 94% score"),
            ("Resume", "Uploaded and analyzed resume for AI Engineer role (Match: 82%)"),
            ("Interview", "Practiced 15 AI Engineering Technical Interview Questions"),
            ("Skill", "Added PyTorch and Vector Databases to profile core competencies"),
            ("Roadmap", "Started Stage 1: Mathematical Foundations & Python for AI")
        ]
        for act_type, desc in seed_activities:
            cursor.execute("""
                INSERT INTO activities (user_id, activity_type, description)
                VALUES (?, ?, ?)
            """, (user_id, act_type, desc))

        conn.commit()

    conn.close()

# ----------------- User Authentication Functions -----------------

def register_user(name: str, email: str, password: str, current_role: str = "Learner",
                  experience_level: str = "Beginner", skills_csv: str = "",
                  target_career: str = "Frontend Developer", timeline_goal: str = "6 months",
                  notes: str = "") -> tuple[bool, str]:
    """Registers a new user with securely hashed password."""
    email = email.strip().lower()
    if not name.strip() or not email or not password:
        return False, "Name, email, and password cannot be empty."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return False, "An account with this email already exists."

        pwd_hash, salt_hex = hash_password(password)
        cursor.execute("""
            INSERT INTO users (
                name, email, password_hash, salt, current_role,
                experience_level, skills_csv, target_career, timeline_goal, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name.strip(), email, pwd_hash, salt_hex, current_role.strip(),
            experience_level, skills_csv.strip(), target_career.strip(),
            timeline_goal, notes.strip()
        ))
        user_id = cursor.lastrowid
        # Log welcome activity
        cursor.execute("""
            INSERT INTO activities (user_id, activity_type, description)
            VALUES (?, ?, ?)
        """, (user_id, "Account", "Account created successfully. Welcome to CareerGPT!"))
        conn.commit()
        return True, "Registration successful! You can now log in."
    except Exception as e:
        return False, f"Database error: {str(e)}"
    finally:
        conn.close()

def authenticate_user(email: str, password: str) -> tuple[bool, dict | str]:
    """Authenticates a user by email and password using PBKDF2 hash verification."""
    email = email.strip().lower()
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        if not row:
            return False, "Invalid email or password."

        stored_hash = row["password_hash"]
        stored_salt = row["salt"]
        if verify_password(stored_hash, stored_salt, password):
            user_data = {
                "id": row["id"],
                "name": row["name"],
                "email": row["email"],
                "current_role": row["current_role"],
                "experience_level": row["experience_level"],
                "skills_csv": row["skills_csv"],
                "target_career": row["target_career"],
                "timeline_goal": row["timeline_goal"],
                "notes": row["notes"],
                "created_at": row["created_at"]
            }
            return True, user_data
        return False, "Invalid email or password."
    finally:
        conn.close()

def update_user_profile(user_id: int, name: str, current_role: str, experience_level: str,
                        skills_csv: str, target_career: str, timeline_goal: str) -> bool:
    """Updates user profile details."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE users SET
                name = ?, current_role = ?, experience_level = ?,
                skills_csv = ?, target_career = ?, timeline_goal = ?
            WHERE id = ?
        """, (name, current_role, experience_level, skills_csv, target_career, timeline_goal, user_id))
        cursor.execute("""
            INSERT INTO activities (user_id, activity_type, description)
            VALUES (?, ?, ?)
        """, (user_id, "Profile", "Updated career preferences and profile details"))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

# ----------------- Milestone Tracking Functions -----------------

def get_completed_milestones(user_id: int, career_name: str) -> set[tuple[int, int]]:
    """Returns a set of (stage_index, milestone_index) tuples completed by the user."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT stage_index, milestone_index FROM user_milestones
            WHERE user_id = ? AND career_name = ? AND is_completed = 1
        """, (user_id, career_name))
        return {(row["stage_index"], row["milestone_index"]) for row in cursor.fetchall()}
    finally:
        conn.close()

def toggle_milestone(user_id: int, career_name: str, stage_index: int, milestone_index: int, is_completed: bool, milestone_title: str = ""):
    """Toggles or updates milestone status in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    val = 1 if is_completed else 0
    try:
        cursor.execute("""
            INSERT INTO user_milestones (user_id, career_name, stage_index, milestone_index, is_completed, updated_at)
            VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, career_name, stage_index, milestone_index)
            DO UPDATE SET is_completed = excluded.is_completed, updated_at = CURRENT_TIMESTAMP
        """, (user_id, career_name, stage_index, milestone_index, val))

        if is_completed and milestone_title:
            cursor.execute("""
                INSERT INTO activities (user_id, activity_type, description)
                VALUES (?, ?, ?)
            """, (user_id, "Milestone", f"Completed milestone: '{milestone_title}' in {career_name}"))
        conn.commit()
    finally:
        conn.close()

# ----------------- Saved Roadmaps Functions -----------------

def save_roadmap(user_id: int, career_name: str, timeline_goal: str, experience_level: str,
                 job_readiness: int, milestones_state: list) -> int:
    """Saves or updates a custom roadmap for the user."""
    conn = get_connection()
    cursor = conn.cursor()
    milestones_json = json.dumps(milestones_state)
    try:
        cursor.execute("""
            SELECT id FROM saved_roadmaps
            WHERE user_id = ? AND career_name = ?
        """, (user_id, career_name))
        existing = cursor.fetchone()
        if existing:
            roadmap_id = existing["id"]
            cursor.execute("""
                UPDATE saved_roadmaps SET
                    timeline_goal = ?, experience_level = ?, job_readiness = ?,
                    milestones_json = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (timeline_goal, experience_level, job_readiness, milestones_json, roadmap_id))
        else:
            cursor.execute("""
                INSERT INTO saved_roadmaps (
                    user_id, career_name, timeline_goal, experience_level, job_readiness, milestones_json
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, career_name, timeline_goal, experience_level, job_readiness, milestones_json))
            roadmap_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO activities (user_id, activity_type, description)
            VALUES (?, ?, ?)
        """, (user_id, "Roadmap", f"Saved career roadmap for '{career_name}' (Readiness: {job_readiness}%)"))
        conn.commit()
        return roadmap_id
    finally:
        conn.close()

def get_user_saved_roadmaps(user_id: int) -> list[dict]:
    """Retrieves all saved roadmaps for a user."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT * FROM saved_roadmaps
            WHERE user_id = ?
            ORDER BY updated_at DESC
        """, (user_id,))
        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row["id"],
                "career_name": row["career_name"],
                "timeline_goal": row["timeline_goal"],
                "experience_level": row["experience_level"],
                "job_readiness": row["job_readiness"],
                "milestones": json.loads(row["milestones_json"]) if row["milestones_json"] else [],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            })
        return results
    finally:
        conn.close()

def delete_saved_roadmap(user_id: int, roadmap_id: int) -> bool:
    """Deletes a saved roadmap."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM saved_roadmaps WHERE id = ? AND user_id = ?", (roadmap_id, user_id))
        conn.commit()
        return True
    finally:
        conn.close()

# ----------------- User Activity Logging -----------------

def log_activity(user_id: int, activity_type: str, description: str):
    """Logs an activity item for the user."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO activities (user_id, activity_type, description)
            VALUES (?, ?, ?)
        """, (user_id, activity_type, description))
        conn.commit()
    finally:
        conn.close()

def get_user_activities(user_id: int, limit: int = 10) -> list[dict]:
    """Retrieves recent activities for a user."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT * FROM activities
            WHERE user_id = ?
            ORDER BY created_at DESC LIMIT ?
        """, (user_id, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()

def get_user_dashboard_stats(user_id: int) -> dict:
    """Computes real-time dashboard KPIs for the user."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Total completed milestones
        cursor.execute("""
            SELECT COUNT(*) AS cnt FROM user_milestones
            WHERE user_id = ? AND is_completed = 1
        """, (user_id,))
        milestones_done = cursor.fetchone()["cnt"]

        # Number of saved roadmaps
        cursor.execute("""
            SELECT COUNT(*) AS cnt FROM saved_roadmaps
            WHERE user_id = ?
        """, (user_id,))
        saved_count = cursor.fetchone()["cnt"]

        # User profile
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user_row = cursor.fetchone()
        skills_count = 0
        profile_completion = 50
        if user_row:
            skills = [s.strip() for s in user_row["skills_csv"].split(",") if s.strip()]
            skills_count = len(skills)
            if user_row["name"]: profile_completion += 10
            if user_row["current_role"]: profile_completion += 10
            if user_row["target_career"]: profile_completion += 10
            if skills_count > 0: profile_completion += 15
            if saved_count > 0: profile_completion += 5
            profile_completion = min(profile_completion, 100)

        # Average readiness across saved roadmaps or milestone ratio
        job_match = 65
        if saved_count > 0:
            cursor.execute("""
                SELECT AVG(job_readiness) AS avg_readiness FROM saved_roadmaps
                WHERE user_id = ?
            """, (user_id,))
            avg_r = cursor.fetchone()["avg_readiness"]
            if avg_r is not None:
                job_match = int(avg_r)

        return {
            "profile_completion": profile_completion,
            "skills_acquired": max(skills_count, 12),
            "milestones_done": milestones_done,
            "saved_roadmaps": saved_count,
            "job_match_score": job_match
        }
    finally:
        conn.close()
