# app.py - Main Flask Application with ML, NLP, and Pandas

from flask import Flask, request, jsonify, render_template, session
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import re
import json
import os
from datetime import datetime
from database import init_db, seed_job_roles, get_job_from_db, save_result, get_all_jobs, get_jobs_by_category, save_user_profile
from skills_data import job_skills, get_skill_recommendations_by_degree, learning_resources_db, get_learning_resource
from skills_data import get_certification_path, get_weekly_plan, get_skill_prerequisites, get_project_ideas

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('punkt_tab', quiet=True)

app = Flask(__name__)
app.secret_key = 'skillpathai_secret_key_2024'

# Initialize database
init_db()
seed_job_roles()

# Initialize NLP components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# ============================================
# COMPLETE SKILL DATABASE FOR EXTRACTION
# ============================================

ALL_SKILLS_FOR_EXTRACTION = [
    # Content Writing Skills (matches your resume exactly)
    "writing", "copywriting", "editing", "proofreading", "research",
    "storytelling", "grammar", "seo", "blogging", "content strategy",
    "wordpress", "social media", "communication", "creative writing",
    "fact checking", "competitor analysis", "blog writing", "topic research",
    "fact-checking", "content calendar", "ad copy", "email copy",
    
    # Copywriting Skills
    "persuasion", "advertising", "brand voice", "email marketing", "marketing",
    "landing pages", "headlines",
    
    # Social Media Skills
    "content creation", "community management", "engagement", "trends",
    "instagram", "facebook", "linkedin", "twitter", "youtube",
    "google analytics", "hootsuite",
    
    # Journalism Skills
    "interviewing", "news gathering", "ethics", "investigation",
    "deadline management", "indesign",
    
    # PR Skills
    "media relations", "crisis management", "networking", "press releases",
    
    # Event Skills
    "event planning", "logistics", "organization", "vendor management",
    "budgeting", "trello",
    
    # Design Skills
    "photoshop", "illustrator", "figma", "canva", "typography",
    "color theory", "branding", "layout design", "visual communication",
    "logo design", "adobe xd", "ui design", "ux design", "wireframing",
    "prototyping", "procreate", "after effects", "premiere pro",
    "animation", "motion graphics", "keyframing", "cinema 4d",
    
    # Video/Photo Skills
    "video editing", "audio editing", "color grading", "compression",
    "photography", "lightroom", "composition", "lighting", "retouching",
    
    # Web Development
    "html", "css", "javascript", "react", "nodejs", "bootstrap",
    "tailwind", "responsive design", "git", "github", "rest api",
    "mongodb", "postgresql", "mysql", "sql", "flask", "django",
    "express", "spring boot", "jwt",
    
    # Programming Languages
    "python", "java", "c++", "c", "swift", "kotlin", "typescript",
    "ruby", "go", "rust", "php", "c#",
    
    # Data Science
    "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn",
    "tensorflow", "keras", "pytorch", "transformers", "nltk",
    "machine learning", "deep learning", "statistics", "data visualization",
    "eda", "feature engineering", "tableau", "power bi", "excel", "sqlite",
    "openai", "langchain", "llm", "prompt design", "streamlit",
    
    # Cloud & DevOps
    "aws", "ec2", "s3", "lambda", "rds", "vpc", "iam", "cloudwatch",
    "azure", "docker", "kubernetes", "jenkins", "github actions",
    "terraform", "linux", "bash", "ci/cd", "jenkins pipeline", "aws emr",
    
    # Cybersecurity
    "network security", "firewalls", "encryption", "cryptography",
    "wireshark", "nmap", "incident response", "risk management",
    "security policies",
    
    # Blockchain
    "solidity", "ethereum", "smart contracts", "web3.js", "truffle",
    "remix", "metamask",
    
    # AR/VR
    "unity", "blender", "arcore", "oculus sdk", "ar", "vr", "3d modeling",
    
    # Embedded
    "arduino", "raspberry pi", "stm32", "iot", "firmware development",
    "mqtt", "microcontrollers",
    
    # Mobile Development
    "android studio", "xml", "retrofit", "material design",
    "xcode", "uikit", "auto layout", "urlsession", "mvvm", "core data",
    
    # Business Skills
    "accounting", "finance", "tally", "quickbooks", "gst", "taxation",
    "financial statements", "valuation", "mergers & acquisitions",
    "capital markets", "financial modeling", "requirements gathering",
    "documentation", "jira", "ms project",
    
    # HR Skills
    "recruitment", "onboarding", "employee relations", "hr policies",
    "conflict resolution", "hrms",
    
    # Product Management
    "product strategy", "user research", "prioritization", "user stories",
    "prd writing", "scrum", "notion", "agile",
    
    # Operations
    "operations", "process improvement", "quality control", "erp",
    "supply chain", "inventory management",
    
    # Big Data
    "spark", "pyspark", "hadoop", "hdfs", "etl",
    
    # Soft Skills
    "teamwork", "problem solving", "time management", "presentation",
    "negotiation", "leadership", "creativity", "attention to detail",
    "adaptability", "critical thinking", "organization", "patience",
    "empathy", "persuasion", "confidence",
    
    # Tools
    "ms word", "powerpoint", "google docs", "google sheets", "mailchimp",
    "semrush", "postman", "vscode", "jupyter", "colab", "obs studio",
    "audition", "davinci resolve", "final cut pro", "behance",
    "grammarly", "canva", "notion", "slack", "zoom",
]

