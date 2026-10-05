from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = PromptTemplate(
    template="""
    Please summarize the research paper titled  "{paper_title}" in {explanation_type} style.

    The output include:
    1. Summary
    2. Key Contributions
    3. Applications
    4. Future Scope

    Explanation style:
    - Beginner: Use simple language.
    - Technical: Use detailed technical explanations.
    - Bullet Points: Use concise bullet points.

    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

    Ensure the summary is clear, accurate, and aligned with the provided style and length.
""")

chain = prompt | model

paper_title = input("Enter Research Paper Title: ")

print("\nChoose Explanation Type:")
print("1. Beginner")
print("2. Technical")
print("3. Bullet Points")

choice = input("\nEnter your choice (1/2/3): ")

if choice == "1":
    explanation_type = "Beginner"
elif choice == "2":
    explanation_type = "Technical"
elif choice == "3":
    explanation_type = "Bullet Points"
else:
    print("Invalid choice. Defaulting to Beginner.")
    explanation_type = "Beginner"

result = chain.invoke(
    {
        "paper_title": paper_title,
        "explanation_type": explanation_type
    }
)

print(result.content)