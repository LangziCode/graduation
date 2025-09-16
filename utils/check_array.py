def check_array_type(arr):
    # 检查数组是否为空
    if not arr:
        return "Array is empty"

    # 初始化一个计数器来存储数值和字符串的数量
    num_count = 0
    str_count = 0

    for element in arr:
        if isinstance(element, (int, float)):  # 检查是否为数值（整数或浮点数）
            num_count += 1
        elif isinstance(element, str):  # 检查是否为字符串
            str_count += 1
        else:
            return "Array contains other types besides numbers and strings"

    # 根据计数器的值判断数组的类型
    if num_count > 0 and str_count > 0:
        return "str and number"
    elif num_count > 0:
        return "number"
    else:
        return "str"