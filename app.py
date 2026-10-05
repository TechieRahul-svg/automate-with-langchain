import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered"
)

# Model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1.0
)

# Prompt
prompt = PromptTemplate(
    template="""
You are a world-class LinkedIn content creator, storyteller, and personal branding strategist.

Your task is to create a highly engaging LinkedIn post.

Topic: {topic}
Target Audience: {audience}
Tone: {tone}

Guidelines:
1. Begin with a strong attention-grabbing hook.
2. Write in a natural, authentic, and human-like style.
3. Make the content insightful and valuable for the target audience.
4. Use short paragraphs for readability.
5. Include a key lesson, insight, or takeaway.
6. Avoid generic or robotic language.
7. End with a question that encourages discussion and engagement.
8. Generate relevant hashtags.
9. Generate a compelling call-to-action.

Return the response in the following format:

🚀 LinkedIn Post:
<post>

📌 Key Takeaway:
<takeaway>

🏷️ Hashtags:
<5 hashtags>

💬 Call To Action:
<cta>
""",
    input_variables=["topic", "audience", "tone"]
)

# Title
st.title("💼 LinkedIn Post Generator")
st.write("Generate engaging LinkedIn posts using AI.")

# Inputs
topic = st.text_input(
    "📌 Topic",
    placeholder="e.g. Future of Artificial Intelligence"
)

audience = st.text_input(
    "👥 Target Audience",
    placeholder="e.g. Students, Developers, Recruiters"
)

tone = st.selectbox(
    "🎭 Tone",
    [
        "Professional",
        "Motivational",
        "Inspirational",
        "Friendly"
    ]
)

# Generate Button
if st.button("🚀 Generate LinkedIn Post", use_container_width=True):

    if not topic or not audience:
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Generating post..."):

            formatted_prompt = prompt.invoke({
                "topic": topic,
                "audience": audience,
                "tone": tone
            })

            result = model.invoke(formatted_prompt)

        st.success("Post Generated Successfully!")

        st.text_area(
            "Generated LinkedIn Post",
            value=result.content,
            height=500
        )