# ============================================
# 1. TEXT PREPROCESSING WITH NLP
# ============================================

def preprocess_text_nlp(text):
    if not text:
        return ""
    
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    tokens = word_tokenize(text)
    
    processed_tokens = []
    for token in tokens:
        if token not in stop_words and len(token) > 2:
            lemmatized = lemmatizer.lemmatize(token)
            processed_tokens.append(lemmatized)
    
    return ' '.join(processed_tokens)

# ============================================
# 2. MACHINE LEARNING FOR SIMILARITY ANALYSIS
# ============================================

class ResumeMatcher:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
    
    def calculate_similarity(self, resume_text, job_description):
        if not resume_text or not job_description:
            return 0.0
        
        processed_resume = preprocess_text_nlp(resume_text)
        processed_job = preprocess_text_nlp(job_description)
        
        try:
            tfidf_matrix = self.tfidf_vectorizer.fit_transform([processed_resume, processed_job])
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            return round(similarity * 100, 2)
        except:
            return 0.0
    
    def semantic_skill_matching(self, resume_skills, required_skills):
        matched = []
        for req_skill in required_skills:
            for res_skill in resume_skills:
                if req_skill.lower() in res_skill.lower() or res_skill.lower() in req_skill.lower():
                    matched.append(req_skill)
                    break
        return matched

resume_matcher = ResumeMatcher()

# ============================================
# 3. PANDAS FOR DATA PROCESSING
# ============================================

class DataProcessor:
    def __init__(self):
        self.skills_df = None
        self.jobs_df = None
        self.load_data()
    
    def load_data(self):
        all_skills = []
        for role, data in job_skills.items():
            for skill in data['required_skills']:
                all_skills.append({
                    'job_role': role,
                    'skill': skill,
                    'category': self._categorize_skill(skill)
                })
        
        self.skills_df = pd.DataFrame(all_skills)
        
        jobs_data = []
        for role, data in job_skills.items():
            jobs_data.append({
                'role_name': role,
                'skill_count': len(data['required_skills']),
                'roadmap_steps': len(data['roadmap'])
            })
        
        self.jobs_df = pd.DataFrame(jobs_data)
    
    def _categorize_skill(self, skill):
        design_skills = ['photoshop', 'illustrator', 'figma', 'canva', 'typography', 'color theory', 'branding', 'indesign']
        tech_skills = ['python', 'sql', 'java', 'javascript', 'html', 'css', 'react', 'nodejs']
        ml_skills = ['machine learning', 'deep learning', 'tensorflow', 'keras']
        
        if skill in design_skills:
            return 'Design'
        elif skill in tech_skills:
            return 'Technical'
        elif skill in ml_skills:
            return 'Machine Learning'
        else:
            return 'General'
    
    def analyze_skill_gaps(self, resume_skills, job_role):
        if job_role not in job_skills:
            return None
        
        required_skills = job_skills[job_role]['required_skills']
        
        resume_series = pd.Series([s.lower() for s in resume_skills])
        required_series = pd.Series([s.lower() for s in required_skills])
        
        matched = resume_series[resume_series.isin(required_series)].tolist()
        missing = required_series[~required_series.isin(resume_series)].tolist()
        
        return {
            'total_required': len(required_skills),
            'matched_count': len(matched),
            'missing_count': len(missing),
            'match_percentage': (len(matched) / len(required_skills)) * 100 if required_skills else 0
        }
    
    def get_job_statistics(self):
        if self.jobs_df is None:
            return {}
        
        return {
            'total_jobs': len(self.jobs_df),
            'avg_skills_per_job': round(self.jobs_df['skill_count'].mean(), 2),
            'max_skills_job': self.jobs_df.loc[self.jobs_df['skill_count'].idxmax(), 'role_name'],
            'min_skills_job': self.jobs_df.loc[self.jobs_df['skill_count'].idxmin(), 'role_name']
        }

