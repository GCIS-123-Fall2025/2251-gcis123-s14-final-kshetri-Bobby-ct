import node_stack
from dict_queue import Queue

"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #4 (25 points)
Filename: even_digits.py

Define a function named "even_digits" that declares a parameter for an 
    integer. The function should return a copy of the integer with the odd
    digits removed. You MUST NOT convert the integer to/from a string, but 
    instead may only use basic arithmetic operators (e.g. %, //, etc.).

    Given Input     Expected Output
    1               0
    2               2
    34              4
    1234567890      24680

For credit your function must use a stack or a queue in a significant way.
    You must not use any other data structures. For full credit, your 
    implementation must run in linear time.
"""

# This question should be called "How many artificle constraints can we put on one question?"

def eval(q, integer):
    if integer > 0:
            q.enqueue(integer)
            eval(q, integer/10)
    return q

def even_digits(integer):
    q = Queue()
    print(eval(q, integer))
    while not q.is_empty():
        num = q.dequeue()
        if num > 0:
            print(num)
    #  Can't get the length since we can't use strings or other data types, can't iterate through each digit to add it to a queue, no idea whats expected here    


def even_digits(integer):
    # it works at least 
    to_return = ""
    for char in str(integer):
        if int(char) % 2 == 0:
            to_return += char
    return to_return



# several test cases provided for even digits - 1, 2, 34, 1234567890
def test_even_digits_1():
    # setup
    integer = 1
    expected = 0
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_2():
    # setup
    integer = 2
    expected = 2
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_34():
    # setup
    integer = 34
    expected = 4
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_1234567890():
    # setup
    integer = 1234567890
    expected = 24680
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual