import random


def read_numbers(n: int) -> list:
    return [random.randint(1,100)for _ in range(n)]


def show(numbers:list) -> None:
    for number in numbers:
        print(number,end=' ')
    print()



# wymagane !!!
def buble_sort(numbers:list) -> list:

    for j in range(len(numbers)-1):
        for i in range(len(numbers)-1-j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    show(numbers)

def selection_sort(numbers:list) -> list:
    for j in range(len(numbers)-1):
        p = j
        for i in range(j+1,len(numbers)):
            if numbers[i] < numbers[p]:
                p=i
        numbers[p], numbers[j] = numbers[j], numbers[p]
    show(numbers)
# ---------------------------------------------------------------------------------


def wstawianie(numbers:list) -> list:
    for j in range(len(numbers)-2, -1, -1):
        x = numbers[j]
        i = j+1
        while i < len(numbers) and x > numbers[i]:
            numbers[i-1] = numbers[i]
            i = i + 1
        numbers[i-1] = x
    return numbers






if __name__ == "__main__":
    numbers = read_numbers(30)
    print("przed sortowaniem")
    show(numbers)
    print("po sortowamiu bombelkowym")
    buble_sort(numbers[:])
    print("po sortowamiu tym drugim")
    selection_sort(numbers[:])
    print("po wstawiania")
    show(wstawianie(numbers[:]))