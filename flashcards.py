def generate_flashcards(text):
    sentences = text.split(".")
    cards = []

    for s in sentences:
        s = s.strip()

        if len(s) > 20:
            cards.append({
                "front": s,
                "back": "Explanation: " + s
            })

        if len(cards) == 5:   # 5 flashcards
            break

    return cards