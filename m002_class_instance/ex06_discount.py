"""
Bài 06 - Mã giảm giá (Discount)
Mục tiêu: Áp dụng giảm giá cho giỏ hàng/đơn hàng.
Ngữ cảnh: Có các mã giảm theo % hoặc theo số tiền cố định.

Yêu cầu triển khai lớp:
- Class Discount(code: str, kind: str, value: int)
  + kind: 'percent' hoặc 'fixed'
  + apply(amount: int) -> int: trả về số tiền sau giảm (không âm)

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "new code kind value" tạo mã
  + "apply code amount" -> in số tiền sau khi áp mã
  + "dump" -> in dict tất cả mã
"""
from typing import Dict


class Discount:
    def __init__(self, code: str, kind: str, value: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def apply(self, amount: int) -> int:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # write your code below
    # write your code above
