per_ct= 0.2

user = input("몇 캐럿입니까?")

ct = float(user)

gram = ct * per_ct

desc = "{0}캐럿 = {1}그램".format(ct,gram)

print(desc)