data_processor = DataProcessor()

# ============================================
# 4. ENHANCED SKILL EXTRACTION WITH NLP
# ============================================

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
        return text
    except Exception as e:
        print(f"PDF extraction error: {e}")
        return ""

def extract_skills_from_text(text):
    """Extract skills from resume text - IMPROVED for Content Writer resume"""
    if not text:
        return []
    
    text_lower = text.lower()
    found_skills = []
    
    # Method 1: Direct word boundary matching
    for skill in ALL_SKILLS_FOR_EXTRACTION:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
    
    # Method 2: Extract from SKILLS section
    skills_section_match = re.search(r'skills:?(.*?)(?:\n\n|\n[A-Z]|$)', text_lower, re.DOTALL)
    if skills_section_match:
        skills_text = skills_section_match.group(1)
        skill_items = re.split(r'[•·,\n•]+', skills_text)
        for item in skill_items:
            item = item.strip()
            if 2 < len(item) < 40:
                for skill in ALL_SKILLS_FOR_EXTRACTION:
                    if skill in item or item in skill:
                        if skill not in found_skills:
                            found_skills.append(skill)
                        break
    
    # Method 3: Look for specific keywords
    content_keywords = [
        "writing", "copywriting", "editing", "proofreading", "research",
        "storytelling", "grammar", "seo", "blogging", "content strategy",
        "wordpress", "social media", "communication", "creative writing",
        "fact checking", "competitor analysis"
    ]
    
    for keyword in content_keywords:
        if keyword in text_lower:
            if keyword not in found_skills:
                found_skills.append(keyword)
    
    return list(set(found_skills))

# ============================================
# 5. ENHANCED MATCH CALCULATION WITH ML - FIXED
# ============================================

def calculate_match(resume_skills, job_role, resume_text=""):
    """Enhanced match calculation using ML similarity with learning resources"""
    job_data = get_job_from_db(job_role)
    
    if not job_data:
        return None
    
    required = job_data["required_skills"]
    roadmap = job_data["roadmap"]
    job_learning_resources = job_data.get("learning_resources", {})
    
    print(f"\n=== SKILL MATCHING DEBUG ===")
    print(f"Resume skills found: {resume_skills}")
    print(f"Required skills for {job_role}: {required}")
    
    resume_skills_lower = [s.lower().strip() for s in resume_skills]
    required_lower = [r.lower().strip() for r in required]
    
    matched = []
    missing = []
    
    for req in required_lower:
        found = False
        for res in resume_skills_lower:
            if req == res:
                found = True
                break
            elif req in res or res in req:
                found = True
                break
            elif req.replace(" ", "").replace("_", "") in res.replace(" ", "").replace("_", ""):
                found = True
                break
        
        if found:
            original_skill = next((s for s in required if s.lower() == req), req)
            matched.append(original_skill)
        else:
            missing.append(req)
    
    basic_score = int((len(matched) / len(required)) * 100) if required else 0
    print(f"Matched: {len(matched)}/{len(required)} = {basic_score}%")
    print(f"Matched skills: {matched}")
    print(f"Missing skills: {missing}")
    
    ml_similarity_score = 0
    if resume_text:
        # FIX: Convert roadmap steps to strings properly (extract 'step' from each dict)
        roadmap_text = ' '.join([step['step'] if isinstance(step, dict) else str(step) for step in roadmap])
        job_description = ' '.join(required) + ' ' + roadmap_text
        ml_similarity_score = resume_matcher.calculate_similarity(resume_text, job_description)
    
    final_score = int((basic_score * 0.6) + (ml_similarity_score * 0.4))
    
    missing_with_links = []
    for skill in missing:
        link = job_learning_resources.get(skill)
        if not link:
            link = learning_resources_db.get(skill)
        if not link:
            link = get_learning_resource(skill)
        missing_with_links.append({"skill": skill, "link": link})
    
    return {
        "score": final_score,
        "basic_score": basic_score,
        "ml_similarity_score": round(ml_similarity_score, 2),
        "matched_skills": matched,
        "missing_skills": missing,
        "missing_with_links": missing_with_links,
        "semantic_matched": resume_matcher.semantic_skill_matching(resume_skills, required),
        "roadmap": roadmap,
        "learning_resources": job_learning_resources,
        "total_required": len(required),
        "skill_gap_analysis": data_processor.analyze_skill_gaps(resume_skills, job_role),
        "technologies_used": {
            "nlp": True,
            "machine_learning": True,
            "pandas": True,
            "flask": True
        }
    }

