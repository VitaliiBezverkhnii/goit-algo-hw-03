import random

def get_numbers_ticket(min, max, quantity):
    """
    Generates a sorted list of unique random numbers within a specified range.

    Parameters:
        min (int): The minimum number in the range (inclusive).
        max (int): The maximum number in the range (inclusive).
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list: A sorted list of unique random numbers.
    """
    if not all(isinstance(arg, int) for arg in [min, max, quantity]):
        print("All input parameters must be integers.")
        return []
    
    if min < 1:
        print("min не може бути менше 1")
        return []
    
    if max > 1000:
        print("max не може бути більше 1000")
        return []
    
    if quantity > (max - min + 1):
        print("Quantity перевищує кількість цифр в діапазоні між min та max")
        return []
    
    uniq_numbers = set()
    while len(uniq_numbers) < quantity:
        random_number = random.randint(min, max)
        uniq_numbers.add(random_number)
    
    sorted_list = sorted(uniq_numbers)
    return sorted_list

numbers = get_numbers_ticket(100, 118,  19)
print(numbers)