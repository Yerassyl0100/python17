print("Мы начинаем QUIZ по истории! Ответы принимаются на латинице [A, B, C, D]")
right_answers = 0

print("\n1. В каком периоде каменного века сформировался современный тип человека?")
print("A) в раннем палеолите")
print("B) в среднем палеолите")
print("C) в позднем палеолите")
print("D) в мезолите")

correct_answer = "C" and "c"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n2. В какой части Казахстана обнаружены стоянки палеолитического периода?")
print("A) в бассейне р. Сырдарьи")
print("B) в районе хребта Каратау")
print("C) на Мангышлаке")
print("D) в мезолите")

correct_answer = "B" and "b"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n3. Какой тип хозяйства зародился в эпоху неолита?")
print("A) производящий")
print("B) потребляющий")
print("C) натуральный")
print("D) комплексный")

correct_answer = "A" and "a"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------


print("\n4. Какой хронологический период охватывает неолит?")
print("A) 5 тыс. лет до н.э. – 3 тыс. лет до н.э.")
print("B) 12 – 10 тыс. лет н.э.")
print("C) 5 – 10 тыс. лет до н.э.")
print("D) 12 – 10 тыс. лет до н.э.")

correct_answer = "A" and "a"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n5. Бумеранг был изобретен в эпоху: ")
print("A) неолита")
print("B) мезолита")
print("C) верхнего палеолита")
print("D) железного века.")

correct_answer = "B" and "b"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n6. Люди научились шлифовать, сверлить и пилить камень в эпоху:")
print("A) позднего палеолита")
print("B) мезолита")
print("C) среднего палеолита")
print("D) неолита")

correct_answer = "D" and "d"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n7. Добывать огонь человек научился в эпоху:")
print("A) мезолита")
print("B) позднего палеолита")
print("C) энеолита")
print("D) среднего палеолита")

correct_answer = "D" and "d"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n8. Из какого материала человек сделал первые орудия труда?")
print("A) железо")
print("B) камень")
print("C) дерево")
print("D) бронза")

correct_answer = "B" and "b"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n9. На каком языке говорили племена эпохи бронзы?")
print("A) на кыпчакском")
print("B) на арабском")
print("C) на индоиранском")
print("D) на индоевропейском.")

correct_answer = "C" and "c"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! Идем дальше...")
    right_answers = right_answers + 1
else:
    print("Не правильно(")

# ----------------------------------------------------------------------------------------------------------------------

print("\n10. Тип жилища у андроновцев:")
print("A) пещера")
print("B) землянка")
print("C) глинобитный дом")
print("D) шалаш")

correct_answer = "B" and "b"
user_answer = input("Введите Ваш ответ: ")

if user_answer == correct_answer:
    print("Правильно! QUIZ завершен!")
    right_answers = right_answers + 1
else:
    print("Не правильно( QUIZ завершен!")

# ----------------------------------------------------------------------------------------------------------------------

print("\nСпасибо за участие в нашем QUIZ!")

if right_answers == 0:
    print("Вы не ответили правильно ни на один вопрос, повезет в следующий раз)")
elif right_answers == 1:
    print("Вы ответили правильно на 1 вопрос")
elif 4 >= right_answers > 1:
    print("Вы ответили правильно на", right_answers, "вопроса")
else:
    print("Вы ответили правильно на", right_answers, "вопросов")