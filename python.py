


#  ------------List---------------

# list=[10,"jay",10,20,"hello"]

# list[1]="yash"

# print(list[1:4])

# print(list[::-1])

# list.append("good")

# list.insert(2,"shivay")

# list.extend([5,6,7])

# list.remove(20)

# list.pop(1)

# list.clear()

# list2=[10,50,30,30,20,70,90,20]

# print(sum(list2))

# print(max(list2))

# print(min(list2))

# list2.sort()

# list2.sort(reverse=True)

# list2.reverse()

# print(list2.count(20))

# print(list2.index(90))

# print(len(list2))

# list3=[[1,2,3],["jay",10],["hello"]]
# print(list3[1][0])



#   --------------Tuple----------------

# tuple=(10,)

# tuple1=(10,"jay",20,30,10)

# print(tuple1.count(10))

# print(tuple1.index("jay"))

# print(tuple + tuple1)

# print(tuple1 * 2)



#   ---------Dictionary-------------

# D = {
#     "name":"Sundar",
#     "age":25,
#     "salary":25000
# }

# print(D["name"])

# print(D.get("marks","sorry key not found !!!"))

# D["name"]="Raju"

# D.pop("age")

# D.popitem()

# D.clear()

# print(D.keys())

# print(D.values())

# print(D.items())

# print(len(D))

# D2 = {
#     "salary":30000,
#     "marks":95,
#     "city":"Nashik"
# }
# D.update(D2)
# print(D)


# D3 = {
#     "stu1":{"name":"Messi","age":24},
#     "stu2":{"name":"Ronaldo","age":26}
# }
# print(D3["stu2"]["name"])



#    -------------Set-------------

# s=set()

# s.update([1,2,3,4])
# print(s)

# s1={10,50,40,(1,2,5,8)}

# s1.add(99)
# print(s1)

# s1.remove(10)

# s1.discard(150)

# s1.pop()

# s1.clear()

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7}

# print(set1 | set2)  # unique element print(set1.union(set2))

# print(set1 & set2)  # intersection  print(set1.intersection(set2))

# print(set1 - set2)  # difference  print(set1.difference(set2))

# print(set1 ^ set2)  # symmetric difference  print(set1.symmetric_difference(set2))

# print(5 in set1)  # Membership

# cpy=set1.copy()

# print(cpy)