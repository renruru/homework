# dict1 = {'name':'earth','port':'ert'}
# # for key in dict1.keys():
# #     print 'key = %s,values = %s' % (key,dict1[key])
# # dict1['arch'] = 'sunos'
# # print(dict1.items())
# dict2 = {'TURE':'a','B':'b'}
# # dict2.update(dict1)
# print(dict2.keys())

list1 = [1,2,3,4]
list2 = ['a','b','c','d']


print(dict([ (list1[i], list2[i]) for i in range(0,4)]))

list3=[]
for i in range(0,4):
    list3.append([list1[i],list2[i]])

print(dict(list3))
# list3 = list1[0::2]
# list4 = list2[1::2]
# print(list2)
# dict1 = {}

list3 = tuple([x for x in list1])
# print(list3)

list4 = tuple([x for x in list2])
# list3 = [1,2]
# list4 = ['a','b']

print(dict(zip(list3,list4)))

# #print([list1,list2])

# #print(dict([list2,list1]))
# print(dict([list3,list4]))


#print(dict(zip(list3,list4)))
#print(dict(zip(list1,list2)))
        

#print(dict1.fromkeys(list3,list4))

