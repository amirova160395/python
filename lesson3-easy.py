print("Zadacha 1 - easy")
n = float(input("Введите десятичное число: "))
nd = int(input("Округление до кол-ва знаков: "))
def my_round(n, nd):
    m = pow(10.0, nd)
    return int (n*m + 0.5) / m
print(my_round(n, nd))
print()

print("Zadacha 2 - easy")
ticket = str(input("Введите номер билета: "))
ticket_number = list(ticket)
def lucky_ticket(ticket_number):
    if int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == int(ticket_number[-3]) + int(ticket_number[-2]) + int(ticket_number[-1]):
        print("Поздравляем! У вас счастливый билет!")
lucky_ticket(ticket_number)
print()





