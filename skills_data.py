# skills_data.py - Complete job skills database with 40+ roles for all degrees

job_skills = {
    # ============================================
    # ROLES FOR ARTS / HUMANITIES GRADUATES (BA, BFA, Journalism)
    # ============================================
    
    "content writer": {
        "required_skills": ["writing", "editing", "research", "seo", "blogging", "copywriting", "storytelling", "grammar", "content strategy", "wordpress", "social media", "proofreading", "communication", "creative writing"],
        "roadmap": ["Master English grammar and writing", "Learn SEO writing", "Study content formats", "Learn WordPress", "Practice copywriting", "Build portfolio of 10+ samples", "Start a blog", "Freelance on platforms"],
        "learning_resources": {"seo": "https://moz.com/beginners-guide-to-seo", "wordpress": "https://wordpress.com/learn/", "copywriting": "https://www.copyblogger.com/"}
    },
    
    "copywriter": {
        "required_skills": ["copywriting", "persuasion", "marketing", "advertising", "brand voice", "headlines", "cta", "email marketing", "landing pages", "social media", "research", "creativity"],
        "roadmap": ["Learn copywriting fundamentals", "Study advertising psychology", "Master headline writing", "Learn email marketing", "Practice writing ads", "Build portfolio", "Get certified in copywriting"],
        "learning_resources": {"copywriting": "https://www.copyblogger.com/", "email marketing": "https://mailchimp.com/resources/"}
    },
    
    "social media manager": {
        "required_skills": ["social media", "content creation", "community management", "instagram", "facebook", "linkedin", "twitter", "tiktok", "analytics", "scheduling", "engagement", "trends", "branding"],
        "roadmap": ["Learn social media platforms", "Study content strategy", "Master scheduling tools", "Learn analytics", "Practice community management", "Build portfolio", "Get Meta certified"],
        "learning_resources": {"social media": "https://www.facebook.com/business/learn", "analytics": "https://analytics.google.com/"}
    },
    
    "journalist": {
        "required_skills": ["writing", "research", "interviewing", "fact-checking", "news gathering", "ethics", "investigation", "deadline management", "editing", "storytelling", "media law"],
        "roadmap": ["Master news writing", "Learn investigative techniques", "Study media ethics", "Practice interviewing", "Build portfolio", "Intern at news outlets", "Get journalism certification"],
        "learning_resources": {"writing": "https://www.poynter.org/", "research": "https://www.journalism.org/"}
    },
    
    "public relations specialist": {
        "required_skills": ["communication", "media relations", "press releases", "crisis management", "branding", "storytelling", "event planning", "social media", "writing", "networking"],
        "roadmap": ["Learn PR fundamentals", "Master press release writing", "Study crisis communication", "Learn media monitoring", "Build media contacts", "Get PR certification"],
        "learning_resources": {"pr": "https://www.prsa.org/", "crisis management": "https://www.instituteforpr.org/"}
    },
    
    "event coordinator": {
        "required_skills": ["event planning", "organization", "budgeting", "vendor management", "logistics", "communication", "problem solving", "time management", "negotiation", "creativity"],
        "roadmap": ["Learn event planning basics", "Master budgeting", "Study logistics management", "Learn vendor negotiation", "Plan 2-3 events", "Get CMP certification"],
        "learning_resources": {"event planning": "https://www.mpi.org/", "budgeting": "https://www.eventbrite.com/blog/"}
    },
    
    "graphic designer": {
        "required_skills": ["photoshop", "illustrator", "figma", "typography", "color theory", "branding", "indesign", "layout design", "canva", "visual communication", "logo design", "premiere pro"],
        "roadmap": ["Learn design fundamentals", "Master Photoshop/Illustrator", "Learn Figma", "Study branding", "Learn InDesign", "Build Behance portfolio", "Freelance"],
        "learning_resources": {"photoshop": "https://helpx.adobe.com/photoshop/tutorials.html", "figma": "https://help.figma.com/"}
    },
    
    "ui ux designer": {
        "required_skills": ["figma", "adobe xd", "user research", "wireframing", "prototyping", "visual design", "interaction design", "usability testing", "design systems", "html", "css", "user personas"],
        "roadmap": ["Learn design principles", "Master Figma", "Learn user research", "Study interaction design", "Practice wireframing", "Learn usability testing", "Build portfolio"],
        "learning_resources": {"figma": "https://help.figma.com/", "user research": "https://www.nngroup.com/"}
    },
    
    "video editor": {
        "required_skills": ["premiere pro", "after effects", "final cut pro", "video editing", "motion graphics", "color grading", "audio editing", "storytelling", "compression", "codecs"],
        "roadmap": ["Learn editing software", "Master Premiere Pro", "Learn After Effects", "Study color grading", "Practice editing", "Build showreel", "Freelance"],
        "learning_resources": {"premiere pro": "https://helpx.adobe.com/premiere-pro/tutorials.html", "after effects": "https://helpx.adobe.com/after-effects/tutorials.html"}
    },
    
    "photographer": {
        "required_skills": ["photography", "lightroom", "photoshop", "composition", "lighting", "editing", "portrait", "product", "event", "business", "marketing"],
        "roadmap": ["Master camera settings", "Learn composition", "Study lighting", "Learn Lightroom/Photoshop", "Build portfolio", "Create website", "Market services"],
        "learning_resources": {"photography": "https://www.canon.com/learning/", "lightroom": "https://helpx.adobe.com/lightroom/tutorials.html"}
    },
    
    "illustrator": {
        "required_skills": ["illustrator", "photoshop", "drawing", "sketching", "color theory", "composition", "digital art", "character design", "storyboarding", "visual storytelling"],
        "roadmap": ["Learn fundamentals", "Master Illustrator", "Learn Photoshop", "Study color theory", "Practice daily", "Build portfolio", "Sell on marketplaces"],
        "learning_resources": {"illustrator": "https://helpx.adobe.com/illustrator/tutorials.html", "digital art": "https://www.proko.com/"}
    },
    
    "motion graphics designer": {
        "required_skills": ["after effects", "premiere pro", "cinema 4d", "animation", "motion graphics", "typography", "storyboarding", "illustrator", "photoshop", "sound design"],
        "roadmap": ["Learn After Effects", "Master Premiere Pro", "Learn Cinema 4D", "Study animation principles", "Learn sound design", "Build showreel", "Freelance"],
        "learning_resources": {"after effects": "https://helpx.adobe.com/after-effects/tutorials.html", "cinema 4d": "https://www.maxon.net/en/training"}
    },
    
    "web designer": {
        "required_skills": ["figma", "adobe xd", "html", "css", "javascript", "responsive design", "typography", "color theory", "ux design", "prototyping", "wordpress"],
        "roadmap": ["Learn design tools", "Master Figma", "Learn HTML/CSS", "Study responsive design", "Learn basic JS", "Build portfolio", "Get clients"],
        "learning_resources": {"figma": "https://help.figma.com/", "html": "https://developer.mozilla.org/"}
    },

    # ============================================
    # ROLES FOR COMMERCE GRADUATES
    # ============================================
    
    "business analyst": {
        "required_skills": ["excel", "sql", "communication", "problem solving", "requirements gathering", "agile", "scrum", "data analysis", "documentation", "stakeholder management", "power bi"],
        "roadmap": ["Master Excel", "Learn SQL", "Study business process", "Learn Agile/Scrum", "Practice requirements gathering", "Learn data viz", "Get ECBA cert", "Build case studies"],
        "learning_resources": {"excel": "https://support.microsoft.com/excel", "sql": "https://www.w3schools.com/sql/", "agile": "https://www.agilealliance.org/"}
    },
    
    "financial analyst": {
        "required_skills": ["excel", "financial modeling", "accounting", "valuation", "financial statements", "budgeting", "forecasting", "data analysis", "power bi"],
        "roadmap": ["Master Advanced Excel", "Learn financial modeling", "Study accounting principles", "Learn valuation techniques", "Master financial statements", "Get CFA/CPA certification"],
        "learning_resources": {"excel": "https://support.microsoft.com/excel", "financial modeling": "https://corporatefinanceinstitute.com/"}
    },
    
    "accountant": {
        "required_skills": ["accounting", "taxation", "tally", "quickbooks", "gst", "financial statements", "auditing", "excel", "bookkeeping"],
        "roadmap": ["Learn accounting principles", "Master Tally/QuickBooks", "Study taxation", "Learn GST compliance", "Practice bookkeeping", "Get CA/CPA certification"],
        "learning_resources": {"accounting": "https://www.icai.org/", "tally": "https://tallysolutions.com/"}
    },
    
    "digital marketing analyst": {
        "required_skills": ["google analytics", "seo", "data analysis", "excel", "sql", "tableau", "marketing metrics", "conversion tracking", "a/b testing", "google ads"],
        "roadmap": ["Master Google Analytics", "Learn SQL", "Master Excel", "Learn data viz", "Study attribution models", "Learn A/B testing", "Get GA certification"],
        "learning_resources": {"google analytics": "https://analytics.google.com/analytics/academy/", "sql": "https://www.w3schools.com/sql/"}
    },
    
    "marketing coordinator": {
        "required_skills": ["marketing", "campaign management", "social media", "email marketing", "content creation", "analytics", "market research", "branding", "communication"],
        "roadmap": ["Learn marketing fundamentals", "Master campaign management", "Study social media marketing", "Learn email marketing", "Practice market research", "Get HubSpot certification"],
        "learning_resources": {"marketing": "https://academy.hubspot.com/", "email marketing": "https://mailchimp.com/resources/"}
    },
    
    "sales executive": {
        "required_skills": ["communication", "negotiation", "crm", "lead generation", "cold calling", "client relationship", "salesforce", "presentation", "closing skills"],
        "roadmap": ["Learn sales fundamentals", "Master CRM tools", "Learn lead generation", "Practice cold calling", "Study negotiation", "Get Salesforce certification"],
        "learning_resources": {"salesforce": "https://trailhead.salesforce.com/", "crm": "https://www.salesforce.com/crm/"}
    },
    
    "project coordinator": {
        "required_skills": ["communication", "ms project", "excel", "jira", "risk management", "budgeting", "scheduling", "client management", "documentation", "agile", "scrum"],
        "roadmap": ["Learn project management", "Master MS Project/Excel", "Learn Agile/Scrum", "Master Jira/Trello", "Study risk management", "Get CAPM certification"],
        "learning_resources": {"ms project": "https://support.microsoft.com/project", "jira": "https://www.atlassian.com/software/jira/guides"}
    },
    
    "hr generalist": {
        "required_skills": ["recruitment", "employee relations", "performance management", "hr policies", "labor laws", "payroll", "communication", "conflict resolution", "onboarding"],
        "roadmap": ["Learn recruitment", "Study labor laws", "Master onboarding", "Learn performance management", "Study HRMS tools", "Get SHRM certification"],
        "learning_resources": {"recruitment": "https://www.shrm.org/", "labor laws": "https://www.dol.gov/"}
    },
    
    "product manager": {
        "required_skills": ["communication", "agile", "product strategy", "market research", "user experience", "data analysis", "roadmapping", "scrum", "prioritization"],
        "roadmap": ["Learn product lifecycle", "Master Agile/Scrum", "Learn analytics tools", "Study user research", "Learn roadmapping", "Get CSPO certification"],
        "learning_resources": {"product strategy": "https://www.productschool.com/", "agile": "https://www.agilealliance.org/"}
    },

    # ============================================
    # ROLES FOR TECH GRADUATES
    # ============================================
    
    "data analyst": {
        "required_skills": ["python", "sql", "excel", "tableau", "power bi", "statistics", "pandas", "numpy", "data visualization", "machine learning"],
        "roadmap": ["Learn Python basics", "Learn SQL", "Practice Excel", "Learn Pandas/NumPy", "Learn data viz", "Study statistics", "Build projects", "Apply for jobs"],
        "learning_resources": {"python": "https://www.python.org/", "sql": "https://www.w3schools.com/sql/", "tableau": "https://www.tableau.com/learn/training"}
    },
    
    "data scientist": {
        "required_skills": ["python", "sql", "statistics", "machine learning", "pandas", "numpy", "deep learning", "data visualization", "big data"],
        "roadmap": ["Master Python/R", "Learn advanced stats", "Master SQL", "Learn data cleaning", "Study ML algorithms", "Learn deep learning", "Practice Kaggle"],
        "learning_resources": {"python": "https://www.python.org/", "machine learning": "https://www.coursera.org/learn/machine-learning"}
    },
    
    "machine learning engineer": {
        "required_skills": ["python", "machine learning", "deep learning", "tensorflow", "keras", "scikit-learn", "numpy", "pandas", "statistics", "neural networks"],
        "roadmap": ["Learn Python", "Study Math/Stats", "Learn Scikit-learn", "Study Deep Learning", "Learn TensorFlow", "Work on ML projects", "Publish on GitHub"],
        "learning_resources": {"tensorflow": "https://www.tensorflow.org/learn", "scikit-learn": "https://scikit-learn.org/"}
    },
    
    "python developer": {
        "required_skills": ["python", "django", "flask", "sql", "api", "git", "oop", "data structures", "algorithms", "rest api"],
        "roadmap": ["Master Python", "Learn OOP", "Learn Django/Flask", "Learn SQL", "Build REST APIs", "Practice Data Structures", "Build projects"],
        "learning_resources": {"django": "https://docs.djangoproject.com/", "flask": "https://flask.palletsprojects.com/"}
    },
    
    "web developer": {
        "required_skills": ["html", "css", "javascript", "react", "nodejs", "sql", "git", "api", "bootstrap"],
        "roadmap": ["Learn HTML/CSS", "Learn JavaScript", "Learn React", "Learn backend", "Learn databases", "Build projects", "Deploy apps"],
        "learning_resources": {"react": "https://react.dev/learn", "nodejs": "https://nodejs.org/en/learn"}
    }
}

