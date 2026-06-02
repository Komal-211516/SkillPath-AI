# database.py - SQLite Database Setup for SkillPath AI

import sqlite3
import json
from datetime import datetime

DB_NAME = "skillpath.db"

def init_db():
    """Create all tables if they don't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_roles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_name TEXT NOT NULL UNIQUE,
            required_skills TEXT NOT NULL,
            roadmap TEXT NOT NULL,
            learning_resources TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_role TEXT NOT NULL,
            matched_skills TEXT NOT NULL,
            missing_skills TEXT NOT NULL,
            match_score INTEGER NOT NULL,
            analyzed_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saved_roadmaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_role TEXT NOT NULL,
            user_notes TEXT,
            saved_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            degree_name TEXT NOT NULL,
            transferable_skills TEXT,
            recommended_roles TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database tables created!")

def seed_job_roles():
    """Insert default job roles into database"""
    from skills_data import job_skills
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for role_name, role_data in job_skills.items():
        cursor.execute('''
            INSERT OR IGNORE INTO job_roles (role_name, required_skills, roadmap, learning_resources)
            VALUES (?, ?, ?, ?)
        ''', (
            role_name,
            json.dumps(role_data["required_skills"]),
            json.dumps(role_data["roadmap"]),
            json.dumps(role_data.get("learning_resources", {}))
        ))

    conn.commit()
    conn.close()
    print(f"✅ {len(job_skills)} job roles added to database!")

def get_job_from_db(role_name):
    """Fetch job role data from database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT required_skills, roadmap, learning_resources FROM job_roles WHERE role_name = ?', (role_name,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "required_skills": json.loads(row[0]),
            "roadmap": json.loads(row[1]),
            "learning_resources": json.loads(row[2]) if row[2] else {}
        }
    return None

def save_result(job_role, matched_skills, missing_skills, score):
    """Save user analysis result to database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_results (job_role, matched_skills, missing_skills, match_score)
        VALUES (?, ?, ?, ?)
    ''', (
        job_role,
        json.dumps(matched_skills),
        json.dumps(missing_skills),
        score
    ))
    conn.commit()
    conn.close()

def get_all_results():
    """Get all past analysis results"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_results ORDER BY analyzed_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_jobs():
    """Get all job roles from database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT role_name, id FROM job_roles ORDER BY role_name')
    rows = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "id": row[1]} for row in rows]

def get_jobs_by_category():
    """Get job roles grouped by category"""
    job_categories = {
        "🤖 AI & Data Science": ["data analyst", "data scientist", "machine learning engineer"],
        "💻 Web & Mobile Development": ["web developer", "frontend developer", "python developer", "android developer", "ios developer"],
        "☁️ Cloud & Infrastructure": ["cloud engineer", "devops engineer"],
        "🔒 Security": ["cybersecurity analyst"],
        "📊 Business & Product": ["business analyst", "product manager", "project coordinator", "sales executive"],
        "🎨 Design": ["ui ux designer", "graphic designer"],
        "📢 Marketing & Content": ["digital marketer", "content writer", "digital marketing analyst"],
        "👥 HR & Management": ["hr generalist"]
    }
    return job_categories

def save_user_profile(degree_name, transferable_skills, recommended_roles):
    """Save user degree profile"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_profiles (degree_name, transferable_skills, recommended_roles)
        VALUES (?, ?, ?)
    ''', (
        degree_name,
        json.dumps(transferable_skills),
        json.dumps(recommended_roles)
    ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    seed_job_roles()
    jobs = get_all_jobs()
    print(f"📋 Jobs in DB ({len(jobs)}):")
    for job in jobs:
        print(f"  - {job['name']}")