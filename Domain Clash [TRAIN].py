import random
import pygame
import time

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WASD_mass = ["w", "a", "s", "d"]
WASD_mass = [random.choice(WASD_mass) for _ in range(len(WASD_mass))]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Domain Clash")
font = pygame.font.Font(None, 36)

start_time = time.time()
running = True
current_index = 0  # Текущий индекс для проверки правильности нажатых клавиш

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == WASD_mass[current_index]:
                print("Correct key pressed:", event.unicode)
                current_index += 1  # Переходим к следующему индексу

                if current_index == len(WASD_mass):
                    end_time = time.time()
                    total_time = end_time - start_time
                    print("All keys pressed correctly! Total time:", total_time)
                    print("Всё верно! Затраченое время:", total_time)
                    running = False
            else:
                print("Wrong key pressed:", event.unicode)

    screen.fill(WHITE)
    for i, key in enumerate(WASD_mass):
        text_color = GREEN if i < current_index else RED  # Зеленый для правильно нажатых, красный для остальных
        text_surface = font.render(key, True, text_color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2 + i * 50, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()