# ============================================
# DEGREE-SPECIFIC RECOMMENDATIONS (FIXED)
# ============================================

def get_skill_recommendations_by_degree(degree_name):
    """Get complete skill recommendations based on degree - FIXED VERSION"""
    degree_lower = degree_name.lower()
    
    # ========== ARTS & HUMANITIES ==========
    if "ba" in degree_lower and "psychology" in degree_lower:
        return {
            "transferable_skills": ["human behavior", "research methods", "statistics", "empathy", "communication", "active listening", "problem solving", "data analysis", "critical thinking"],
            "recommended_roles": ["ui ux designer", "hr generalist", "product manager", "user researcher", "content writer", "digital marketer", "market researcher"],
            "roadmap": [
                "Your understanding of human behavior is perfect for UX research roles",
                "Learn Figma and design tools to become a UI/UX Designer",
                "Study HR management software for HR Generalist roles",
                "Learn data analysis tools (Excel, SQL) for user research",
                "Build a portfolio with user research case studies"
            ],
            "certifications": ["Google UX Design Certificate", "HRCI Associate Professional in HR", "Nielsen Norman Group UX Certification"]
        }
    
    elif "ba" in degree_lower and "economics" in degree_lower:
        return {
            "transferable_skills": ["econometrics", "statistics", "data analysis", "excel", "critical thinking", "research", "mathematical modeling", "quantitative skills", "forecasting"],
            "recommended_roles": ["data analyst", "business analyst", "financial analyst", "digital marketing analyst", "product manager", "data scientist", "market researcher"],
            "roadmap": [
                "Your econometrics background is powerful for data analyst roles",
                "Learn Python and SQL for advanced data analysis",
                "Master data visualization tools (Tableau, Power BI)",
                "Study machine learning basics for predictive modeling",
                "Build a portfolio of data analysis projects on Kaggle"
            ],
            "certifications": ["Google Data Analytics Certificate", "CFA Investment Foundations", "IBM Data Science Certificate", "Microsoft Power BI Certification"]
        }
    
    elif "ba" in degree_lower and "english" in degree_lower:
        return {
            "transferable_skills": ["writing", "editing", "research", "critical analysis", "storytelling", "grammar", "communication", "attention to detail", "creativity"],
            "recommended_roles": ["content writer", "copywriter", "journalist", "editor", "technical writer", "social media manager", "public relations specialist"],
            "roadmap": [
                "Your writing skills are your superpower: Take content writing courses",
                "Learn SEO and content strategy for digital content roles",
                "Master WordPress and CMS platforms",
                "Build a portfolio of writing samples (blog, articles, social media)",
                "Freelance on platforms like Upwork to gain experience"
            ],
            "certifications": ["HubSpot Content Marketing Certification", "SEO Fundamentals (Moz)", "Google Digital Marketing Certificate", "Technical Writing Certification"]
        }
    
    elif "ba" in degree_lower or "bachelor of arts" in degree_lower:
        return {
            "transferable_skills": ["communication", "writing", "research", "critical thinking", "creativity", "analytical skills", "presentation", "empathy", "storytelling", "adaptability"],
            "recommended_roles": ["content writer", "copywriter", "social media manager", "digital marketer", "journalist", "public relations specialist", "event coordinator", "ui ux designer", "graphic designer", "hr generalist"],
            "roadmap": [
                "Leverage your communication skills: Take content writing and copywriting courses",
                "Learn digital marketing: SEO, Google Analytics, social media marketing",
                "Use your creativity: Learn design tools (Figma, Canva, Adobe Suite)",
                "Build analytical skills: Learn Excel and data analysis basics",
                "Create a portfolio: Start a blog, run social media campaigns, create design projects",
                "Get certified in digital marketing or content strategy"
            ],
            "certifications": ["Google Digital Marketing Certificate", "Google UX Design Certificate", "HubSpot Content Marketing Certification", "Meta Social Media Marketing"]
        }
    
    # ========== FINE ARTS ==========
    elif "bfa" in degree_lower or "fine arts" in degree_lower:
        return {
            "transferable_skills": ["visual design", "creativity", "color theory", "typography", "illustration", "composition", "design thinking", "attention to detail", "art direction"],
            "recommended_roles": ["graphic designer", "ui ux designer", "illustrator", "motion graphics designer", "web designer", "video editor", "photographer", "art director"],
            "roadmap": [
                "Your design foundation is incredible: Master digital design tools",
                "Learn Figma and Adobe Creative Suite (Photoshop, Illustrator, After Effects)",
                "Study UI/UX design principles and user research",
                "Learn basic HTML/CSS for web design roles",
                "Build a strong portfolio on Behance or Dribbble",
                "Freelance on design platforms to gain clients"
            ],
            "certifications": ["Google UX Design Certificate", "Adobe Certified Professional", "Figma UI/UX Design Specialization", "Motion Graphics with After Effects"]
        }
    
    # ========== JOURNALISM ==========
    elif "journalism" in degree_lower or "mass communication" in degree_lower or "bjmc" in degree_lower:
        return {
            "transferable_skills": ["writing", "editing", "research", "storytelling", "interviewing", "media production", "social media", "content creation", "critical analysis", "deadline management"],
            "recommended_roles": ["content writer", "digital marketer", "social media manager", "copywriter", "public relations specialist", "journalist", "video editor", "news anchor"],
            "roadmap": [
                "Your writing and storytelling skills are your superpower",
                "Learn SEO and content strategy for digital media roles",
                "Master social media marketing and analytics tools",
                "Learn Google Analytics and digital marketing platforms",
                "Study video content creation and editing for multimedia roles",
                "Build a portfolio of published work (articles, videos, social campaigns)"
            ],
            "certifications": ["Google Digital Marketing Certificate", "HubSpot Content Marketing Certification", "SEO Fundamentals (Moz)", "Meta Certified Digital Marketing Associate"]
        }
    
    # ========== COMMERCE ==========
    elif "b.com" in degree_lower or "bcom" in degree_lower or "commerce" in degree_lower:
        return {
            "transferable_skills": ["accounting", "finance", "excel", "business acumen", "data analysis", "problem solving", "attention to detail", "statistics", "financial reporting", "taxation"],
            "recommended_roles": ["business analyst", "financial analyst", "accountant", "investment banker", "digital marketing analyst", "marketing coordinator", "sales executive", "project coordinator", "operations manager"],
            "roadmap": [
                "Excel is your superpower: Master pivot tables, VLOOKUP, and Power Query",
                "Learn SQL for data extraction and database management",
                "Study data visualization (Power BI, Tableau) for reporting roles",
                "Learn business analysis and requirements gathering techniques",
                "Get certified in project management or business analytics",
                "Build a portfolio of financial models and business case studies"
            ],
            "certifications": ["Google Data Analytics Certificate", "IIBA ECBA", "CAPM", "Microsoft Power BI Certification", "CFA Investment Foundations"]
        }
    
    # ========== BBA ==========
    elif "bba" in degree_lower or "business administration" in degree_lower:
        return {
            "transferable_skills": ["management", "marketing", "finance", "hr", "communication", "leadership", "teamwork", "business strategy", "presentation", "client management"],
            "recommended_roles": ["business analyst", "product manager", "digital marketer", "hr generalist", "sales executive", "project coordinator", "marketing coordinator", "operations manager", "management consultant"],
            "roadmap": [
                "Your business core is your strength: Add data analysis skills",
                "Learn Excel, SQL, and data visualization tools",
                "Study product management and Agile methodologies",
                "Learn digital marketing analytics and campaign management",
                "Get certified in project management (CAPM, Scrum Master)",
                "Build a portfolio of business cases and marketing campaigns"
            ],
            "certifications": ["Google Project Management Certificate", "Product School PMC", "HubSpot Academy Certifications", "Google Digital Marketing Certificate", "Scrum Master Certification"]
        }
    
    # ========== SCIENCE ==========
    elif "b.sc" in degree_lower and "computer science" in degree_lower:
        return {
            "transferable_skills": ["programming", "algorithms", "data structures", "problem solving", "logical thinking", "mathematics", "database management", "software development"],
            "recommended_roles": ["software engineer", "python developer", "web developer", "data analyst", "database administrator", "full stack developer", "backend developer"],
            "roadmap": [
                "Your CS foundation is solid: Deepen your programming skills",
                "Master a backend framework (Django, Spring Boot, Node.js)",
                "Learn frontend technologies (React, Vue, Angular)",
                "Study cloud platforms and deployment (AWS, Docker)",
                "Build a portfolio of full-stack applications",
                "Contribute to open source projects"
            ],
            "certifications": ["AWS Certified Developer", "Meta Backend Developer Certificate", "Google IT Automation with Python", "Docker Certification"]
        }
    
    elif "b.sc" in degree_lower and "mathematics" in degree_lower:
        return {
            "transferable_skills": ["mathematics", "statistics", "logical reasoning", "problem solving", "analytical thinking", "quantitative analysis", "data modeling"],
            "recommended_roles": ["data analyst", "data scientist", "business analyst", "financial analyst", "quantitative analyst", "machine learning engineer", "actuary"],
            "roadmap": [
                "Your math background is gold for data science roles",
                "Learn Python and data science libraries (Pandas, NumPy, Scikit-learn)",
                "Study machine learning algorithms and statistical modeling",
                "Learn SQL for database management",
                "Build a portfolio of data science projects on Kaggle"
            ],
            "certifications": ["IBM Data Science Certificate", "Google Advanced Data Analytics", "TensorFlow Developer Certificate", "SAS Certification"]
        }
    
    elif "b.sc" in degree_lower and "statistics" in degree_lower:
        return {
            "transferable_skills": ["statistics", "probability", "data analysis", "mathematics", "research methodology", "analytical thinking", "quantitative analysis", "hypothesis testing"],
            "recommended_roles": ["data analyst", "data scientist", "business analyst", "statistician", "market researcher", "risk analyst", "quantitative analyst"],
            "roadmap": [
                "Your statistics background is perfect for data roles",
                "Learn Python, R, and statistical analysis libraries",
                "Master SQL for data extraction",
                "Learn data visualization (Tableau, Power BI, Matplotlib)",
                "Study machine learning algorithms",
                "Build a portfolio of statistical analysis projects"
            ],
            "certifications": ["Google Data Analytics Certificate", "IBM Data Science Certificate", "SAS Statistical Business Analyst", "Microsoft Power BI Certification"]
        }
    
    elif "b.sc" in degree_lower or "bsc" in degree_lower:
        return {
            "transferable_skills": ["mathematics", "statistics", "analytical thinking", "research methodology", "problem solving", "data analysis", "logical reasoning", "scientific method"],
            "recommended_roles": ["data analyst", "data scientist", "business analyst", "python developer", "market researcher", "research analyst"],
            "roadmap": [
                "Your analytical skills are valuable for data roles",
                "Learn Python and data science libraries (Pandas, NumPy)",
                "Master SQL for database querying",
                "Learn data visualization tools (Tableau, Power BI)",
                "Study statistics and machine learning basics",
                "Build a portfolio of data analysis projects"
            ],
            "certifications": ["Google Data Analytics Certificate", "IBM Data Science Certificate", "Python for Data Science (IBM)"]
        }
    
    # ========== BCA ==========
    elif "bca" in degree_lower or "computer applications" in degree_lower:
        return {
            "transferable_skills": ["programming", "database management", "web development", "software engineering", "algorithms", "data structures", "problem solving", "logical thinking", "it fundamentals"],
            "recommended_roles": ["python developer", "web developer", "frontend developer", "android developer", "ios developer", "devops engineer", "data analyst", "software engineer", "database administrator", "full stack developer"],
            "roadmap": [
                "Your coding foundation is solid: Master backend frameworks (Django, Spring Boot)",
                "Add modern frontend skills: React, Vue, or Angular",
                "Learn mobile development (Kotlin for Android, Swift for iOS)",
                "Study cloud platforms and DevOps (AWS, Docker, Kubernetes)",
                "Learn data science libraries for data analyst roles",
                "Build a portfolio of full-stack applications and contribute to open source"
            ],
            "certifications": ["Meta Backend Developer Certificate", "AWS Certified Developer", "Google IT Automation with Python", "IBM Full Stack Developer", "Docker Certification"]
        }
    
    # ========== ENGINEERING ==========
    elif "b.tech" in degree_lower or "be" in degree_lower and "computer" in degree_lower:
        return {
            "transferable_skills": ["engineering mathematics", "programming", "data structures", "algorithms", "system design", "problem solving", "project management", "technical documentation", "software architecture"],
            "recommended_roles": ["software engineer", "data scientist", "machine learning engineer", "cloud engineer", "devops engineer", "ai engineer", "backend developer", "full stack developer", "cybersecurity analyst", "data engineer", "site reliability engineer"],
            "roadmap": [
                "Your engineering mindset is your biggest asset for tech roles",
                "Master system design and software architecture",
                "Deep dive into AI/ML using your strong math foundation",
                "Learn cloud platforms (AWS, Azure, GCP) and DevOps tools",
                "Study data engineering and big data technologies",
                "Build scalable systems and contribute to open source",
                "LeetCode and system design interview prep for top companies"
            ],
            "certifications": ["AWS Solutions Architect", "Google Professional ML Engineer", "DeepLearning.AI TensorFlow Developer", "Kubernetes Certification", "System Design Interview Prep"]
        }
    
    elif "b.tech" in degree_lower or "be" in degree_lower or "engineering" in degree_lower:
        return {
            "transferable_skills": ["engineering mathematics", "programming", "data structures", "algorithms", "system design", "problem solving", "project management", "technical documentation", "analytical thinking"],
            "recommended_roles": ["software engineer", "data scientist", "machine learning engineer", "cloud engineer", "devops engineer", "backend developer", "full stack developer", "embedded engineer", "cybersecurity analyst"],
            "roadmap": [
                "Your engineering mindset is your biggest asset",
                "Master data structures and algorithms for software roles",
                "Deep dive into AI/ML using your math foundation",
                "Learn cloud platforms (AWS, Azure, GCP)",
                "Study DevOps and infrastructure as code",
                "Build a portfolio of projects and contribute to open source",
                "Practice LeetCode for technical interviews"
            ],
            "certifications": ["AWS Solutions Architect", "Google Professional ML Engineer", "DeepLearning.AI TensorFlow Developer", "Kubernetes Certification", "System Design Interview Prep"]
        }
    
    # ========== DEFAULT ==========
    else:
        return {
            "transferable_skills": ["communication", "problem solving", "analytical thinking", "teamwork", "time management", "adaptability", "critical thinking", "organization", "leadership"],
            "recommended_roles": ["business analyst", "digital marketer", "content writer", "data analyst", "project coordinator", "sales executive", "hr generalist", "marketing coordinator", "customer success"],
            "roadmap": [
                "Identify your core strengths and skills from your background",
                "Add digital skills relevant to your interests (Excel, data analysis, design, marketing)",
                "Take online courses to bridge skill gaps (Coursera, Udemy, LinkedIn Learning)",
                "Build a portfolio of practical projects in your chosen field",
                "Network with professionals in your target industry on LinkedIn",
                "Start with internships or entry-level positions to gain hands-on experience",
                "Get certified in your chosen career path"
            ],
            "certifications": ["Google Career Certificates", "HubSpot Academy Courses", "LinkedIn Learning Paths", "Coursera Professional Certificates", "Microsoft Learn"]
        }