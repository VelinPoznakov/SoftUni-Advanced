def extract_parentheses(expression):
    stack = []  # Use a stack to keep track of opening parentheses indices

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                start = stack.pop()  # Pop the last opening parenthesis index
                print(expression[start:i + 1])  # Print the substring with parentheses


# Read input
algebraic_expression = input()

# Extract and print parentheses from the expression
extract_parentheses(algebraic_expression)
