from functools import reduce

# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# k=list(map(lambda x,y: x+y,a,b))                      #2
# print(k)
# Output: [11, 22, 33, 44, 55]


# nums=[12,15,7,18,20,21,25]
# k=list(filter(lambda x: x%3 or x%5,nums))             #3
# print(k)
# Output: [12, 7, 18, 20, 21, 25]


# nums=[1,2,3,4]
# print(reduce(lambda x,y:x+y,nums,10))                 #4
# Output: 20


# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))      #5
# print("Result:", result)
# print("Nums:", nums)
# Output:Result: [None, None, None]
# Output:Nums: [[1, 2, 10], [3, 4, 10], [5, 6, 10]]


#2 PDF

# a=[[1, 2], [3, 4], [5, 6]]
# k=list(map(lambda x: x+[5],a))                        #1
# print(k)
# Output:[[1, 2, 5], [3, 4, 5], [5, 6, 5]]


# d = {"apple": 100, "banana": 40, "cherry": 150}
# k=dict(filter(lambda x: x[1]>50,d.items()))           #2
# print(d.items())
# print(k)
# Output:dict_items([('apple', 100), ('banana', 40), ('cherry', 150)])
# Output:{'apple': 100, 'cherry': 150}


# n = int(input("How many items? "))
# a = []
# for i in range(n):
#      value = int(input("Enter value: "))               #3
#      a.append(value)
# print(a)
# k=reduce(lambda x,y: x+y,a)
# print(k)
# Output:
# How many items? 5
# Enter value: 1
# Enter value: 2
# Enter value: 3
# Enter value: 4
# Enter value: 5
# [1, 2, 3, 4, 5]
# 15



# a=input()
# k=list(map(lambda x: ord(x),a))                       #5
# print(k)


# a=input()
# r=list(filter(lambda x: x not in "AEIOUaeiou",a))     #6
# print(r)
# Output:
# hello
# ['h', 'l', 'l']


# l=['P', 'y', 't', 'h', 'o', 'n']
# print(reduce(lambda x,y: x+y,l))                      #7
# Output: Python


# l=[10, 350, 10, 350, 20]
# k=list(map(lambda x: id(x),l))                        #8
# print(k)

# l=[5, 10, 15, 20, 25, 30]
# print(reduce(lambda x,y: x+y,filter(lambda x: x%5==0,map(lambda x: x**2,l)),0))    #10
# Output:2275