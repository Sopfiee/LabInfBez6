#Вариант 11
#Только те, у кого полные права, могут давать передачу прав
import Lab as l

C = ["Чтение", "Запись", "Передать права", "Выход", "Печать"]
L = l.Lab

print(l.cm.table.table)

while 1:
    user = 0

    while user == 0:
        user = L.identefication(L, input("Пользователь: "))

    command = 0
    while command == 0:
        command = input("Жду ваших указаний(Чтение/Запись/Передать права/Выход/Печать): ")

        if command == C[0]:
            n = input("Какой файл прочитать?: ")
            command = L.read(L, n, user)

        elif command == C[1]:
            n = input("В какой файл сделать запись?: ")
            command = L.write(L, n, user)

        elif command == C[2]:
            n = input("Права на какой файл передать?: ")
            g = input("Какое право передать?: ")
            w = input("Кому передать права?: ")
            command = L.give(L, user, n, g, w)

        elif command == C[3]:
            print("До свидания, " + user + "!")
            command = 1

        elif command == C[4]:
            command = L.print(L)

        else:
            print("Такой команды нет!")
            command = 0


