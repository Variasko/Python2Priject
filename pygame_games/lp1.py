import pygame

# Инициализация Pygame
pygame.init()

# Объявление переменных
W = 800
H = 600

# Создание окна
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Моя первая игра")

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    screen.fill((0, 0, 0))  # Заполнение экрана черным цветом
    pygame.display.flip()

pygame.quit()