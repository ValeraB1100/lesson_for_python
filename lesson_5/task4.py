my_file = "task4"
my_file2 = "task4.2"
dict_num = {
    "one" : "один",
    "two" : "два",
    "three" : "три",
    "four" : "четыре"
}

with open(my_file, "r", encoding="utf-8") as m_f:
    lst = m_f.readlines()
lst1 = [f"{dict_num[i.split(' - ')[0]]} - {i.split(' - ')[-1]}" for i in lst]

with open(my_file2, "w", encoding="utf-8") as m_f2:
    m_f2.writelines(lst1)