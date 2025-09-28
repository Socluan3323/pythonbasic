"""
Bài 10 - Loyalty Pipeline: mua hàng -> tích điểm -> áp mã giảm -> xuất hoá đơn
Mục tiêu: Kết hợp nhiều class và luồng xử lý.
Ngữ cảnh: Khi khách mua hàng, cửa hàng tính điểm thưởng, áp mã giảm và in hóa đơn.

Yêu cầu triển khai lớp:
- Dùng lại: Product, Catalog, Customer, Discount, Order, Receipt
- Lớp LoyaltyEngine với run(customer, items, discount?) -> Receipt

Yêu cầu I/O (tự viết main):
- Bạn tự thiết kế input hợp lý để tạo Catalog/Customer/Order/Discount, sau đó gọi LoyaltyEngine.run và in hóa đơn.
"""
from __future__ import annotations
from typing import Dict, List, Optional, Tuple


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


class Discount:
    def __init__(self, code: str, kind: str, value: int) -> None:
        self._code = code
        self._kind = kind
        self._value = value

    def apply(self, amount: int) -> int:
        if self._kind == "percent":
            return max(0, amount - amount * self._value // 100)
        return max(0, amount - self._value)


class Receipt:
    def __init__(self, order: Order, tax_percent: int = 0, discount: Optional[Discount] = None) -> None:
        self._order = order
        self._tax_percent = max(0, tax_percent)
        self._discount = discount

    def subtotal(self) -> int:
        return self._order.total()

    def tax_amount(self) -> int:
        return self.subtotal() * self._tax_percent // 100

    def total(self) -> int:
        amount = self.subtotal() + self.tax_amount()
        return self._discount.apply(amount) if self._discount else amount

    def to_dict(self) -> Dict[str, int]:
        return {"subtotal": self.subtotal(), "tax": self.tax_amount(), "total": self.total()}


class LoyaltyEngine:
    def __init__(self, catalog: Catalog) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def run(self, customer: Customer, items: List[Tuple[str, int]], discount: Optional[Discount] = None) -> Receipt:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main để tạo Catalog/Customer/Order/Discount và chạy LoyaltyEngine.
    # write your code below
    # write your code above
