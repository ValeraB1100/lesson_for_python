my_file = ("task2")

with open(my_file, "r", encoding="utf-8") as m_f:
    lst = m_f.readlines()
print(f"количество строк в файле: {len(lst)}")
for i, j in enumerate(lst):
    print(f"в строке {i} {len(j.split())} слов")
