def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == -1:
            break

        numbers.append(number)

    for number in numbers:
        print(number)

if __name__ == '__main__':
    main()
