my_file = "task5"

with open(my_file, "w", encoding="utf-8") as m_f:
    a = input("введите числа через пробел: ")
    m_f.write(a)


with open(my_file, "r", encoding="utf-8") as m_f:
    lst = m_f.read()
    lst1 = [int(i) for i in lst.split()]
    print(sum(lst1))