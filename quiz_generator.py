from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile"
)
prompt=PromptTemplate(
    template="""
    Create {num_questions} multiple-choice questions on {topic} at a {difficulty} difficulty level.

    For each question provide:
    - Question
    - Four options (A, B, C, D)
    - Correct Answer
    - Brief Explanation

    Keep the questions accurate, engaging, and appropriate for the difficulty level.
    """,
    input_variables=["topic", "num_questions", "difficulty"]
)

num=int(input("Enter the no. of question you want:"))
topic=input("Enter the topic:")
difficulty=input("Enter the difficulty level:")

formated_prompt=prompt.invoke({
    'topic':topic,
    'num_questions':num,
    'difficulty':difficulty
})

result=model.invoke(formated_prompt)

print(result.content)