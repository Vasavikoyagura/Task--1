#[1]Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [1, 7, 5, 4, 2, 6, 3]
summ = 8

find(array, len(array), summ)


# [2]Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A):
  print( A[::-1])
A = [10, 20, 30, 40, 50]
reverseList(A)

# [3] Write a program to check if two strings are a rotation of each other?

string1 = input()
string2 = input()
if len(string1)!= len(string2):
  print('Invalid rotation')
else:
  newstrn = string1+string2
  if string2 in newstrn:
    print('Valid Rotation')
  else:
    print('Invalid Rotation')

# [4]   Write a program to print the first non-repeated character from a string?

str = "PREPINSTA"
flag = 0
for i in str:
    if str.count(i) == 1:
        print("First non-repeating character is :", i)
        flag = 1
        break
if flag == 0:
    print("No non-repeating character")

# [5] Read about the Tower of Hanoi algorithm. Write a program to implement it?

def toh(n,src,dest,temp):
    if (n==0):
        return
    toh(n-1,src,temp,dest)
    print("Move",n,"from",src,"to",dest)
    toh(n-1,temp,dest,src)
n=int(input())
for i in range(n):
    c=0
    a=int(input())
    print(2**a-1)
    toh(a,'A','C','B')

# [6] Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression ?
def is_operator(char):
    return char in {'+', '-', '*', '/'}

def postfix_to_prefix(postfix_expression):
    stack = []
    for char in postfix_expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)

    return stack.pop()

a=str(input())
b = postfix_to_prefix(a)
print(b)

# [7] Write a program to convert prefix expression to infix expression ? 

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(prefix_expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in reversed(prefix_expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = f"({operand1} {char} {operand2})"
            stack.append(infix_expression)

    return stack.pop()
a=str(input())
b = prefix_to_infix(a)
print(b)

# [8]  Write a program to check if all the brackets are closed in a given code snippet ?

def are_brackets_closed(code):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return not stack

a=input()
res=are_brackets_closed(a)
if res:
    print("closed")
else:
    print("Not closed")

# [9] Write a program to reverse a stack ?

class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_stack(input_stack):
    aux_stack = Stack()

  
    while not input_stack.is_empty():
        aux_stack.push(input_stack.pop())

    while not aux_stack.is_empty():
        input_stack.push(aux_stack.pop())

input_stack = Stack()

input_elements = input().split()
for element in input_elements:
    input_stack.push(element)

reverse_stack(input_stack)

print( input_stack.items)

# [10] Write a program to find the smallest number using a stack ? 

class StackWithMin:
    def _init_(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            if popped_item == self.min_stack[-1]:
                self.min_stack.pop()
            return popped_item

    def get_min(self):
        if not self.is_empty():
            return self.min_stack[-1]

stack_with_min = StackWithMin()
input_elements = input().split()
for element in input_elements:
    stack_with_min.push(int(element))

print(stack_with_min.stack)
print(stack_with_min.get_min())






