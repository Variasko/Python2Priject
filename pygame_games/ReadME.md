## 1. Основы

Базовый __шаблон__ игры на PyGame представлен в файле lp1.py

Основные моменты:

1. Импорт библиотеки
```python
import pygame
```
2. Инициализация библиотеки
```python
pygame.init()
```
3. Создание основных переменных
```python
W = 800 # ширина
H = 600 # высота
```
4. Создание окна и добавление ему заголовка
```python
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Моя первая игра")
```
5. Основной цикл игры, событие выхода и заливка экрана цветом
```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    screen.fill((0, 0, 0))  # Заполнение экрана черным цветом
    pygame.display.flip()
```
6. Принудительных выход, в непредвиденных ситуациях

```python
pygame.quit()
```
7. Повторное, построчное объяснение
   - `import pygame`: Импортируем библиотеку Pygame.
   - `pygame.init()`: Инициализируем все модули Pygame.
   - `screen = pygame.display.set_mode((800, 600))`: Создаем окно размером 800x600 пикселей.
   - `pygame.display.set_caption("Моя первая игра")`: Устанавливаем заголовок окна.
   - `running = True`: Переменная для управления основным циклом игры.
   - `while running:`: Основной цикл игры, который будет выполняться до тех пор, пока `running` равно `True`.
   - `for event in pygame.event.get():`: Обработка событий (например, закрытие окна).
   - `if event.type == pygame.QUIT:`: Если событие — закрытие окна, то `running` становится `False`, и цикл завершается.
   - `screen.fill((0, 0, 0))`: Заполняем экран черным цветом.
   - `pygame.display.flip()`: Обновляем экран.
   - `pygame.quit()`: Завершаем работу Pygame.