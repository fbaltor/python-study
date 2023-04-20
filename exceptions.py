while True:
    try:
        x = int(input("Please enter a integer: "))
        break
    except BaseException:
        print("Oooops!")
        break
