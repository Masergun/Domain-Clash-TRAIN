import random
import pygame
import time


pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK=(0, 0, 0)

WASD_mass = ["w", "a", "s", "d"]
WASD_nado=[]
for _ in range(10):
    WASD_nado.append(random.choice(WASD_mass))
print(WASD_nado)
SCORE=0

a=0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Domain Clash")
font = pygame.font.Font(None, 36)

start_time = time.time()
running = True
current_index = 0  # Текущий индекс для проверки правильности нажатых клавиш

def socre(SCORE):
    SCORE = str(SCORE)
    score = font.render(SCORE, True, BLACK)
    score_rect = score.get_rect(center=(200, 50))
    screen.blit(score, score_rect)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            end_time = time.time()
            total_time = end_time - start_time
            if len(WASD_nado) < 21:
                WASD_nado.append(random.choice(WASD_mass))
            if len(WASD_nado)> 11:
                WASD_nado.pop(0)
                current_index = current_index - 1

            if event.unicode == WASD_nado[current_index]:
                if a == 0:
                    SCREEN_WIDTH -= 100
                    a=1
                print("Correct key pressed:", event.unicode)
                current_index += 1  # Переходим к следующему индексу
                SCORE=SCORE+1

            else:
                print("Wrong key pressed:", event.unicode)
                print("Score:", SCORE)
                print("Попробуй ещё раз! Затраченое время:", total_time)
                running = False
    screen.fill(WHITE)

    for i, key in enumerate(WASD_nado):
        text_color = GREEN if i < current_index else RED  # Зеленый для правильно нажатых, красный для остальных
        text_surface = font.render(key, True, text_color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2 + i * 50, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        socre(SCORE)
    pygame.display.flip()



pygame.quit()
