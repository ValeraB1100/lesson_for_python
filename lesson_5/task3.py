my_file = ("task2")

with open(my_file, "r", encoding="utf-8") as m_f:
    lst = m_f.readlines()
familiya = []
sum_zp = 0
for i in lst:
    fam, zp = i.split()
    zp = float(zp)
    sum_zp += zp
    if zp < 20000:
        familiya.append(fam)

print(f"средняя величина дохода: {round(sum_zp/len(lst), 2)}")
print(f"сотрудники у которых доход меньше 20000: {familiya}")
