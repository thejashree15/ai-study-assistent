from openai import OpenAI

def generate_flashcards(text, client):
    try:
        prompt = f"""
        You are a helpful study assistant.

        From the following text, create 5 flashcards.

        Format:
        Front: Question
        Back: Answer

        Text:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a flashcard generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        flashcards = response.choices[0].message.content
        return flashcards

    except Exception as e:
        return f"Error generating flashcards: {e}"