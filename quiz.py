from openai import OpenAI

def generate_quiz(text, client):
    try:
        prompt = f"""
        You are a helpful teacher.

        From the following study material, create 5 quiz questions with answers.

        Format:
        Q1: Question
        Answer: ...

        Text:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a quiz generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        quiz = response.choices[0].message.content
        return quiz

    except Exception as e:
        return f"Error generating quiz: {e}"