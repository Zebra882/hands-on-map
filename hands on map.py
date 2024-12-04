number1=[1,2,6,9]
number2=[6,7,3,4]
result =map(lambda x,y : x*y, number1, number2)
print("addition of the two list.")
print(list(result))

num=[6,9,1,4,5,6,12,5,1,4,2,6,9,4,8,8,4,7,9,5,9,8,3,8,0,5,6]
def sq(n):
    return n*n
square= list(map(sq,num))
print("square of numbers in the list.")
print(square) 