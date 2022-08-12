#Lists
lst1=['a','b','c','d','e']
lst2=['red','blue','orange','grey','pink']
item_lst=[1,2,3,True,]
item_lst1=["Siva",24,176.0]
shopping=['Vegetables','Bakery Items','Grocercy']
#List Slicing
#lists can be changeable,also access based on memory spaces
print(item_lst)
print(shopping[0:2])
print(item_lst)
print(shopping[:])
item_lst1[1]=26
items=item_lst1
print(items)
print(len(shopping))
shopping.append('Toys')
shopping.remove(shopping[1])
shopping.pop()
#muliples vales can't be done
shopping.append('Grocery')
shopping.index(1)
print(shopping)
