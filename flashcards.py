def generate_flashcards(text):
    sentences = text.split(".")
    cards = []

    for s in sentences:
        s = s.strip()

        if len(s) > 20:
            parts = s.split("is")

            if len(parts) > 1:
                front = parts[0]
                back = "is".join(parts[1:])
            else:
                front = s
                back = "Explanation: " + s

            cards.append({
                "front": front,
                "back": back
            })

        if len(cards) == 5:
            break

    return cards