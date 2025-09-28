"""
Bài 08 - Cửa hàng (Store) quản lý Catalog, Customer và Order
Mục tiêu: Phối hợp nhiều class; điều phối luồng thêm sản phẩm, mua hàng, tích điểm.
Ngữ cảnh: Mô phỏng cửa hàng nhỏ.

Yêu cầu triển khai lớp:
- Store có:
  + Catalog (từ bài 02)
  + customers: dict[int, Customer]
  + place_order(customer_id: int, items: list[tuple[name, qty]]) -> Order

Yêu cầu I/O (tự viết main):
- Tự thiết kế lệnh nhập/xuất hợp lý để thử các chức năng trên (add product, new customer, order...)
"""
from __future__ import annotations
from typing import Dict, List, Tuple


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


class Customer:
    def __init__(self, customer_id: int, name: str) -> None:
        self._id = customer_id
        self._name = name
        self._points = 0

    def add_points(self, p: int) -> None:
        self._points += max(0, p)


class OrderItem:
    def __init__(self, product: Product, qty: int) -> None:
        self._product = product
        self._qty = qty

    def subtotal(self) -> int:
        return self._product._price * self._qty


class Order:
    def __init__(self) -> None:
        self._items: List[OrderItem] = []

    def add_item(self, product: Product, qty: int) -> None:
        self._items.append(OrderItem(product, qty))

    def total(self) -> int:
        return sum(i.subtotal() for i in self._items)


class Store:
    def __init__(self) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def place_order(self, customer_id: int, items: List[Tuple[str, int]]) -> Order:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main để thử thêm sản phẩm, thêm khách và tạo đơn hàng.
    # write your code below
    # write your code above
