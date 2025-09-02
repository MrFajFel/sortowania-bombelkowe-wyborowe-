import random


def read_numbers(n: int) -> list:
    return [random.randint(1,100)for _ in range(n)]


def show(numbers:list) -> None:
    for number in numbers:
        print(number,end=' ')
    print()

def buble_sort(numbers:list) -> list:

    for j in range(len(numbers)-1):
        for i in range(len(numbers)-1-j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    show(numbers)

def schemat_wyborowy(numbers:list) -> list:
    for j in range(len(numbers)-1):
        p = j
        for i in range(j+1,len(numbers)):
            if numbers[i] < numbers[p]:
                p=i
        numbers[p], numbers[j] = numbers[j], numbers[p]
    show(numbers)




if __name__ == "__main__":
    numbers = read_numbers(30)
    print("przed sortowaniem")
    show(numbers)
    # print("po sortowamiu bombelkowym")
    # buble_sort(numbers)
    print("po sortowamiu tym drugim")
    schemat_wyborowy(numbers)