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
from typing import Dict, Optional


class Product:
    def __init__(self, name: str, price: int) -> None:
        # write your code below
        # write your code above
        self._name = name
        self._price = price

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price}


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
        self.__items[product_name] = product


    def get(self, name: str) -> Optional[Product]:
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
    # print (c.to_dict())

    catalog = Catalog()
    while True:
        lines = input().strip().split()
        print(lines)
        command = lines[0]
        if command == "add":
            p = Product(lines[1],lines[2])
            catalog.add(p)
        if command == "dump":
            print(catalog.to_dict())
