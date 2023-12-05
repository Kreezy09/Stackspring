import pygame
import priorityqueue as pq
import button as b

def calculate_priority(severity, age, urgency):
    # Customize this function to calculate priority based on your requirements
    # You can adjust the weights and formulas based on the significance of each factor
    # For simplicity, a basic formula is used here

    severity_weights = {"Very High": 3, "High": 2, "Medium": 1, "Low": 0}
    priority = severity_weights.get(severity, 0) * 10 + age + urgency
    return priority

def show_invalid_input_message(message):
    # Add code to display an error message on the screen
    print(f"Error: {message}")

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital")

reception = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/receptionist.png")
receptionWidth, receptionHeight = reception.get_size()

person = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/people.png")
person = pygame.transform.scale(person, (200, 200))

addimg = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_add-patient.png").convert_alpha()
removeminImg = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_remove-min.png").convert_alpha()
removeanyImg = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_remove-any.png").convert_alpha()
len_Img = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_length.png").convert_alpha()
is_empty_Img = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_is-empty.png").convert_alpha()
update_priority_Img = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_update-priority.png").convert_alpha()

add_button = b.Button(400, 50, addimg)
removemin = b.Button(600, 50, removeminImg)
removeany = b.Button(400, 130, removeanyImg)
len_ = b.Button(642, 130, len_Img)
is_empty = b.Button(621, 210, is_empty_Img)
update_priority = b.Button(400, 210, update_priority_Img)

priority_queue = pq.SortedPriorityQueue()

font = pygame.font.Font(None, 32)
message_font = pygame.font.Font(None, 36)

nameVal = ""
severityVal = ""
ageVal = ""
urgencyVal = ""
updated_patient_name = ""

