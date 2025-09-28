"""
Bài 03 - Giỏ hàng cơ bản (Cart)
Mục tiêu: Dùng class chứa state, thao tác với Product.
Ngữ cảnh: Thêm sản phẩm vào giỏ và xem tổng tiền.

Yêu cầu triển khai lớp:
- Class Product(name, price) như bài 01
- Class Cart với _items: dict[str, int] (map name -> quantity)
  + add(product: Product, qty: int)
  + remove(name: str, qty: int)
  + total(catalog: Catalog) -> int (tính theo price trong Catalog)

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name qty" | "remove name qty" | "total"
- Output:
  + Với "total": in tổng tiền (int)
"""
from __future__ import annotations
from typing import Dict


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price 


class Catalog:
    def __init__(self) -> None:
        self._items: Dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self._items[product._name] = product

    def get(self, name: str) -> Product | None:
        return self._items.get(name)
        
    def to_dict(self) -> Dict[str, Product]:
        return {name: product.to_dict() for name, product in self._items.items()}

class Cart:
    def __init__(self) -> None:
        # write your code below
        self._items: Dict[str, Product] = {}
        # write your code above

    def add(self, product: Product, qty: int) -> None:
        # write your code below
        self._items[product._name] = product
        # write your code above

    def remove(self, name: str, qty: int) -> None:
        # write your code below
        self._items[name] -= qty
        # write your code above

    def total(self, catalog: Catalog) -> int:
        # write your code below
        return sum(product.price * qty for product, qty in self._items.items())
        # write your code above


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, thêm vài Product mẫu (tuỳ bạn)
    # - Tạo Cart, xử lý lệnh add/remove/total
    # write your code below
    # write your code above
