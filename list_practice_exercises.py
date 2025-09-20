# list_practice_exercises.py
# Mục tiêu: Luyện tập list + while, break, continue, match, del, index()


# =========================
# 1) WHILE 
# =========================

def while_sum_positive(nums):
    """
    Bài 1 (while): Tính tổng các phần tử dương đầu tiên cho đến khi gặp số âm thì dừng vòng lặp.
    - Input: nums (list[int])
    - Output: tổng (int) của các phần tử dương liên tiếp từ đầu list cho đến trước phần tử âm đầu tiên.
    Ví dụ:
        while_sum_positive([1, 2, 3, -4, 5]) -> 6   (vì gặp -4 thì dừng, 1+2+3=6)
        while_sum_positive([-1, 2, 3]) -> 0        (phần tử đầu đã âm, tổng = 0)
    """
    i = 0
    total = 0
    # TODO: dùng while với điều kiện chỉ số còn trong phạm vi list
    while ___ < ___:
        # TODO: lấy phần tử hiện tại
        val = ___[___]
        # TODO: nếu val < 0 thì dừng vòng while (break)
        if ___:
            ___
        # TODO: cộng vào total và tăng i
        total ___ ___
        i ___ ___
    return total


# def while_collect_until_zero(nums):
#     """
#     Bài 2 (while): Thu thập các phần tử cho đến khi gặp 0 thì dừng, trả về list kết quả.
#     Ví dụ:
#         while_collect_until_zero([5, 4, 0, 9]) -> [5, 4]
#         while_collect_until_zero([0, 1, 2]) -> []
#     """
#     res = []
#     idx = 0
#     # TODO: vòng while duyệt qua list
#     while ___:
#         current = ___[___]
#         # TODO: nếu current == 0 thì dừng vòng while
#         if ___:
#             ___
#         # TODO: thêm current vào res và tăng idx
#         ___(___)
#         idx ___ ___
#     return res


# =========================
# 2) BREAK 
# =========================

# def break_find_first_even(nums):
#     """
#     Bài 1 (break): Tìm số chẵn đầu tiên trong list. Nếu không có trả về None.
#     Ví dụ:
#         break_find_first_even([1, 3, 5, 8, 10]) -> 8
#         break_find_first_even([1, 3, 5]) -> None
#     """
#     found = None
#     for n in ___:
#         if ___ % 2 == 0:
#             found = ___
#             ___   # dùng break để thoát vòng for
#     return found


# def break_stop_after_target(names, target):
#     """
#     Bài 2 (break): Duyệt qua names, gom tên vào result cho đến khi gặp target thì dừng (không thêm target).
#     Ví dụ:
#         break_stop_after_target(["a", "b", "c", "d"], "c") -> ["a", "b"]
#         break_stop_after_target(["a", "b"], "z") -> ["a", "b"]
#     """
#     result = []
#     for name in ___:
#         if name == ___:
#             ___
#         ___(___)
#     return result


# =========================
# 3) CONTINUE 
# =========================

# def continue_filter_negatives(nums):
#     """
#     Bài 1 (continue): Tạo list mới chỉ chứa số không âm (>=0). Bỏ qua số âm bằng continue.
#     Ví dụ:
#         continue_filter_negatives([1, -2, 3, -4, 0]) -> [1, 3, 0]
#     """
#     res = []
#     for x in ___:
#         if x < 0:
#             ___   # bỏ qua phần còn lại của vòng lặp
#         ___(___)
#     return res


# def continue_skip_short_words(words, min_len):
#     """
#     Bài 2 (continue): Trả về list gồm các từ có độ dài >= min_len. Bỏ qua từ ngắn bằng continue.
#     Ví dụ:
#         continue_skip_short_words(["hi","code","ai","python"], 3) -> ["code","python"]
#     """
#     out = []
#     for w in ___:
#         if ___(w) < ___:
#             ___
#         ___(___)
#     return out


# =========================
# 4) MATCH 
# =========================

# def match_classify_token(token):
#     """
#     Bài 1 (match): Phân loại token theo kiểu dữ liệu.
#     - Nếu token là int dương: trả về "POS_INT"
#     - Nếu token là int không dương (<=0): trả về "NON_POS_INT"
#     - Nếu token là str rỗng: trả về "EMPTY_STR"
#     - Nếu token là str khác rỗng: trả về "STR"
#     - Ngược lại: trả về "OTHER"
#     """
#     match ___:
#         case int() as n if ___:
#             return "POS_INT"
#         case int() as n:
#             return ___
#         case str() as s if ___ == "":
#             return ___
#         case str():
#             return ___
#         case _:
#             return "OTHER"


