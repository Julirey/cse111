
statements = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.",
            "I am able to do things as well as most other people.", "I feel I do not have much to be proud of.", "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.",
            "I wish I could have more respect for myself.", "I certainly feel useless at times.","At times I think I am no good at all." ]


def main():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print("")    
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score_total = 0

    for i in range(len(statements)):
        print(f"{i + 1}. {statements[i]}")
        response = input("   Enter D, d, a, or A: ")
        if i + 1 == 1 or i + 1 == 2 or i + 1 == 4 or i + 1 == 6 or i + 1 == 7:
            score = compute_score_positive(response)
            score_total += score
        else:
            score = compute_score_negative(response)
            score_total += score
    print()
    print(f"Your score is {score_total}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def compute_score_positive(response):
    if response == "D":
        return 0
    elif response == "d":
        return 1
    elif response == "a":
        return 2
    elif response == "A":
        return 3
    
def compute_score_negative(response):
    if response == "D":
        return 3
    elif response == "d": 
        return 2
    elif response == "a": 
        return 1
    elif response == "A":
        return 0
    
main()
