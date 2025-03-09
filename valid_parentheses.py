'''
Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
A string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket must have a corresponding open bracket.

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False
'''


def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # Map closing to opening brackets

    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'  # Get the last open bracket
            if mapping[char] != top_element:  # Check if it matches
                return False
        else:
            stack.append(char)  # Push open brackets to stack

    return not stack  # Return True if stack is empty (all matched)


s = "()[]{}"
print(is_valid(s))  # Output: True

s = "(]"
print(is_valid(s))  # Output: False
