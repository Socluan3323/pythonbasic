"""
Bài 09 - Kiểm kê kho (Inventory) theo lô nhập/xuất
Mục tiêu: Quản lý tồn kho chi tiết hơn với nhiều lệnh.
Ngữ cảnh: Cập nhật kho khi nhập hàng và khi khách mua.

Yêu cầu triển khai lớp:
- Inventory với _stock: dict[str, int]
  + import_batch(list[tuple[name, qty]]) -> None
  + export(name: str, qty: int) -> None (giảm tồn; nếu thiếu -> ValueError)
  + to_dict() -> dict

Yêu cầu I/O (tự viết main):
- Input: nhiều lệnh đến EOF
  + "import name qty"
  + "export name qty"
  + "dump"
"""
from typing import Dict


class Inventory:
    def __init__(self) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def import_batch(self, batch: list[tuple[str, int]]) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def export(self, name: str, qty: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int]:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main để xử lý các lệnh import/export/dump.
    # write your code below
    # write your code above
