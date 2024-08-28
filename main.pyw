import pygame
import random
from pygame.locals import *
from generator import Generate
from text import text_list, choices_for_text

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text-Based Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

# Load and scale the background image
try:
    background_image = pygame.image.load('background.png')  # Ensure 'background.png' is in your project directory
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    exit()

# Initialize player stats
player_stats = {
    "Gold": 0,
    "Health": 100,
    "Reputation": 50
}

def handle_choice(choice_num, text):
    # Retrieve responses and stats based on text and choice number
    choices = choices_for_text.get(text, {})
    choice = choices.get(choice_num, {"response": "Invalid choice.", "stats": {"Health": 0, "Gold": 0, "Reputation": 0}})
    
    response = choice["response"]
    stats_change = choice["stats"]

    # Apply stats changes
    player_stats["Health"] += stats_change["Health"]
    player_stats["Gold"] += stats_change["Gold"]
    player_stats["Reputation"] += stats_change["Reputation"]

    # Check for death
    if player_stats["Health"] <= 0:
        return "You have died. Game Over."

    return response

def draw_text(text, font, surface, x, y):
    """ Helper function to draw text on the screen """
    textobj = font.render(text, True, WHITE)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_choices(choices):
    """ Draw choices on the screen """
    y = SCREEN_HEIGHT // 2 + 50
    for key, value in choices.items():
        draw_text(f"{key}: {value['response']}", font, screen, SCREEN_WIDTH // 2, y)
        y += 40

def print_stats():
    """ Display player stats on the screen """
    y = SCREEN_HEIGHT - 150
    for stat, value in player_stats.items():
        draw_text(f"{stat}: {value}", font, screen, SCREEN_WIDTH // 2, y)
        y += 30

def main():
    clock = pygame.time.Clock()
    maker = Generate(text_list)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        if not game_over:
            # Draw the background image
            screen.blit(background_image, (0, 0))

            random_text = maker.randomText()
            draw_text(random_text, font, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            
            choices = maker.get_choices(random_text)
            draw_choices(choices)

            print_stats()

            pygame.display.flip()

            user_input = ""
            while user_input not in [str(i) for i in choices.keys()] and not game_over:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        return
                    if event.type == KEYDOWN:
                        if event.key == K_1:
                            user_input = "1"
                        elif event.key == K_2:
                            user_input = "2"
                        elif event.key == K_q:
                            pygame.quit()
                            return

            if user_input:
                choice_num = int(user_input)
                result = handle_choice(choice_num, random_text)
                draw_text(result, font, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                print_stats()
                pygame.display.flip()
                pygame.time.wait(2000)

                if player_stats["Health"] <= 0:
                    game_over = True

if __name__ == "__main__":
    main()
