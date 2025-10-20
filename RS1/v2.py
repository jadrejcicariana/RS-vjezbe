#prijestupna godina

godina = int(input("Unesite godinu: "))
if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(godina, ". je prijestupna.")
else:
    print(godina, ". nije prijestupna.")