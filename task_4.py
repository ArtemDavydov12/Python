cur_hours = int(input("Введите кол-во часов: "))
cur_minutes = int(input("Введите кол-во минут: "))
cur_seconds = int(input("Введите кол-во секунд: "))
Sum_sec = cur_seconds + (cur_minutes*60) + (cur_hours * 60) * 60
print("Всего", Sum_sec, "секунд.")
