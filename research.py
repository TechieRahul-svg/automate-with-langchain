import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Research Paper Summary Generator",
    page_icon="📚",
    layout="centered"
)

# Title
st.title("📚 Research Paper Summary Generator")
st.write("Generate AI-powered summaries of research papers in different explanation styles.")

# Model
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Prompt Template
prompt = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_title}" in {explanation_type} style.

The output should include:

1. Summary
2. Key Contributions
3. Applications
4. Future Scope

Explanation Style:
- Beginner: Use simple language.
- Technical: Use detailed technical explanations.
- Bullet Points: Use concise bullet points.

If certain information is not available in the paper, respond with:
"Insufficient information available"

Ensure the summary is clear, accurate, and aligned with the requested style.
""",
    input_variables=["paper_title", "explanation_type"]
)

# Chain
chain = prompt | model

# Input Section
paper_title = st.text_input(
    "📄 Research Paper Title",
    placeholder="e.g. Attention Is All You Need"
)

explanation_type = st.radio(
    "📖 Choose Explanation Style",
    [
        "Beginner",
        "Technical",
        "Bullet Points"
    ],
    horizontal=True
)

# Generate Button
if st.button("🚀 Generate Summary", use_container_width=True):

    if not paper_title:
        st.warning("Please enter a research paper title.")
    else:
        with st.spinner("Generating Summary..."):

            result = chain.invoke(
                {
                    "paper_title": paper_title,
                    "explanation_type": explanation_type
                }
            )

        st.success("Summary Generated Successfully!")

        st.text_area(
            "Generated Summary",
            value=result.content,
            height=500
        )

        # Download Button
        st.download_button(
            label="📥 Download Summary",
            data=result.content,
            file_name=f"{paper_title}_summary.txt",
            mime="text/plain"
        )