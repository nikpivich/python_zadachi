import random


def get_user_choice():
    """Получить выбор пользователя."""
    print("Выберите: камень, ножницы, бумага")
    user_choice = input().lower()
    while user_choice not in ["камень", "ножницы", "бумага"]:
        print("Некорректный ввод. Пожалуйста, выберите камень, ножницы или бумагу.")
        user_choice = input().lower()
    return user_choice


def get_computer_choice(prev_user_choice):
    """Получить выбор компьютера."""
    choices = ["камень", "ножницы", "бумага"]

    # Простой алгоритм для выбора следующего хода компьютера
    if prev_user_choice:
        prev_index = choices.index(prev_user_choice)
        next_index = (prev_index + 1) % len(choices)
        return choices[next_index]
    else:
        return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Определить победителя в игре."""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
            (user_choice == "камень" and computer_choice == "ножницы") or
            (user_choice == "ножницы" and computer_choice == "бумага") or
            (user_choice == "бумага" and computer_choice == "камень")
    ):
        return "Вы победили!"
    else:
        return "Компьютер победил!"


def play_game():
    """Запустить игру."""
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice(user_choice)

        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "победили" in result:
            user_score += 1
        elif "победил" in result:
            computer_score += 1

        print(f"Счет: Вы {user_score}, Компьютер {computer_score}")

        print("Хотите сыграть еще раз? (да/нет)")
        play_again = input().lower()
        if play_again != "да":
            break


if __name__ == "__main__":
    play_game()