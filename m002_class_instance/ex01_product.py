"""
Bài 01 - Sản phẩm trong cửa hàng (Product)
Mục tiêu: Làm quen với class & instance, thuộc tính cơ bản.
Ngữ cảnh: Lưu thông tin một sản phẩm đơn giản.

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int)
  + name: tên sản phẩm (không rỗng)
  + price: đơn giá (đơn vị: đồng, >= 0)
- to_dict() -> dict[str, int|str]

Yêu cầu I/O (tự viết main):
- Input:
  Dòng 1: tên sản phẩm
  Dòng 2: đơn giá (số nguyên)
- Output: in dict thông tin sản phẩm, ví dụ: {'name': 'Milk', 'price': 15000}
"""
from typing import Dict


class Product:
    def __init__(self, name: str, price: int) -> None:
        # write your code below
        # write your code above
        self._name = name
        self._price = price
        

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        # write your code above
        return {"name": self._name , "price": self._price}
        


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Đọc name, price
    # - p = Product(name, price); print(p.to_dict())
    # write your code below
    # write your code above
  product = Product("Apple", 10000)
  print(product.to_dict())