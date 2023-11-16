def main():

    try:
        raw_string = input("Enter a year: ")
        year = int(raw_string)

    except:
        print(f'"{raw_string}" is not a valid year')


if __name__ == "__main__":
    main()
