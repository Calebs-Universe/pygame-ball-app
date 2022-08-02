import pygame

pygame.init()

WIN = pygame.display.set_mode((500, 500))

def draw_ball(x:int, y:int, radius:int):
    pygame.draw.circle(WIN, (128, 10, 200), (x, y), radius)

def main():
    run = True
    x, y = 250, 250
    radius = 50
    clock = pygame.time.Clock()
    while run:
        # Setting the background color
        WIN.fill(pygame.Color('gray'))
        # To make sure the game runs at 60 FPS
        fps = clock.tick(60)
        dt = 1/fps
        # To display the ball
        draw_ball(x, y, radius)

        # Check for closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Check key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 2 * dt * 30 # Multipling by dt * 30 is to ensure a smooth and uniform movement
        elif keys[pygame.K_RIGHT]:
            x += 2 * dt * 30
        elif keys[pygame.K_UP]:
            y -= 2 * dt * 30
        elif keys[pygame.K_DOWN]:
            y += 2 * dt * 30

        # Check for wall collisions
        if x-radius < 0: x = radius # Collision with left border
        if x+radius > 500: x = 500-radius # Collision with right border
        if y-radius < 0: y = radius # Collision with top border
        if y+radius > 500: y = 500 - radius # Collision with bottom border
        
        # To update the display on the pygame window
        pygame.display.update()

    # It closes the pygame window
    pygame.quit()

if __name__ == "__main__":
    main()
