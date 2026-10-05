from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1.0
)

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
topic = input("Enter Topic: ")
audience = input("Enter Target Audience: ")
tone = input("Enter Tone (Professional/Motivational/Inspirational/Friendly): ")

formated_prompt=prompt.invoke({
    'topic':topic,
    'audience':audience,
    'tone':tone
})

result=model.invoke(formated_prompt)

print(result.content)