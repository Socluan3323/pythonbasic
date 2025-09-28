"""
Bài 05 - Khách hàng (Customer) và điểm tích luỹ
Mục tiêu: Quản lý thông tin khách và tích luỹ điểm.
Ngữ cảnh: Mỗi lần mua hàng, khách được cộng điểm.

Yêu cầu triển khai lớp:
- Class Customer(id: int, name: str)
  + add_points(p: int) -> None
  + points (property read-only)
  + to_dict() -> dict

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "new id name" tạo khách
  + "add id points" cộng điểm cho khách
  + "get id" in dict khách hoặc None
  + "dump" in dict tất cả khách theo id
"""
from typing import Dict


class Customer:
    def __init__(self, customer_id: int, name: str) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def add_points(self, p: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    @property
    def points(self) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý: dùng dict[int, Customer] để lưu nhiều khách.
    # write your code below
    # write your code above
