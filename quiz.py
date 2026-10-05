import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load Environment Variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Quiz Generator",
    page_icon="📝",
    layout="centered"
)

# Title
st.title("📝 AI Quiz Generator")
st.write("Generate MCQ quizzes on any topic using AI.")

# LLM Model
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Prompt Template
prompt = PromptTemplate(
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

# Input Section
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input(
        "📚 Topic",
        placeholder="e.g. Python, Machine Learning"
    )

with col2:
    difficulty = st.selectbox(
        "⚡ Difficulty",
        ["Easy", "Medium", "Hard", "Expert"]
    )

num_questions = st.slider(
    "🔢 Number of Questions",
    min_value=1,
    max_value=20,
    value=5
)

# Generate Button
if st.button("🎯 Generate Quiz", use_container_width=True):

    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating Quiz..."):

            formatted_prompt = prompt.invoke({
                "topic": topic,
                "num_questions": num_questions,
                "difficulty": difficulty
            })

            result = model.invoke(formatted_prompt)

        st.success("Quiz Generated Successfully!")

        st.text_area(
            "Generated Quiz",
            value=result.content,
            height=600
        )

        # Download Button
        st.download_button(
            label="📥 Download Quiz",
            data=result.content,
            file_name=f"{topic}_quiz.txt",
            mime="text/plain"
        )