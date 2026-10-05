from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.9
)

prompt = PromptTemplate(
    template="""
You are an expert communication coach and professional email writer.

Write a high-quality email based on the following details:

Purpose: {purpose}
Recipient: {recipient}
Tone: {tone}

Requirements:
- Write like a real person, not a template or AI.
- Make the email natural, engaging, and easy to read.
- Adapt the writing style to match the requested tone.
- Clearly communicate the purpose of the email.
- Use a strong and relevant subject line.
- Include a warm and appropriate greeting.
- Keep the content concise while providing enough detail.
- Use smooth transitions and professional language.
- End with a thoughtful and professional closing.
- Avoid generic phrases and repetitive wording.

The email should feel authentic, polished, and ready to send.

Return only the complete email with:
1. Subject
2. Greeting
3. Email Body
4. Closing
""",
    input_variables=["purpose", "recipient", "tone"]
)

Purpose=input("Enter the purpose of the Email: ")
Recipient=input("Enter the recipient: ")
Tone=input("Enter the tone:")

formated_prompt=prompt.invoke({
    'purpose':Purpose,
    'recipient':Recipient,
    'tone':Tone
})

result=model.invoke(formated_prompt)
print(result.content)