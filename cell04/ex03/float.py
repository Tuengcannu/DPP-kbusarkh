def main():
    try:
        user_input = input("Give me a number: ")
        num = float(user_input)
       
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        pass

if __name__ == "__main__":
    main()