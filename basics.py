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

#strings
# a= 'hellodavood'
# print(a[::-1])
# a = 'davoodbhaiooo'
# vowels_count = 0
# cons_count = 0
# for i in a:
#     if i in 'aeiosAEIOS':
#         vowels_count = vowels_count + 1
#     else:
#         cons_count +=1
# print("vowels_count",vowels_count)
# print("cons_count",cons_count)

#count words in string 

# a = 'hello davood bhai how are you bro'
# b = a.split()
# print(len(b))


# a = ['a','d','a','b','d','v','c','g']
# fre = {}

# for i in a:
#     if i in fre:
#         fre[i] +=1
#     else:
#         fre[i] = 1
# print(fre)

# a='davod bahi is god bhai'
# print("".join(a.split()))

# a = 'medamre'
# b = 'damemer'
# f=0
# if (len(a) == len(b)):
#     for i in a:
#         if i not in b:
#             f=1
#             break
#     if(f==1):
#         print("Not anagram")
#     else:
#         print("Anagram")

# else:
#     print("Not anagram")

# a = 'sjdhuejdalsjd'
# b ={}
# for i in a:
#     b[i] = b.get(i,0)+1
# print(b)

# def duplitcate(n):
#     a=set()
#     for i in n:
#         if i in a:
#             return True
#         a.add(i)
#     return False

print(duplitcate([1,2,3,1]))
# print(duplitcate([1,2,3,4]))

    