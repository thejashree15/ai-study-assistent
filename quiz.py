def generate_quiz(text):
    sentences = text.split(".")
    questions = []

    for s in sentences:
        s = s.strip()

        # skip empty or very small sentences
        if len(s) > 20:
            questions.append(f"What is meant by: {s}?")

        # limit to 10 questions
        if len(questions) == 10:
            break

    return questions