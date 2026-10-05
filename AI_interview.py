import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Interview Question Generator",
    page_icon="🎯",
    layout="centered"
)

# Title
st.title("🎯 AI Interview Question Generator")
st.write("Generate interview questions, answers, and follow-up questions for any technology.")

# Model
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Prompt Template
prompt = PromptTemplate(
    template="""
I am preparing for an interview on {technology} and would like to practice questions at the {difficulty} level.

Generate exactly 5 interview questions.

Use this format strictly:

QUESTION:
<question>

ANSWER:
<answer>

FOLLOWUP:
<followup>

===

Repeat for all 5 questions.
""",
    input_variables=["technology", "difficulty"]
)

# Inputs
col1, col2 = st.columns(2)

with col1:
    technology = st.text_input(
        "💻 Technology",
        placeholder="e.g. Python, Java, SQL, Machine Learning"
    )

with col2:
    difficulty = st.selectbox(
        "📊 Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
            "Expert"
        ]
    )

# Generate Button
if st.button("🚀 Generate Questions", use_container_width=True):

    if not technology:
        st.warning("Please enter a technology.")
    else:
        with st.spinner("Generating Interview Questions..."):

            formatted_prompt = prompt.invoke({
                "technology": technology,
                "difficulty": difficulty
            })

            result = model.invoke(formatted_prompt)

        import re

        st.success("Questions Generated Successfully!")

        blocks = result.content.split("===")

        for i, block in enumerate(blocks):

            block = block.strip()

            if not block:
                continue

            try:
                question = re.search(
                    r"QUESTION:(.*?)ANSWER:",
                    block,
                    re.DOTALL
                ).group(1).strip()

                answer = re.search(
                    r"ANSWER:(.*?)FOLLOWUP:",
                    block,
                    re.DOTALL
                ).group(1).strip()

                followup = re.search(
                    r"FOLLOWUP:(.*)",
                    block,
                    re.DOTALL
                ).group(1).strip()

                with st.container(border=True):

                    st.subheader(f"🎯 Question {i+1}")

                    st.info(question)

                    with st.expander("✅ View Ideal Answer"):
                        st.write(answer)

                    with st.expander("🔄 View Follow-up Question"):
                        st.write(followup)

            except:
                st.write(block)

        st.download_button(
            label="📥 Download Questions",
            data=result.content,
            file_name=f"{technology}_interview_questions.txt",
            mime="text/plain"
        )