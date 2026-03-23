from langchain_openai import ChatOpenAI

# -------- BASIC QUIZ --------
def basic_quiz(text):
    sentences = text.split(".")
    questions = []

    for s in sentences:
        s = s.strip()
        if len(s) > 20:
            questions.append(f"What is meant by: {s}?")

        if len(questions) == 10:
            break

    return questions


# -------- AI QUIZ --------
def ai_quiz(text):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    prompt = f"""
    Generate 10 important study questions from the following content:

    {text[:1500]}

    Rules:
    - Questions should be clear and short
    - Do not include answers
    - Number the questions
    """

    response = llm.invoke(prompt)

    questions = response.content.split("\n")
    questions = [q.strip() for q in questions if q.strip() != ""]

    return questions


# -------- MAIN FUNCTION --------
def generate_quiz(text):
    try:
        return ai_quiz(text)
    except Exception as e:
        print("AI failed, using basic quiz:", e)
        return basic_quiz(text)