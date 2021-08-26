import json

my_file = "task7"
my_file1 = "task7_j"
pol_pribil = 0
with open(my_file, "r", encoding="utf-8") as m_f:
    lst = m_f.readlines()
    result = {}
    s_num = 0
    for i in lst:
        name, type_firm, dohod, rashod = i.split()
        pribil = float(dohod) - float(rashod)
        result[name] = pribil
        if pribil > 0:
            s_num += pribil
            pol_pribil += 1

result["sred_prib"] = round(s_num / pol_pribil, 2)

with open(my_file1, "w", encoding="utf-8") as m_f:
    json.dump(result, m_f)
