def main():
    integer_1 = input("Enter an integer: ")
    integer_1 = int(integer_1)

    integer_2 = input("Enter an integer: ")
    integer_2 = int(integer_2)

    print(f"{integer_1} + {integer_2} = {integer_1 + integer_2}")
    print(f"{integer_1} - {integer_2} = {integer_1 - integer_2}")
    print(f"{integer_1} * {integer_2} = {integer_1 * integer_2}")
    print(f"{integer_1} / {integer_2} = {integer_1 / integer_2}")
    print(f"{integer_1} // {integer_2} = {integer_1 // integer_2}")
    print(f"{integer_1} % {integer_2} = {integer_1 % integer_2}")
    print(f"{integer_1} ** {integer_2} = {integer_1 ** integer_2}")


if __name__ == "__main__":
    main()
