# class Product:
#     def __init__(self, name: str, price: int) -> None:
 
#         self._name = name  
#         self._price = price
        
#     def __repr__(self):
#         return f"{self._name}: {self._price}"
    
# products = [
#     Product("laptop", 1000),
#     Product("mouse", 20),
#     Product("keyboard", 50),
#     Product("monitor", 300)
# ]


# print(f"before sort: {products}")

# Sorted_by_price = sorted(products, key=lambda x: x._price)

# print(f"after sort: {Sorted_by_price}")


# list = [2,1,3]
# a = l[0]
# l[0] = l[1]
# l[1] = a
# print(l)
# list = [4,3,2,1,7,6,9,5,10,8]

# def swap(list: list, i, j):
#     print(i,j)
#     a = list[i]
#     list[i] = list[j]
#     list[j] = a

# # swap(l,0,1)
# # print(l)
# # for i in range(len(list)-1):
# #     if list[i] > list[i+1]:
# #         swap(list,i,i+1)
    
# # print(list)
# for i in range(len(list)-1):
#     for j in range(len(list)-1-i):
#         if list[j] > list[j+1]:
#             swap(list,j,j+1)
# print(list)
# # len-1 ra thang cuoi, len-2 ra thang ke cuoi

# bai 2
class Product:
    def __init__(self, name: str, price: int) -> None:
 
        self._name = name  
        self._price = price
        
    def __repr__(self):
        return f"{self._name}: {self._price}"
    


# def clone_sorted_selection_sorted(l: list[Product]):
#     for i in range(len(l)-1):
#         maxindex = -1
#         maxvalue = -9999
#         for j in range(len(l)-i):
#             if maxvalue < l[j]._price:
#                 maxindex = j
#                 maxvalue = l[j]._price
#         swap(l,maxindex,len(l)-1-i)
    

# products = [
#     Product("laptop", 1000),
#     Product("mouse", 20),
#     Product("keyboard", 50),
#     Product("monitor", 300)
# ]

# clone_sorted_selection_sorted(products)
# products = sorted(products,key=lambda x: x._name)
# print(products)

# tmpFunc = lambda x: x._price
# print(tmpFunc(Product("Iphone",20000)))




def swap(list: list, i, j):
    print(i,j)
    a = list[i]
    list[i] = list[j]
    list[j] = a
def clone_sorted(l: list[Product],key: callable, reverse: bool = False):
    if not reverse:
        for i in range(len(l)-1):
            maxindex = -1
            maxvalue = 'a'
            if isinstance(key(l[0]),int):
                maxvalue = -9999
            print(key(l[0]))
            for j in range(len(l)-i):
                print( key(l[j]),maxvalue)
                
                if maxvalue < key(l[j]):
                    maxindex = j
                    maxvalue = key(l[j])
            swap(l,maxindex,len(l)-1-i)
    else:
        for i in range(len(l)-1):
            minindex = len(l)
            minvalue = 'z'
            if isinstance(key(l[0]),int):
                minvalue = 9999999999
            print(key(l[0]))
            for j in range(len(l)-i):
                print( key(l[j]),minvalue)
                
                if minvalue > key(l[j]):
                    minindex = j
                    minvalue = key(l[j])
            swap(l,minindex,len(l)-1-i)
        




products = [
    Product("apple", 5000),
    Product("banana", 7000),
    Product("cherry", 3000)
]

clone_sorted(products,key=lambda x: x._price, reverse = True)
print(products)