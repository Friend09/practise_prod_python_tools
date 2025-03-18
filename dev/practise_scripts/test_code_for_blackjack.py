def card_score(cards):
    if len(cards) < 2:
        raise ValueError("At least two cards are required")
    if not isinstance(cards, str):
        raise ValueError("cards must be a string")
    numbers = [c for c in cards if c in "23456789"]
    print("numbers", numbers)
    faces = [c for c in cards if c in "JQK"]
    print("faces", faces)
    n_aces = sum([1 for c in cards if c == "A"])
    print("n_aces", n_aces)
    score = sum([int(i) for i in numbers]) + len(faces) * 10
    print("score", score)
    while n_aces > 0:
        score += 1 if score + 11 > 21 else 11
        print("score", score)
        n_aces -= 1
    return score if score <= 21 else 0


if __name__ == "__main__":
    print(card_score("23A"))
