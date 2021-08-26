my_file = "task6"

def my_func(s):
    if s != "-":
        return int(s.split("(")[0])
    return 0

def my_sum_func(el):
    return sum([my_func(i) for i in el])

with open(my_file, "r", encoding="utf-8") as m_f:
    lst = m_f.readlines()
    dct = {}
    for i in lst:
        name, *el = i.strip().split()
        dct[name.split(":")[0]] = my_sum_func(el)
    print(dct)
