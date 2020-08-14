def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


print(factorial(10))


def sum_of_square(n: int):
    if n < 2:
        return 1
    else:
        return n ** 2 + sum_of_square(n - 1)


print(sum_of_square(10))


def process_text(text: str):
    lst = text.split(' ', 1)
    text1 = lst[1]
    text2 = ''
    for letter in text1:
        if not ((ord(letter) >= 97) and (ord(letter) <= 122)):
            text2 = text1.replace(letter, '_')
            text1 = text2

    lst[1] = text2
    return tuple(lst)


print(process_text('1234567a Text de te5t'))
