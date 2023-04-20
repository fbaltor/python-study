def main():
    y = int(input("Input 2 for error: "))
    try:
        x = "I can access x"
        if y == 2:
            raise Exception()
    except BaseException:
        print("Ooooops!")

    print(x)

main()
