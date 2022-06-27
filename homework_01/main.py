"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    
    return [num ** 2 for num in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def prime_number(num):
    if num > 1:
        if num == 2: return True
        for item in range(2, num):
            if num % item == 0 and num != item:
                return False
        return True
    else:
        return False

def even_number(num):
    if num % 2 == 0:
        return True
    return False

def odd_number(num):
    if even_number(num):
        return False
    return True


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == PRIME:
        return list(filter(prime_number, numbers_list))
    if filter_type == ODD:
        return list(filter(odd_number, numbers_list))
    if filter_type == EVEN:
        return list(filter(even_number, numbers_list))
    else:
        return False