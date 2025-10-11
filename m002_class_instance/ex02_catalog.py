"""
Bài 02 - Danh mục sản phẩm (Catalog)
Mục tiêu: Dùng class quản lý nhiều Product bằng dictionary.
Ngữ cảnh: Tạo danh mục sản phẩm của cửa hàng.

Yêu cầu triển khai lớp:
- Class Product(name, price) như bài 01 (có thể copy y hệt sang đây nếu cần)
- Class Catalog với _items: dict[str, Product]
  + add(product): thêm/ghi đè theo name
  + get(name) -> Product | None
  + to_dict() -> dict[str, dict]

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name price" hoặc "get name" hoặc "dump"
- Output:
  + Với "get": in dict sản phẩm hoặc None
  + Với "dump": in dict toàn bộ danh mục
"""
from typing import Dict, Optional, List
import math
class Product:
    def __init__(self, name: str, price: int) -> None:
        # write your code below
        # write your code above
        try:
            price = int(price)
        except:
            raise ValueError("Price must be integer")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self._name = name.lower()
        self._price = price

    
    def to_dict(self) -> Dict[str, int | str]:        
        return {"name": self._name, "price": int(self._price)}

class Catalog:
    def __init__(self) -> None:
        # write your code below
        # write your code above
        self.__items : Dict[str, Product] = {}

    def add(self, product: Product) -> None:
        # write your code below
        # write your code above
        product_dict = product.to_dict()
        product_name = product_dict.get("name")
        product_price = product_dict.get("price")
        if product_name == '' or product_name is None or product_name in list(self.__items.keys()):
            return None
        try:
            product_price = int(product_price)
        except:
            return None
        if product_price < 0:
            return None
        self.__items[product_name] = product

    def get(self, name: str) -> Optional[Product]:                       # get(key, defaultvalue)
        # write your code below
        # write your code above
        return self.items.get(name)

    def to_dict(self) -> Dict[str, Dict[str, int | str]]:
        # write your code below
        # write your code above
        # for i,j in self.__items.items():
        #     print(i,j.to_dict())
        pmd = {}
        for i,j in self.__items.items():
          pmd[i] = j.to_dict()
        return pmd  
    
    def search_by_name(self, name: str) -> Optional[Product]:
        try:
            return self.__items.get(name.lower())
        except:
            return None
    
    def get_by_price_range(self, min_price: int, max_price: int) -> List[Dict[str, int | str]]:
        product_list = []
        for name, product in self.__items.items():
            product_dict = product.to_dict()
            current_price = product_dict.get("price")
            if  min_price <= current_price <= max_price:
                product_list.append(product.to_dict())
        return product_list
    
    def remove(self, name: str) -> bool:
        name = name.lower()
        product = self.__items.get(name, None)
        if product is None:
            return False
        
        self.__items.pop(name)
        return True
    
    def count(self) -> int:
        return len(self.__items)
    
    def get_all_names(self) -> List[str]:
        return list(self.__items.keys())
    def get_total_value(self) -> int:
        List_product: List[Product] = list(self.__items.values())
        total_value = 0
        for product in List_product:
            print("current price", product._price)
            total_value += product._price
        return total_value
    
    def get_cheapest(self) -> Optional[Product]:
        min_price = math.inf
        product_tmp = None
        for product in self.__items.values():
            if min_price > product._price:
                min_price = product._price
                product_tmp = product
        return product_tmp
    def get_expensive(self) -> Optional[Product]:
        max_price = -math.inf
        product_tmpmax = None
        for e in self.__items.items():
            current_product = e[1]
            if max_price < current_product._price:
                max_price = current_product._price
                product_tmpmax = current_product
        return product_tmpmax
                

            






if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, đọc dòng lệnh tới EOF, parse và gọi phương thức
    # write your code below
    # write your code above
    # p1 = Product("Hair Spray",20000)
    # p2 = Product("Iphone", 600000)
    # p3 = Product("Samsung", 400000)
    # c = Catalog()
    # c.add(p1)
    # c.add(p2)
    # c.add(p3)
    # # c.to_dict()
    # c.get_expensive()

    catalog = Catalog()
    while True:
        lines = input().strip().split(",")
        print(lines)
        command = lines[0]
        if command == "add":
            p = Product(lines[1],lines[2])
            catalog.add(p)
        if command == "dump":
            print(catalog.to_dict())
        if command == "search":
            product_tmp: Product = catalog.search_by_name(lines[1])
            print(product_tmp.to_dict())
        if command == "filter":
            min_price = int(lines[1])
            max_price = int(lines[2])
            print(catalog.get_by_price_range(min_price, max_price))
        if command == "remove":
            isremove = catalog.remove(lines[1])
            print("Remove Successfully") if isremove else print("Remove Unsuccessfully")
        if command == "count":
            total = catalog.count()
            print(total)
        if command == "brand":
            listname = catalog.get_all_names()
            print(listname)
        if command == "Total Value":
            totalvalue = catalog.get_total_value()
            print("Total value is", totalvalue)
        if command == "Cheapest Product":
            try:
                print("Cheapest Product is", catalog.get_cheapest().to_dict())
            except:
                print("No Product")
        
        if command == "MEP":
            try:
                print("MEP is", catalog.get_expensive().to_dict())
            except:
                print("No Product")

        
    
