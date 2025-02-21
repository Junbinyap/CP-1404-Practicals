import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick(MIN_NUMBER, MAX_NUMBER, NUMBERS_PER_PICK)
        # Format each number to ensure proper alignment
        print(" ".join(f"{num:2}" for num in quick_pick))

def generate_quick_pick(MIN_NUMBER, MAX_NUMBER, NUMBERS_PER_PICK):
    """Generate a sorted list of 6 unique random numbers."""
    quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)
    quick_pick.sort()
    return quick_pick

main()