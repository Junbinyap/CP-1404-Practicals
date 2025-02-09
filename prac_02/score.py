import random

def main():
    """main function"""
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    """The random number"""
    random_score = random.randint(0, 100)
    random_result = evaluate_score(random_score)
    print(f"Random score: {random_score:.2f}, Result: {random_result}")


def evaluate_score(score):
    """Evaluate the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"

main()
