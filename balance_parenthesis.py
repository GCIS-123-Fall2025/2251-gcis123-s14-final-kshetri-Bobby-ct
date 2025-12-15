
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    s = Stack()
    for i in range(len(a_string)-1):
        print(s)
        if a_string[i] == "(":
            s.push(i)
        elif a_string[i] == ")":
            if not s.is_empty():
                s.pop()
            else:  # if the stack is empty, we have an extra ) 
                s.push(i)
    if len(s) == 0:
        return 0
    else:
        remaining = s.pop()
        if a_string[remaining] == "(":
            return remaining
        elif a_string[remaining] == ")":
            return -1



def main():
    print(balance_parenthesis("this (((is a)) test"))  # returns 5, as the ( at index 5 is never closed
    print(balance_parenthesis("this ((is a)) test"))  # returns 0
    print(balance_parenthesis("this (is a)) test"))  # returns -1 

if __name__ == "__main__":    main()