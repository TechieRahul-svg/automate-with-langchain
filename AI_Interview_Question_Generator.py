from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt=PromptTemplate(
    template="""
        I am preparing for an interview on {technology} and would like to practice questions at the {difficulty} level.

        Act as an experienced technical interviewer and generate 5 interview questions that are commonly asked in real interviews.

        For each question, provide:
        - The interview question
        - A clear and concise ideal answer
        - A follow-up question that an interviewer might ask to explore the topic further

        Make sure the questions are appropriate for the selected difficulty level and cover important concepts related to {technology}.

        Keep the answers practical, easy to understand, and useful for interview preparation.

        Present the response in a clear and organized format.

    """
)

technology=input("Enter the technology:")
difficulty=input("Enter the difficulty level:")

formated_prompt=prompt.invoke({
    'technology':technology,
    'difficulty':difficulty
})
result=model.invoke(formated_prompt)
print(result.content)