nameRectActive = False
severityRectActive = False
ageRectActive = False
urgencyRectActive = False
update_priority_active = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            nameRectActive = input_rect_name.collidepoint(event.pos)
            severityRectActive = input_rect_severity.collidepoint(event.pos)
            ageRectActive = input_rect_age.collidepoint(event.pos)
            urgencyRectActive = input_rect_urgency.collidepoint(event.pos)

            if add_button.draw(screen):
                try:
                    patient_severity = severityVal
                    patient_age = int(ageVal)
                    patient_urgency = int(urgencyVal)

                    # Calculate priority based on severity, age, and urgency
                    priority = calculate_priority(patient_severity, patient_age, patient_urgency)

                    patient_name = nameVal
                    priority_queue.add(priority, patient_name)
                    priority_queue.print_contents()
                    nameVal = ""
                    severityVal = ""
                    ageVal = ""
                    urgencyVal = ""
                except ValueError:
                    show_invalid_input_message("Invalid data entered. Please enter valid values.")

            if removemin.draw(screen):
                try:
                    removed_patient = priority_queue.remove_min()
                    print(f"Removed patient with min priority: {removed_patient}")
                    priority_queue.print_contents()
                    message_text = message_font.render("Removed " + removed_patient[1], True, (0, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)
                except pq.Empty as e:
                    show_invalid_input_message(str(e))
                    message_text = message_font.render("Queue is empty!!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)
            
            if removeany.draw(screen):
                try:
                    removed_patient_name = nameVal
                    removed_patient_priority = int(keyVal)
                    removed_patient = (removed_patient_name, removed_patient_priority)
                    priority_queue.remove(removed_patient_priority, removed_patient_name)
                    priority_queue.print_contents()
                    nameVal = ""
                    keyVal = ""
                    message_text = message_font.render("Removed patient: "+ removed_patient[0], True, (0, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)  
                except ValueError:
                    show_invalid_input_message("Invalid input. Please enter a valid name and priority.")
                    nameVal = ""
                    keyVal = ""
                    message_text = message_font.render("Invalid input!!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)  
                except pq.Empty as e:
                    show_invalid_input_message("No patients to remove.")
                    message_text = message_font.render("No patients to remove!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000) 

            if len_.draw(screen):
                print(f"Queue length: {len(priority_queue)}")
                pr_len = str(len(priority_queue))
                message_text = message_font.render("Queue length: " + pr_len, True, (0, 0, 0))
                message_rect = message_text.get_rect(center=(150, 200))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(1000) 

            if is_empty.draw(screen):
                print(f"Is the queue empty? {priority_queue.is_empty()}")
                pr_empty = str(priority_queue.is_empty())
                message_text = message_font.render("Is the queue empty?" + pr_empty, True, (0, 0, 0))
                message_rect = message_text.get_rect(center=(150, 200))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(1000) 
                
            if update_priority.draw(screen):
                try:
                    if not update_priority_active:
                        # If the "Update Priority" button is clicked for the first time
                        updated_patient_name = nameVal
                        nameVal = ""
                        severityVal = ""
                        ageVal = ""
                        urgencyVal = ""
                        update_priority_active = True
                    else:
                        # If the "Update Priority" button is clicked again
                        patient_name = updated_patient_name
                        patient_priority = calculate_priority(severityVal, int(ageVal), int(urgencyVal))
                        priority_queue.update_priority(patient_priority, patient_name)
                        priority_queue.print_contents()
                        nameVal = ""
                        severityVal = ""
                        ageVal = ""
                        urgencyVal = ""
                        update_priority_active = False
                except ValueError:
                    show_invalid_input_message("Invalid input. Please enter valid values.")
                except pq.Empty as e:
                    show_invalid_input_message(str(e))
                    message_text = message_font.render("Queue is empty!!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)

            # ... (similar changes for other buttons)

        if event.type == pygame.KEYDOWN:
            if nameRectActive:
                if event.key == pygame.K_RETURN:
                    print("Name:", nameVal)
                    nameVal = ""
                elif event.key == pygame.K_BACKSPACE:
                    nameVal = nameVal[:-1]
                else:
                    nameVal += event.unicode
            
            if severityRectActive:
                if event.key == pygame.K_RETURN:
                    print("Severity:", severityVal)
                    severityVal = ""
                elif event.key == pygame.K_BACKSPACE:
                    severityVal = severityVal[:-1]
                else:
                    severityVal += event.unicode
            if ageRectActive:
                if event.key == pygame.K_RETURN:
                    print("Age:", ageVal)
                    ageVal = ""
                elif event.key == pygame.K_BACKSPACE:
                    ageVal = ageVal[:-1]
                else:
                    ageVal += event.unicode
            if urgencyRectActive:
                if event.key == pygame.K_RETURN:
                    print("Urgency:", urgencyVal)
                    urgencyVal = ""
                elif event.key == pygame.K_BACKSPACE:
                    urgencyVal = urgencyVal[:-1]
                else:
                    urgencyVal += event.unicode

            # ... (similar changes for other input fields)

    screen.fill((255, 255, 255))

    input_rect_name = pygame.Rect(150, 50, 140, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect_name)
    pygame.draw.rect(screen, (0, 0, 0), input_rect_name, 2)
    text_name = font.render(nameVal, True, (0, 0, 0))
    screen.blit(text_name, (input_rect_name.x + 5, input_rect_name.y + 5))
    input_rect_name.w = max(100, text_name.get_width() + 10)
    
    input_rect_severity = pygame.Rect(150, 90, 140, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect_severity)
    pygame.draw.rect(screen, (0, 0, 0), input_rect_severity, 2)
    text_severity = font.render(severityVal, True, (0, 0, 0))
    screen.blit(text_severity, (input_rect_severity.x + 5, input_rect_severity.y + 5))
    input_rect_severity.w = max(100, text_severity.get_width() + 10)
    
    input_rect_age = pygame.Rect(150, 130, 140, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect_age)
    pygame.draw.rect(screen, (0, 0, 0), input_rect_age, 2)
    text_age = font.render(ageVal, True, (0, 0, 0))
    screen.blit(text_age, (input_rect_age.x + 5, input_rect_age.y + 5))
    input_rect_age.w = max(100, text_age.get_width() + 10)
    
    input_rect_urgency = pygame.Rect(150, 170, 140, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect_urgency)
    pygame.draw.rect(screen, (0, 0, 0), input_rect_urgency, 2)
    text_urgency = font.render(urgencyVal, True, (0, 0, 0))
    screen.blit(text_urgency, (input_rect_urgency.x + 5, input_rect_urgency.y + 5))
    input_rect_urgency.w = max(100, text_urgency.get_width() + 10)
    
    if update_priority_active:
        updated_name_text = message_font.render("Updated Name: " + updated_patient_name, True, (0, 0, 0))
        screen.blit(updated_name_text, (150, 230))

        input_rect_severity = pygame.Rect(150, 270, 140, 32)
        pygame.draw.rect(screen, (255, 255, 255), input_rect_severity)
        pygame.draw.rect(screen, (0, 0, 0), input_rect_severity, 2)
        text_severity = font.render(severityVal, True, (0, 0, 0))
        screen.blit(text_severity, (input_rect_severity.x + 5, input_rect_severity.y + 5))
        input_rect_severity.w = max(100, text_severity.get_width() + 10)

        input_rect_age = pygame.Rect(150, 310, 140, 32)
        pygame.draw.rect(screen, (255, 255, 255), input_rect_age)
        pygame.draw.rect(screen, (0, 0, 0), input_rect_age, 2)
        text_age = font.render(ageVal, True, (0, 0, 0))
        screen.blit(text_age, (input_rect_age.x + 5, input_rect_age.y + 5))
        input_rect_age.w = max(100, text_age.get_width() + 10)

        input_rect_urgency = pygame.Rect(150, 350, 140, 32)
        pygame.draw.rect(screen, (255, 255, 255), input_rect_urgency)
        pygame.draw.rect(screen, (0, 0, 0), input_rect_urgency, 2)
        text_urgency = font.render(urgencyVal, True, (0, 0, 0))
        screen.blit(text_urgency, (input_rect_urgency.x + 5, input_rect_urgency.y + 5))
        input_rect_urgency.w = max(100, text_urgency.get_width() + 10)


    # Add similar changes for other input fields (severity, age, urgency)

    nameText = message_font.render("Name: ", True, (0, 0, 0))
    nameRect = nameText.get_rect(center=(110, 70))
    screen.blit(nameText, nameRect.topleft)

    severityText = message_font.render("Severity: ", True, (0, 0, 0))
    severityRect = severityText.get_rect(center=(110, 110))
    screen.blit(severityText, severityRect.topleft)
    
    ageText = message_font.render("Age: ", True, (0, 0, 0))
    ageRect = ageText.get_rect(center=(110, 150))
    screen.blit(ageText, ageRect.topleft)
    
    urgencyText = message_font.render("Urgency: ", True, (0, 0, 0))
    urgencyRect = urgencyText.get_rect(center=(110, 190))
    screen.blit(urgencyText, urgencyRect.topleft)
    # Add similar changes for other labels (severity, age, urgency)
    
    # Draw reception
    screen.blit(reception, (0, 370))

    # Draw patients
    for i, patient in enumerate(reversed(priority_queue)):
        screen.blit(person, (200 + i * 100, 400))
        patient_text = message_font.render(f"{patient[1]} - {patient[0]}", True, (0, 0, 0))
        screen.blit(patient_text, (270 + i * 100, 350))

    # Draw buttons
    add_button.draw(screen)
    removemin.draw(screen)
    removeany.draw(screen)
    len_.draw(screen)
    is_empty.draw(screen)
    update_priority.draw(screen)

    pygame.display.update()
    pygame.time.delay(25)

pygame.quit()
