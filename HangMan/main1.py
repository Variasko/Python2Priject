import random

# Список слов для игры
words = ["кот", "собака", "дом", "солнце", "школа", "игра"]

# Выбираем случайное слово
word = random.choice(words)

# Создаем строку с подчеркиваниями для отображения угаданных букв
hidden_word = "_" * len(word)

# Количество попыток
tries = 6

# Список для угаданных букв
guessed_letters = []

print("Добро пожаловать в игру 'Виселица'!")
print("Угадай слово, вводя по одной букве. У тебя 6 попыток.")

# Основной цикл игры
while tries > 0 and "_" in hidden_word:
    print("\nСлово:", hidden_word)
    print("Осталось попыток:", tries)
    guess = input("Введи букву: ").lower()  # Переводим ввод в нижний регистр

    # Проверяем, что введена одна буква
    if len(guess) != 1 or not guess.isalpha():
        print("Пожалуйста, введи только одну букву!")
        continue

    # Если буква уже была угадана
    if guess in guessed_letters:
        print("Ты уже называл эту букву!")
        continue

    # Добавляем букву в список угаданных
    guessed_letters.append(guess)

    # Если буква есть в слове
    if guess in word:
        print("Молодец, буква", guess, "есть в слове!")
        # Обновляем скрытое слово
        new_hidden_word = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_hidden_word += guess
            else:
                new_hidden_word += hidden_word[i]
        hidden_word = new_hidden_word
    else:
        print("К сожалению, буквы", guess, "нет в слове.")
        tries -= 1  # Уменьшаем количество попыток

# Конец игры
if "_" not in hidden_word:
    print("\nПоздравляю! Ты угадал слово:", word)
else:
    print("\nУвы, попытки закончились. Загаданное слово было:", word)