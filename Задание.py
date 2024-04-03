import pygame
import sys

# Инициализация библиотеки pygame
pygame.init()

# Установка размеров окна для отображения круга
win_width = 500
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Drawing a circle")

# Задаем цвета
white = (255, 255, 255)  # RGB - белый цвет
black = (0, 0, 0)        # RGB - черный цвет

# Определяем параметры круга
radius = 50
circle_x = 250
circle_y = 250

# Цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка экрана белым цветом
    window.fill(white)

    # Рисуем круг на экране
    pygame.draw.circle(window, black, (circle_x, circle_y), radius)

    # Обновление экрана
    pygame.display.update()

# Выход из игры
pygame.quit()
sys.exit()