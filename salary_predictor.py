def predict_salary(title, experience=2, location='India'):
    base_salaries = {
    'QA Engineer': 500000,
    'Software Engineer': 600000,
    'Data Analyst': 550000,
    'DevOps Engineer': 700000,
    'Frontend Developer': 580000,
    'Mobile App Developer': 650000,
    'Backend Engineer': 650000,
    'Machine Learning Engineer': 900000,
    'Full Stack Developer': 700000,
    'Data Scientist': 850000,
    'Cybersecurity Analyst': 600000,
    'Cloud Architect': 950000,
    'AI Researcher': 900000,
    'UI/UX Designer': 500000,
    'Business Analyst': 600000,
    'Database Administrator': 670000,
    'Systems Analyst': 700000,
    'Product Manager': 1500000,
    'Network Engineer': 600000,
    'Blockchain Developer': 800000,
    'Computer Vision Engineer': 900000,
    'NLP Engineer': 900000,
    'Game Developer': 600000,
    'Embedded Systems Engineer': 600000,
    'Robotics Engineer': 700000,
    'AR/VR Developer': 650000,
    'Big Data Engineer': 850000,
    'Site Reliability Engineer': 900000,
    'Computer Graphics Developer': 600000,
    'Quantum Computing Researcher': 900000,
    'Bioinformatics Specialist': 650000,
    'IT Support Specialist': 400000,
    'CRM Developer': 500000,
    'E-commerce Developer': 550000,
    'Tech Support Engineer': 450000,
    'VR/AR Researcher': 650000,
    'Ethical Hacker': 750000,
    'Firmware Engineer': 650000,
    'Security Engineer': 850000,
    'Research Scientist': 900000
}

    multiplier = 1.2 if location.lower() == 'bangalore' else 1.0
    return base_salaries.get(title, 500000) * (1 + 0.1 * experience) * multiplier
