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
from skills_data import job_skills, get_skill_recommendations_by_degree

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
# 1. TEXT PREPROCESSING WITH NLP
# ============================================

def preprocess_text_nlp(text):
    """
    Advanced text preprocessing using NLP techniques
    - Tokenization
    - Stopword removal
    - Lemmatization
    """
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
    """ML-based resume matching using TF-IDF and Cosine Similarity"""
    
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
    
    def calculate_similarity(self, resume_text, job_description):
        """Calculate cosine similarity between resume and job requirements"""
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
        """Semantic matching using string similarity"""
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
    """Handle all data processing using Pandas"""
    
    def __init__(self):
        self.skills_df = None
        self.jobs_df = None
        self.load_data()
    
    def load_data(self):
        """Load job and skill data into Pandas DataFrames"""
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
        """Categorize skills into types"""
        tech_skills = ['python', 'sql', 'java', 'javascript', 'html', 'css']
        ml_skills = ['machine learning', 'deep learning', 'tensorflow', 'keras']
        if skill in tech_skills:
            return 'Technical'
        elif skill in ml_skills:
            return 'Machine Learning'
        else:
            return 'General'
    
    def analyze_skill_gaps(self, resume_skills, job_role):
        """Analyze skill gaps using Pandas operations"""
        if job_role not in job_skills:
            return None
        
        required_skills = job_skills[job_role]['required_skills']
        
        resume_series = pd.Series(resume_skills)
        required_series = pd.Series(required_skills)
        
        matched = resume_series[resume_series.isin(required_series)].tolist()
        missing = required_series[~required_series.isin(resume_series)].tolist()
        
        return {
            'total_required': len(required_skills),
            'matched_count': len(matched),
            'missing_count': len(missing),
            'match_percentage': (len(matched) / len(required_skills)) * 100 if required_skills else 0
        }
    
    def get_job_statistics(self):
        """Get job market statistics using Pandas"""
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
    """Extract text from uploaded PDF resume"""
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

def advanced_skill_extraction(text):
    """Advanced skill extraction using NLP techniques"""
    if not text:
        return []
    
    text_lower = text.lower()
    
    skill_categories = {
        'programming_languages': ['python', 'java', 'javascript', 'c++', 'swift', 'kotlin', 'typescript'],
        'web_technologies': ['html', 'css', 'react', 'angular', 'vue', 'nodejs', 'django', 'flask'],
        'data_science': ['pandas', 'numpy', 'tensorflow', 'keras', 'scikit-learn', 'matplotlib'],
        'databases': ['sql', 'mysql', 'postgresql', 'mongodb', 'oracle'],
        'cloud_devops': ['aws', 'azure', 'docker', 'kubernetes', 'jenkins', 'terraform'],
        'ml_ai': ['machine learning', 'deep learning', 'nlp', 'computer vision'],
        'soft_skills': ['communication', 'leadership', 'teamwork', 'problem solving']
    }
    
    extracted_skills = []
    
    for category, skills in skill_categories.items():
        for skill in skills:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                extracted_skills.append(skill)
    
    multi_word_skills = ['machine learning', 'deep learning', 'data science', 'big data']
    for skill in multi_word_skills:
        if skill in text_lower:
            extracted_skills.append(skill)
    
    return list(set(extracted_skills))

def extract_skills_from_text(text):
    """Main skill extraction function using NLP"""
    try:
        skills = advanced_skill_extraction(text)
        if not skills:
            skills = basic_skill_extraction(text)
        return skills
    except Exception as e:
        print(f"Skill extraction error: {e}")
        return basic_skill_extraction(text)

def basic_skill_extraction(text):
    """Fallback basic skill extraction"""
    basic_skills = [
        "python", "sql", "excel", "tableau", "power bi", "statistics",
        "pandas", "numpy", "machine learning", "deep learning", "tensorflow",
        "html", "css", "javascript", "react", "nodejs", "git", "docker", "aws"
    ]
    found = []
    text_lower = text.lower()
    for skill in basic_skills:
        if skill in text_lower:
            found.append(skill)
    return found

# ============================================
# 5. ENHANCED MATCH CALCULATION WITH ML
# ============================================

def calculate_match(resume_skills, job_role, resume_text=""):
    """Enhanced match calculation using ML similarity"""
    job_data = get_job_from_db(job_role)
    
    if not job_data:
        return None
    
    required = job_data["required_skills"]
    roadmap = job_data["roadmap"]
    learning_resources = job_data["learning_resources"]
    
    matched = [s for s in resume_skills if s in required]
    missing = [s for s in required if s not in resume_skills]
    basic_score = int((len(matched) / len(required)) * 100) if required else 0
    
    ml_similarity_score = 0
    if resume_text:
        job_description = ' '.join(required) + ' ' + ' '.join(roadmap)
        ml_similarity_score = resume_matcher.calculate_similarity(resume_text, job_description)
    
    semantic_matched = resume_matcher.semantic_skill_matching(resume_skills, required)
    final_score = int((basic_score * 0.6) + (ml_similarity_score * 0.4))
    skill_gap_analysis = data_processor.analyze_skill_gaps(resume_skills, job_role)
    
    return {
        "score": final_score,
        "basic_score": basic_score,
        "ml_similarity_score": round(ml_similarity_score, 2),
        "matched_skills": matched,
        "missing_skills": missing,
        "semantic_matched": semantic_matched,
        "roadmap": roadmap,
        "learning_resources": learning_resources,
        "total_required": len(required),
        "skill_gap_analysis": skill_gap_analysis,
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