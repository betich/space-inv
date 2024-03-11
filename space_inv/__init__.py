import pygame
import sys

def main():
  # Initialize Pygame
  pygame.init()

  # Screen dimensions
  screen_width = 800
  screen_height = 600

  # Create the display surface
  screen = pygame.display.set_mode((screen_width, screen_height))

  # Set the title of the window
  pygame.display.set_caption('Keyboard Movement and Shooting Example')

  # Load the background image
  background = pygame.image.load('s3.png')  # Replace 'background.png' with your background image file

  # Load the spaceship image
  image = pygame.image.load('s3.png')  # Replace with your spaceship image

  # Load the bullet image
  bullet_img = pygame.image.load('bullet3.png')  # Replace with your bullet image

  # Spaceship position
  image_x = screen_width // 2
  image_y = screen_height // 2
  x_change = 0
  y_change = 0
  # Movement speed
  speed = 5

  # Bullet properties
  bullet_speed = 10
  bullet_x = 0
  bullet_y = 0
  bullet_state = "ready"  # "ready" or "fire"

  def fire_bullet(x, y):
      global bullet_state
      bullet_state = "fire"
      screen.blit(bullet_img, (x + 16, y + 10))

  # Main game loop
  running = True
  while running:
      screen.fill('black')
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          # Key down events
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  x_change = -speed
              elif event.key == pygame.K_RIGHT:
                  x_change = speed
              elif event.key == pygame.K_UP:
                  y_change = -speed
              elif event.key == pygame.K_DOWN:
                  y_change = speed
              elif event.key == pygame.K_SPACE:
                  if bullet_state == "ready":
                      bullet_x = image_x
                      bullet_y = image_y
                      fire_bullet(bullet_x, bullet_y)
          # Key up events
          if event.type == pygame.KEYUP:
              if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                  x_change = 0
              if event.key in (pygame.K_UP, pygame.K_DOWN):
                  y_change = 0

      # Update spaceship position
      image_x += x_change
      image_y += y_change

      # Prevent the spaceship from going out of bounds
      if image_x < 0:
          image_x = 0
      elif image_x > screen_width - image.get_width():
          image_x = screen_width - image.get_width()

      if image_y < 0:
          image_y = 0
      elif image_y > screen_height - image.get_height():
          image_y = screen_height - image.get_height()

      # Draw the background
      screen.blit(background, (0, 0))

      # Draw the spaceship
      screen.blit(image, (image_x, image_y))

      # Bullet movement
      if bullet_state == "fire":
          fire_bullet(bullet_x, bullet_y)
          bullet_y -= bullet_speed
      if bullet_y < 0:
          bullet_y = image_y
          bullet_state = "ready"

      # Update the display
      pygame.display.flip()

      # Frame rate
      pygame.time.Clock().tick(60)

  # Quit Pygame
  pygame.quit()
  sys.exit()


if __name__ == "__main__":
  main()