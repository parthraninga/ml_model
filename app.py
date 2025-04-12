import fitz  # PyMuPDF
from resume_parser import extract_skills
from matcher import recommend_jobs
from salary_predictor import predict_salary

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def main():
    # 🔼 Provide the path to the uploaded resume PDF
    pdf_path = "data/resume.pdf"  
    resume_text = extract_text_from_pdf(pdf_path)
    # print(resume_text)
    print("\n📄 Extracting skills...")
    user_skills = extract_skills(resume_text)
    print("✅ Found skills:", user_skills)

    print("\n💼 Matching jobs...")
    matches = recommend_jobs(user_skills)
    print(matches)

    print("\n💰 Salary Estimates:")
    for _, row in matches.iterrows():
        salary = predict_salary(row['title'])
        print(f"{row['title']}: ₹{int(salary):,}/year")

if __name__ == "__main__":
    main()
