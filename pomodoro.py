import pygame
import sys
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH = 400
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pomodoro Timer')

def print_github_link():
    font = pygame.font.Font(None, 16)
    text = font.render("GitHub: github.com/mateusartico", True, BLACK)
    text_rect = text.get_rect(center=(100, 10))
    screen.blit(text, text_rect)

def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

def format_time(seconds):
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return '{:02}:{:02}'.format(int(minutes), int(seconds))

def draw_clock(seconds, color):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 100)
    timer = format_time(seconds)
    text = font.render(timer, True, color)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 3))
    screen.blit(text, text_rect)

def update_screen(seconds, color, button_text):
    draw_clock(seconds, color)
    draw_button(90, 200, 100, 50, BLACK, button_text)
    draw_button(210, 200, 100, 50, BLACK, "RESET")
    print_github_link()
    pygame.display.flip()

def reset_game():
    return 1500, "START", False

def pomodoro():
    seconds, button_text, started = reset_game()
    fps = 0

    while seconds != 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(90, 200, 100, 50).collidepoint(event.pos):
                    started = not started
                    button_text = "PAUSE" if started else "START"
                elif pygame.Rect(210, 200, 100, 50).collidepoint(event.pos):
                    seconds, button_text, started = reset_game()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update_screen(seconds, BLACK, button_text)
        pygame.display.update()

        if started:
            if fps == 10:
                seconds -= 1
                fps = 0
            fps += 1
            time.sleep(0.1)

    seconds = 300
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()

    while seconds != 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(90, 200, 100, 50).collidepoint(event.pos):
                    started = not started
                    button_text = "PAUSE" if started else "START"
                elif pygame.Rect(210, 200, 100, 50).collidepoint(event.pos):
                    return 0
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        update_screen(seconds, RED, button_text)
        pygame.display.update()

        if started:
            if fps == 10:
                seconds -= 1
                fps = 0
            fps += 1
            time.sleep(0.1)

def main():
    while True:
        pomodoro()

if __name__ == '__main__':
    main()