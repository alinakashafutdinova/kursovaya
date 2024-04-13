import os
import time
import random

# Функция для очистки экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Инициализация размеров экрана
rows, columns = 20, 40

# Инициализация позиции змейки и фрукта
snake = [(rows//2, columns//2)]
fruit = (random.randint(1, rows-2), random.randint(1, columns-2))

# Инициализация направления движения
direction = 'UP'
score = 0

while True:
    clear_screen()

    # Создание игрового поля
    for i in range(rows+2):
        for j in range(columns+2):
            if i == 0 or i == rows+1:
                print("-", end="")
            elif j == 0 or j == columns+1:
                print("|", end="")
            elif (i, j) in snake:
                print("o", end="")
            elif (i, j) == fruit:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    key = input("Введите WASD для управления: ").upper()

    new_head = (snake[0][0], snake[0][1])

    if key == 'W':
        direction = 'UP'
        new_head = (snake[0][0]-1, snake[0][1])
    elif key == 'S':
        direction = 'DOWN'
        new_head = (snake[0][0]+1, snake[0][1])
    elif key == 'A':
        direction = 'LEFT'
        new_head = (snake[0][0], snake[0][1]-1)
    elif key == 'D':
        direction = 'RIGHT'
        new_head = (snake[0][0], snake[0][1]+1)

    if new_head in snake or new_head[0] == 0 or new_head[0] == rows+1 or new_head[1] == 0 or new_head[1] == columns+1:
        print("Game Over!")
        print(f"Ваш счет: {score}")
        break

    snake.insert(0, new_head)

    if new_head == fruit:
        score += 1
        fruit = (random.randint(1, rows-2), random.randint(1, columns-2))
    else:
        snake.pop()

    time.sleep(0.2)