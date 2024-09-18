import sys

import pygame

import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("main menu")


# Function to draw a button
def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, constants.GRAY, (x, y, width, height))  # Draw the button rectangle
    font = pygame.font.SysFont(None, 40)  # Font for the button text
    text_surface = font.render(text, True, constants.BLACK)  # Render the text
    screen.blit(text_surface, (x + 10, y + 10))  # Display text on the button


# Function to handle button click events
def check_button_click(mouse_pos, x, y, width, height):
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        return True  # Return True if the button is clicked
    return False


# Function to open a new window based on the option clicked, with a Go Back button
def open_option_window(option_text):
    running = True
    while running:
        screen.fill(constants.WHITE)  # Set background color to white
        font = pygame.font.SysFont(None, 55)
        text_surface = font.render(option_text, True, constants.BLACK)  # Show the selected option text
        screen.blit(text_surface, (constants.SCREEN_WIDTH // 4, constants.SCREEN_HEIGHT // 3))

        # Draw the "Go Back" button
        draw_button("Go Back", 200, 300, 200, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Exit if the window is closed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position

                # Check if "Go Back" button is clicked
                if check_button_click(mouse_pos, 200, 300, 200, 50):
                    running = False  # Go back to the main menu


# Main function for the menu
def main_menu():
    running = True
    while running:
        screen.fill(constants.WHITE)  # Set background color to white

        # Draw the three buttons
        draw_button("User", 200, 100, 200, 50)
        draw_button("Admin", 200, 170, 200, 50)
        draw_button("Manager", 200, 240, 200, 50)

        pygame.display.flip()  # Update the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Exit if the window is closed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position

                # Check which button was clicked
                if check_button_click(mouse_pos, 200, 100, 200, 50):
                    open_option_window("User Selected")
                elif check_button_click(mouse_pos, 200, 170, 200, 50):
                    open_option_window("Admin Selected")
                elif check_button_click(mouse_pos, 200, 240, 200, 50):
                    open_option_window("manager Selected")


# Run the main menu
main_menu()
