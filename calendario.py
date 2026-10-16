import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)

ano = int(input("Escolha o ano: "))
for mes in range(1, 13):
    print(cal.formatmonth(ano, mes))