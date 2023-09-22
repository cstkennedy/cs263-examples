def main():
    integer_1 = input("Enter an integer: ")
    integer_1 = int(integer_1)

    integer_2 = input("Enter an integer: ")
    integer_2 = int(integer_2)

    integer_sum = integer_1 + integer_2
    print(f"{integer_1} + {integer_2} = {integer_sum}")

    integer_difference = integer_1 - integer_2
    print(f"{integer_1} - {integer_2} = {integer_difference}")

    integer_product = integer_1 * integer_2
    print(f"{integer_1} * {integer_2} = {integer_product}")

    integer_quotient = integer_1 / integer_2
    print(f"{integer_1} / {integer_2} = {integer_quotient}")

    integer_quotient = integer_1 // integer_2
    print(f"{integer_1} // {integer_2} = {integer_quotient}")

    integer_modulus = integer_1 % integer_2
    print(f"{integer_1} % {integer_2} = {integer_modulus}")


if __name__ == "__main__":
    main()
