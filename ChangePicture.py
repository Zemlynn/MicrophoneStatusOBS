import pygame
import sys
import keyboard  # Import the keyboard library

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Microphone Status')

# Load images
image1 = pygame.image.load(r'LOCATIONofYourPictures')
image2 = pygame.image.load(r'LOCATIONofYourPictures')

# Scale images to fit the screen if necessary
image1 = pygame.transform.scale(image1, (screen_width, screen_height))
image2 = pygame.transform.scale(image2, (screen_width, screen_height))

# Variable to track current image
current_image = image1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for global key presses (works even when the window is not focused)
    if keyboard.is_pressed('k'):  # K key
        # Toggle between images
        current_image = image2 if current_image == image1 else image1
        # Optional: Add a delay to prevent multiple toggles on a single key press
        pygame.time.wait(1000)  # 200 ms delay

    if keyboard.is_pressed('l'):  # L key
        # Toggle between images
        current_image = image1 if current_image == image2 else image2
        # Optional: Add a delay to prevent multiple toggles on a single key press
        pygame.time.wait(1000)  # 200 ms delay
    # Draw current image
    screen.blit(current_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Print message before quitting
print("Exiting... Press Enter to close the terminal.")

# Quit Pygame
pygame.quit()
sys.exit()
