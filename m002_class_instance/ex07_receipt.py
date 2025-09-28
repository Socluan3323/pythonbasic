"""
Bài 07 - Hóa đơn (Receipt) từ Order
Mục tiêu: Tổng hợp dữ liệu từ Order để xuất hóa đơn.
Ngữ cảnh: In hóa đơn với các dòng hàng, thuế, giảm giá.

Yêu cầu triển khai lớp:
- Receipt(order: Order, tax_percent: int = 0, discount: Discount | None = None)
  + subtotal() -> int
  + tax_amount() -> int
  + total() -> int (sau thuế và giảm)
  + to_dict() -> dict

Yêu cầu I/O (tự viết main):
- Input: bạn tự quyết định cấu trúc (đơn giản/nâng cao tùy ý) để dựng Order, Discount, rồi in Receipt
"""
from typing import Dict, List, Optional


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price


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
        # write your code below
        raise NotImplementedError
        # write your code above

    def subtotal(self) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def tax_amount(self) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def total(self) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int]:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main để dựng Order, Discount (nếu có), tạo Receipt và in to_dict()
    # write your code below
    # write your code above
