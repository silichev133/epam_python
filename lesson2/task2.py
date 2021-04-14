while True:
    input_string = input('Enter string (type "x" for exit): ')
    if input_string == "x":
        print("Exit")
        break
    elif input_string == input_string[::-1]:
        print("This is polindrome")
    elif input_string != input_string[::-1]:
        print("this is not polindrome")

    
