from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile"
)

print("Paste your resume below (type END on a new line when finished):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

resume_text = "\n".join(lines)
prompt=PromptTemplate(
    template="""
    Analyze the following resume carefully and provide a detailed evalution.
    Resume:
    {resume_text}

    Instructions:
    1. Read the resume thoroughly.
    2. Identify the candidate's education, skills, projects, work experience, certifications, and achievements.
    3. Provide a concise professional summary of the candidate.
    4. Highlight the key strengths that make the candidate a strong applicant.
    5. Identify weaknesses, missing information, or areas that may reduce the candidate's chances of selection.
    6. Suggest practical improvements to make the resume more effective and ATS-friendly.
    7. Base your analysis only on the information present in the resume.

    Return the response in the following format:

    Resume Summary:
    - A concise 3-5 sentence summary of the candidate's profile.

    Strengths:

    Weaknesses:
    
    Improvements:
    """,
        input_variables=["resume_text"]
)

formated_prompt=prompt.invoke(
    {"resume_text": resume_text}
)

result=model.invoke(formated_prompt)
print(result.content)