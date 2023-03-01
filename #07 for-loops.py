#list1=("A", "B", "C", "D", "E")
#for item in list1:
#    print(item)


"""
list2=[["A",1], ["B",2], ["C",5], ["D",9], ["E",6]]
#for item,lollypop in list2:
 #   print(item,lollypop)

# convert in dictionary
dict1=dict(list2)
for item in dict1:
    print(item)

"""
# practics

items=["hello","python","world",11,45,6,2,7,85,69,15]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)