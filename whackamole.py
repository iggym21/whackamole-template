import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_x = 0
        mole_y = 0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    mouse_pos_list = [mouse_pos[0], mouse_pos[1]]
                    new_mouse_pos_list = [(x//32) for x in mouse_pos_list]

                    if new_mouse_pos_list == [mole_x, mole_y]:
                        mole_x = random.randrange(0, 20)
                        mole_y = random.randrange(0, 16)
            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "dark green", (0, 32*i), (640, 32*i))
            for i in range(20):
                pygame.draw.line(screen, "dark green", (32*i, 0), (32*i, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*32, mole_y*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
