my_file = ("my_file.txt")

with open(my_file, "w", encoding="utf-8") as m_f:
    while True:
        a = input("введите что-нибудь или нажмите ентер для выхода: ")
        if a == "":
            break
        m_f.write(f"{a}\n")
