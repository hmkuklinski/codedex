import datetime, bday_messages

today = datetime.date.today()
my_next_birthday = datetime.date(2024, 7, 1)

days_away = my_next_birthday - today

if today == my_next_birthday:
	print(bday_messages.selected_message)
else:
	print("My next birthday is " + str(days_away.days) + "days away from today!")