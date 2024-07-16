import random

# edit this list - get more from Chat GPT
words = [
    {"malay": "rumah", "english": "house"},
    {"malay": "kereta", "english": "car"},
    {"malay": "umur", "english": "age"},
    {"malay": "kuat", "english": "strong"},
    {"malay": "sihat", "english": "healthy"},
    {"malay": "sakit", "english": "sick"},
    {"malay": "satu", "english": "one"},
    {"malay": "dua", "english": "two"},
    {"malay": "manusia", "english": "human"},
    {"malay": "haiwan", "english": "animal"},
    {"malay": "manis", "english": "sweet"},
    {"malay": "masam", "english": "sour"},
    {"malay": "tanah", "english": "land"},
    {"malay": "bumi", "english": "earth"},
    {"malay": "hitam", "english": "black"},
    {"malay": "sekolah", "english": "school"},
    {"malay": "lebuhraya", "english": "highway"},
    {"malay": "lampu", "english": "lamp"},
    {"malay": "nasi", "english": "rice"},
    {"malay": "kolam", "english": "pool"},
]


def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['malay']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()