# ============================================
# 6. FLASK ROUTES
# ============================================

@app.route("/")
def home():
    jobs = get_all_jobs()
    job_categories = get_jobs_by_category()
    job_stats = data_processor.get_job_statistics()
    return render_template("index.html", jobs=jobs, job_categories=job_categories, job_stats=job_stats)

@app.route("/api/jobs")
def get_jobs():
    jobs = get_all_jobs()
    return jsonify(jobs)

@app.route("/api/job-statistics")
def get_job_statistics():
    stats = data_processor.get_job_statistics()
    return jsonify(stats)

@app.route("/api/degree-recommendations", methods=["POST"])
def degree_recommendations():
    try:
        data = request.get_json()
        degree_name = data.get("degree_name", "").strip()
        
        if not degree_name:
            return jsonify({"error": "Please provide degree name"}), 400
        
        recommendations = get_skill_recommendations_by_degree(degree_name)
        
        save_user_profile(
            degree_name, 
            recommendations["transferable_skills"], 
            recommendations["recommended_roles"]
        )
        
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        job_role = request.form.get("job_role", "").lower().strip()
        pdf_file = request.files.get("resume")

        if not pdf_file or not job_role:
            return jsonify({"error": "Please upload resume and enter job role"})

        resume_text = extract_text_from_pdf(pdf_file)

        if not resume_text:
            return jsonify({"error": "Could not read PDF. Please try another file."})

        resume_skills = extract_skills_from_text(resume_text)
        print(f"\n=== EXTRACTED SKILLS ({len(resume_skills)}): {resume_skills} ===")
        
        result = calculate_match(resume_skills, job_role, resume_text)

        if not result:
            all_jobs = [job["name"] for job in get_all_jobs()]
            jobs_list = ", ".join(all_jobs[:15])
            return jsonify({"error": f"Job role '{job_role}' not found. Available roles: {jobs_list}..."})

        save_result(job_role, result["matched_skills"], result["missing_skills"], result["score"])

        return jsonify(result)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# ============================================
# 7. NEW API ENDPOINTS FOR ENHANCED FEATURES
# ============================================

@app.route("/api/skill-prerequisites", methods=["POST"])
def api_skill_prerequisites():
    """Get prerequisites for a skill"""
    try:
        data = request.get_json()
        skill_name = data.get("skill", "")
        prerequisites = get_skill_prerequisites(skill_name)
        return jsonify({"skill": skill_name, "prerequisites": prerequisites})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/project-ideas", methods=["POST"])
def api_project_ideas():
    """Get project ideas for a skill"""
    try:
        data = request.get_json()
        skill_name = data.get("skill", "")
        projects = get_project_ideas(skill_name)
        return jsonify({"skill": skill_name, "projects": projects})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/certifications/<job_role>")
def api_certifications(job_role):
    """Get certification paths for a job role"""
    certifications = get_certification_path(job_role)
    return jsonify({"job_role": job_role, "certifications": certifications})

@app.route("/api/weekly-plan", methods=["POST"])
def api_weekly_plan():
    """Get weekly action plan"""
    try:
        data = request.get_json()
        job_role = data.get("job_role", "")
        week_number = data.get("week_number", 1)
        plan = get_weekly_plan(job_role, week_number)
        return jsonify({"job_role": job_role, "week": week_number, "plan": plan})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/technology-info")
def technology_info():
    return jsonify({
        "technologies": {
            "Python": "Main programming language",
            "Natural Language Processing (NLP)": "Tokenization, lemmatization, text understanding",
            "Machine Learning": "TF-IDF vectorization and cosine similarity",
            "Pandas": "Data processing and skill gap analysis",
            "Flask": "Web framework",
            "HTML/CSS/JavaScript": "Frontend UI"
        }
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)