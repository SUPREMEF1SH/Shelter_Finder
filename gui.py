import sys
import pygame
import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("City Selection")

def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, constants.GRAY, (x, y, width, height))
    font = pygame.font.SysFont(None, 40)
    text_surface = font.render(text, True, constants.BLACK)
    screen.blit(text_surface, (x + 10, y + 10))

def check_button_click(mouse_pos, x, y, width, height):
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

def draw_input_box(user_text, input_description):
    font = pygame.font.SysFont(None, 40)

    instruction_surface = font.render(input_description, True, constants.BLACK)
    screen.blit(instruction_surface, (50, 100))

    input_box = pygame.Rect(50, 150, 300, 50)
    pygame.draw.rect(screen, constants.GRAY, input_box)

    user_input_surface = font.render(user_text, True, constants.BLACK)
    screen.blit(user_input_surface, (input_box.x + 10, input_box.y + 10))

    return user_text

def process_user_input(user_text):
    city_coords = constants.get_city_coordinates(user_text)
    if city_coords:
        return user_text
    else:
        print("City not found.")
        return None

def handle_text_input(event, user_text, input_active):
    if event.type == pygame.KEYDOWN and input_active:
        if event.key == pygame.K_RETURN:
            return '', process_user_input(user_text)
        elif event.key == pygame.K_BACKSPACE:
            return user_text[:-1], None
        else:
            return user_text + event.unicode, None
    return user_text, None

def open_user_input_window():
    running = True
    input_active = False
    user_text = ''

    while running:
        screen.fill(constants.WHITE)

        user_city = draw_input_box(user_text, "Enter city name:")
        draw_button("Go Back", 50, 250, 200, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if check_button_click(mouse_pos, 50, 250, 200, 50):
                    running = False

                input_box = pygame.Rect(50, 150, 300, 50)
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False

            user_text, selected_city = handle_text_input(event, user_text, input_active)
            if selected_city:
                return selected_city

def main_menu():
    running = True
    while running:
        screen.fill(constants.WHITE)

        # Draw the buttons
        draw_button("User", 200, 100, 200, 50)
        draw_button("Admin", 200, 170, 200, 50)
        draw_button("Manager", 200, 240, 200, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check which button was clicked
                if check_button_click(mouse_pos, 200, 100, 200, 50):
                    return open_user_input_window()
                elif check_button_click(mouse_pos, 200, 170, 200, 50):
                    print("Admin Selected")
                elif check_button_click(mouse_pos, 200, 240, 200, 50):
                    print("Manager Selected")

def run_gui():
    return main_menu()

if __name__ == "__main__":
    run_gui()
