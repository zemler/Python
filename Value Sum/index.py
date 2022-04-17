
def main():
    temp = liczba
    sum = 0
    while temp != 0:
        r = int(temp % 10)
        sum = int(sum + r)
        temp = int(temp/10)
    print(sum)


if __name__ == "__main__":
    liczba = int(input("Give me num: "))
    main()