# def match_command_list(cmd, data):
#     """
#     Bài 2 (match): Xử lý lệnh đơn giản trên list 'data'.
#     - cmd là tuple dạng ("head", k) -> trả về k phần tử đầu của data
#     - cmd là tuple dạng ("tail", k) -> trả về k phần tử cuối của data
#     - cmd là tuple dạng ("get", i)  -> trả về phần tử tại index i (nếu i hợp lệ), else None
#     - cmd là tuple dạng ("count", x) -> trả về số lần xuất hiện của x trong data
#     - còn lại -> trả về None
#     Ví dụ:
#         match_command_list(("head", 2), [1,2,3,4]) -> [1,2]
#         match_command_list(("tail", 2), [1,2,3,4]) -> [3,4]
#         match_command_list(("get", 1), ["a","b"]) -> "b"
#         match_command_list(("count", "a"), ["a","b","a"]) -> 2
#     """
#     match ___:
#         case ("head", k):
#             return ___[:___]
#         case ("tail", k):
#             return ___[-___:]
#         case ("get", i):
#             # trả về phần tử tại i nếu i hợp lệ, else None
#             return ___[___] if 0 <= ___ < ___(___) else ___
#         case ("count", x):
#             return ___.___(___)
#         case _:
#             return ___


# =========================
# 5) DEL 
# =========================

# def del_remove_range(data, start, end):
#     """
#     Bài 1 (del): Xóa các phần tử trong đoạn [start, end) bằng del.
#     - Nếu start/end không hợp lệ, không làm gì.
#     Ví dụ:
#         del_remove_range([0,1,2,3,4], 1, 4) -> [0,4]
#     """
#     # TODO: kiểm tra hợp lệ, rồi del data[start:end]
#     if 0 <= ___ <= ___ and 0 <= ___ <= ___ and ___ < ___:
#         del ___[___:___]
#     return data


# def del_remove_every_second(data):
#     """
#     Bài 2 (del): Xóa các phần tử ở vị trí chẵn (index 0,2,4,...) bằng del slicing.
#     Ví dụ:
#         del_remove_every_second([10,11,12,13,14]) -> [11,13]
#     """
#     # Gợi ý: dùng del data[___:___:___]
#     del ___[___:___:___]
#     return data


# =========================
# 6) INDEX() 
# =========================

# def index_find_first_occurrence(data, target):
#     """
#     Bài 1 (index): Trả về index xuất hiện đầu tiên của target trong data, hoặc -1 nếu không có.
#     Dùng list.index, nhưng tránh crash bằng try/except.
#     Ví dụ:
#         index_find_first_occurrence(["a","b","a"], "a") -> 0
#         index_find_first_occurrence(["a","b"], "z") -> -1
#     """
#     try:
#         pos = ___.___(___)
#         return ___
#     except ___:
#         return ___


# def index_find_all_occurrences(data, target):
#     """
#     Bài 2 (index): Trả về list chứa mọi chỉ số i sao cho data[i] == target.
#     Không dùng list comprehension; dùng while + index(start).
#     Gợi ý:
#         - dùng start = 0
#         - trong while: gọi data.index(target, start) để lấy vị trí kế tiếp
#         - nếu ValueError -> dừng
#         - update start = vị trí vừa tìm + 1
#     Ví dụ:
#         index_find_all_occurrences(["x","a","x","b","x"], "x") -> [0,2,4]
#     """
#     positions = []
#     start = 0
#     while True:
#         try:
#             i = ___.___(___, ___)
#             ___(___)
#             start = ___ + ___
#         except ___:
#             break
#     return positions


if __name__ == "__main__":
    # Gợi ý: bỏ comment từng dòng sau khi bạn đã hoàn thành hàm tương ứng.
    print(while_sum_positive([1,2,3,-1,5]))
    # print(while_collect_until_zero([5,4,0,9]))
    # print(break_find_first_even([1,3,5,8,10]))
    # print(break_stop_after_target(["a","b","c","d"], "c"))
    # print(continue_filter_negatives([1,-2,3,-4,0]))
    # print(continue_skip_short_words(["hi","code","ai","python"], 3))
    # print(match_classify_token(5), match_classify_token(0), match_classify_token(""), match_classify_token("x"), match_classify_token(2.5))
    # print(match_command_list(("head", 2), [1,2,3,4]))
    # print(match_command_list(("tail", 2), [1,2,3,4]))
    # print(match_command_list(("get", 1), ["a","b"]))
    # print(match_command_list(("count", "a"), ["a","b","a"]))
    # print(del_remove_range([0,1,2,3,4], 1, 4))
    # print(del_remove_every_second([10,11,12,13,14]))
    # print(index_find_first_occurrence(["a","b","a"], "a"))
    # print(index_find_all_occurrences(["x","a","x","b","x"], "x"))
    pass
