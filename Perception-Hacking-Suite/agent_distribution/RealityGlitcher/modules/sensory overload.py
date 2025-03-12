import pygame

def generate_visual_noise(screen_width, screen_height):
    """Generates visual noise by randomly changing pixel colors."""
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Reality Glitcher")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for x in range(screen_width):
            for y in range(screen_height):
                screen.set_at((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # Example usage
    screen_width = 800
    screen_height = 600
    generate_visual_noise(screen_width, screen_height)