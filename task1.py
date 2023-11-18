#[1]Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [1, 7, 5, 4, 2, 6, 3]
summ = 8

# call function find
find(array, len(array), summ)


# [2]Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A):
  print( A[::-1])
A = [10, 20, 30, 40, 50]
reverseList(A)

#[3]Write a program to check if two strings are a rotation of each other?

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



