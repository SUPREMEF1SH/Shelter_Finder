import sys
import pygame
import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")


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


# Draw the input box and instructions
def draw_input_box(user_text, input_description):
  font = pygame.font.SysFont(None, 40)

  # Draw instructions
  instruction_surface = font.render(input_description, True, constants.BLACK)
  screen.blit(instruction_surface, (50, 100))

  # Draw the input box.
  input_box = pygame.Rect(50, 150, 300, 50)
  pygame.draw.rect(screen, constants.GRAY, input_box)

  # Render the current user input text
  user_input_surface = font.render(user_text, True, constants.BLACK)
  screen.blit(user_input_surface, (input_box.x + 10, input_box.y + 10))
  return user_text


# Process user input (Enter key to show coordinates)
def process_user_input(user_text):
  city_coords = constants.get_city_coordinates(user_text)
  if city_coords:
    print(f"Coordinates of {user_text}: {city_coords}")
    return [user_text, city_coords]
  else:
    print("City not found.")


# Handle text input events (keyboard interactions)
def handle_text_input(event, user_text, input_active):
  if event.type == pygame.KEYDOWN and input_active:
    if event.key == pygame.K_RETURN:
      process_user_input(user_text)
      return ''  # Clear text after processing input
    elif event.key == pygame.K_BACKSPACE:
      return user_text[:-1]  # Remove last character
    else:
      return user_text + event.unicode  # Add typed character
  return user_text


# Function to open a window for user input
def open_user_input_window():
  running = True
  input_active = False  # Track if the input box is active for typing
  user_text = ''  # Text input by the user

  while running:
    screen.fill(constants.WHITE)  # Set background color to white

    # Draw input box and button
    user_city = draw_input_box(user_text, "Enter city name:")
    draw_button("Go Back", 50, 250, 200, 50)

    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()  # Exit if the window is closed
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()

        # Check if "Go Back" button is clicked
        if check_button_click(mouse_pos, 50, 250, 200, 50):
          running = False  # Go back to the main menu

        # Check if the input box is clicked to activate text input
        input_box = pygame.Rect(50, 150, 300, 50)
        if input_box.collidepoint(event.pos):
          input_active = True
        else:
          input_active = False

      # Handle keyboard input for text
      user_text = handle_text_input(event, user_text, input_active)


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
          open_user_input_window()  # Open user input window
        elif check_button_click(mouse_pos, 200, 170, 200, 50):
          open_option_window("Admin Selected")
        elif check_button_click(mouse_pos, 200, 240, 200, 50):
          open_option_window("Manager Selected")


# Run the main menu
main_menu()
