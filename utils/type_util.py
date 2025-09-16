import re

def if_int(val):
    return isinstance(val, int)

def if_float(val):
    return isinstance(val, float)

def if_str(val):
    return isinstance(val, str)

def convert_number(val):
    if if_str(val):
        if val.isdigit():
            return int(val)
        else:
            return float(val)
    else:
        return val

# 判断是否是 数值型 或 字符串数字
def is_number(val):
    if if_int(val) or if_float(val):
        return True
    elif re.match(r'^[-+]?\d*\.\d+$', val) or re.match(r'^[-+]?\d+$', val):
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_number("1022.6659"))