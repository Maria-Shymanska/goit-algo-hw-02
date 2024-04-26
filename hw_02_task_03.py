class BracketBalancer:
    @staticmethod
    def is_balanced(string):
        stack = []
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {")": "(", "}": "{", "]": "["}

        for char in string:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack:
                    return "Несиметрично"
                if stack[-1] == bracket_pairs[char]:
                    stack.pop()
                else:
                    return "Несиметрично"

        return "Симетрично" if not stack else "Несиметрично"

# Приклади рядків для перевірки
strings_to_check = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for string in strings_to_check:
    print(f"{string}: {BracketBalancer.is_balanced(string)}")
