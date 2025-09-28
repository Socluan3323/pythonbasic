"""
Bài 04 - Đơn hàng (Order) và dòng hàng (OrderItem)
Mục tiêu: Tổ chức object có quan hệ has-a; validation cơ bản.
Ngữ cảnh: Tạo đơn hàng từ giỏ hàng với số lượng cụ thể.

Yêu cầu triển khai lớp:
- Product(name, price) như bài 01
- OrderItem(product: Product, qty: int)
- Order với _items: list[OrderItem]
  + add_item(product, qty)
  + total() -> int
  + to_dict() -> dict (xuất đơn hàng)

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name price qty" để thêm một dòng hàng (product inline)
  + "total" | "dump"
- Output:
  + Với "total": in tổng tiền
  + Với "dump": in dict đơn hàng
"""
from typing import Dict, List


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price}


class OrderItem:
    def __init__(self, product: Product, qty: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def subtotal(self) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        raise NotImplementedError
        # write your code above


class Order:
    def __init__(self) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def add_item(self, product: Product, qty: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def total(self) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, List[Dict[str, int | str]]]:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Order; parse lệnh add/total/dump
    # write your code below
    # write your code above
