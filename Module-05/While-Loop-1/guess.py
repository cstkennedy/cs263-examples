def get_next_guess(lower_limit, upper_limit) -> int:
    return lower_limit + (upper_limit - lower_limit) // 2


def main():
    lower_limit = 1
    upper_limit = 100

    answer = "n"
    while answer != "y":
        guess = get_next_guess(lower_limit, upper_limit)

        answer = input(f"Is your number {guess}? (y/n): ")
        answer = answer.lower()[0]

        if answer == "y":
            print("I win!")

        elif answer == "n":
            answer = input("Was my guess too high or too low? (h/l): ")
            answer = answer.lower()[0]

            if answer == "h":
                upper_limit = guess

            elif answer == "l":
                lower_limit = guess


if __name__ == "__main__":
    main()
