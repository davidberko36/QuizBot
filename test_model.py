from model import AnswerVerifier

verifier = AnswerVerifier()

test_cases = [
    ("Paris is the capital of France.", "The capital of France is Paris."),
    ("Water boils at 100 degrees Celsius.", "At 100°C, water starts to boil."),
    ("The sun rises in the east.", "The west is where the sun rises."),
]

for correct, user in test_cases:
    is_correct, score, = verifier.verify_answer(correct, user)
    result = "Correct" if is_correct else "Wrong"
    print(f"user's answer: {user}")
    print(f"similarity score: {score:.2f} -> {result}\n")