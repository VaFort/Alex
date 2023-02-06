def Function_Days(Max):
    SumDays = int()
    for i in range(Max):
        if i >= 10:
            SumDays = SumDays + int(str(i)[0]) + int(str(i)[1])
        else:
            SumDays += i
    return SumDays

Year = int(input("Введите год: "))
Sum = int()
if Year % 100 == 0 and Year % 400 != 0:
    print("Не високосный год\n")
    Sum += Function_Days(29)
else:
    print("Високосный год\n")
    Sum += Function_Days(30)

Sum += Function_Days(32)*7
Sum += Function_Days(31)*4
print(Sum)
