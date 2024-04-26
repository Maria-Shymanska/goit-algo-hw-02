from collections import deque

def is_palindrome(string):
    string = string.lower().replace(" ", "")  # Перетворюємо у нижній регістр та видаляємо пробіли
    char_deque = deque(string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Приклади рядків для перевірки
strings_to_check = ["Panama", "Cat", "Python", "Madam"]

for string in strings_to_check:
    if is_palindrome(string):
        print(f"{string} є паліндромом.")
    else:
        print(f"{string} не є паліндромом.")
