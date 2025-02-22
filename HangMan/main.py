import random

# Список слов для игры
words = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]

# Функция для выбора случайного слова
def choose_word():
    return random.choice(words)

# Функция для отображения текущего состояния виселицы
def display_hangman(tries):
    stages = [  # Финальное состояние: голова, торс, обе руки, обе ноги
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Голова, торс, обе руки, одна нога
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # Голова, торс, обе руки
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # Голова, торс, одна рука
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # Голова, торс
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # Голова
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Начальное состояние
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# Основная функция игры
def hangman():
    word = choose_word()
    word_completion = "* " * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давайте играть в виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Пожалуйста, введите букву или слово: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже называли эту букву", guess)
            elif guess not in word:
                print(guess, "нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отлично,", guess, "есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже называли это слово", guess)
            elif guess != word:
                print(guess, "не является правильным словом.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Неверный ввод.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Поздравляю, вы угадали слово! Вы победили!")
    else:
        print("Извините, у вас закончились попытки. Загаданное слово было " + word + ". Может быть, в следующий раз!")

# Запуск игры
if __name__ == "__main__":
    hangman()