# print("Hii davood welcome to python again")

# a =[1,3,4,2,3,5,6]
# b=[]

# for i in a :
#     if i not in b :
#         b.append(i)
# print(b)

# a = [1,3,5,7,9]
# b = [2,4,6,8,10,12,13,14]
# res = a+b
#output = result = [1,2,3,4,5,6,7,8]
# i=0
# j=0
# res = []
# while i <len(a) and j<len(b):
#     if a[i] < b[j]:
#         res.append(a[i])
#         i+=1
#     else:
#         res.append(b[j])
#         j+=1
# res.extend(a[i:])
# res.extend(b[j:])

# print(res)

# a=[1,2,0,0,4,5,0,0,4,5]
# b=[]
# c=[]
# for i in a:
#     if i == 0:
#         c.append(i)
#     else:
#         b.append(i)
# print(b)
# print(c)
# print(b+c)
# b.extend(c)
# print(b)

# a = [1,2,3,4]
# #out = [2,3,4,1]
# rot = 1
# print(a[rot:]+a[:rot])

# a = [1,2,3,0,5]
# n = len(a)
# for i in range(n+1):
#     if i not in a:
#         print(i)
#         break

# a = [1,2,3,3,2,4,5,3,4,5,4]
#out = [2,3]

# b = set()
# c = set()
# for i in a :
#     if i in b:
#         c.add(i)
#     else:
#         b.add(i)
# print(list(c))

# a=[1,3,2,4,5,6]
# tar = 11

# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j] == tar:
#             print(i,j)
#             break