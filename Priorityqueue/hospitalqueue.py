import pygame
import adaptablepriorityqueue as pq
import button as b

pygame.init()  # initialize pygame

# constants
WIDTH, HEIGHT = 800, 600  # set width and height

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# title
pygame.display.set_caption("Hospital")

# load reception
reception = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/receptionist.png")  # load reception image
receptionWidth, receptionHeight = reception.get_size()  # get size of reception

# load smaller people image
person = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/people.png")
person = pygame.transform.scale(person, (200, 200))  # resize the people image

# load buttons' images
addimg = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_add-patient.png").convert_alpha()  # load add image
# addimg = pygame.transform.scale(addimg1, (175, 57))  # resize the add image
removeminImg = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_remove-min.png").convert_alpha()  # load remove min image
removeanyImg = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_remove-any.png").convert_alpha()  # load remove any image
len_Img = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_length.png").convert_alpha()  # load length image
is_empty_Img = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_is-empty.png").convert_alpha()  # load is empty image
update_priority_Img = pygame.image.load("/home/keith/Documents/Code/ics2301Ass/Priorityqueue/assets/button_update-priority.png").convert_alpha()  # load update priority image
# update_priority_Img = pygame.transform.scale(update_priority_Img1, (175, 57))  # resize the update priority image

# create button instances
add_button = b.Button(400, 50, addimg)
removemin = b.Button(600, 50, removeminImg)
removeany = b.Button(400, 130, removeanyImg)
len_ = b.Button(642, 130, len_Img)
is_empty = b.Button(621, 210, is_empty_Img)
update_priority = b.Button(400, 210, update_priority_Img)

# create queue
priority_queue = pq.AdaptableHeapPriorityQueue()

# Fonts
font = pygame.font.Font(None, 32)
message_font = pygame.font.Font(None, 36)

nameVal = ""
keyVal = ""
nameRectActive = False
keyRectActive = False
nameState = False
keyState = False
newPriorityVal = ""
newPriorityRectActive = False

running = True  # set running to true
while running:  # while running is true
    for event in pygame.event.get():  # for all events
        if event.type == pygame.QUIT:  # if the event is quit
            running = False  # set running to false

        if event.type == pygame.MOUSEBUTTONDOWN:
            nameRectActive = input_rect_name.collidepoint(event.pos)
            keyRectActive = input_rect_key.collidepoint(event.pos)

            if add_button.draw(screen):
                try:
                    patient_age = int(keyVal)
                    patient_name = nameVal
                    priority_queue.add(patient_age, patient_name)
                    priority_queue.print_contents()
                    nameVal = ""
                    keyVal = ""
                except ValueError:
                    print("Invalid age. Please enter an integer.")
                    # Draw a message box showing whether empty is true or false
                    message_text = message_font.render("Invalid data entered!!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)  

            if removemin.draw(screen):
                try:
                    removed_patient = priority_queue.remove_min()
                    print(f"Removed patient with min priority: {removed_patient}")
                    # Draw a message box showing whether empty is true or false
                    priority_queue.print_contents()
                    message_text = message_font.render("Removed " + removed_patient[1], True, (0, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)  
                except pq.Empty as e:
                    print(e)
                    # Draw a message box showing whether empty is true or false
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
                    # patients = [patient for patient in patients if patient != removed_patient]
                    print(f"Removed patient: {removed_patient}")
                    priority_queue.remove(removed_patient_priority, removed_patient_name)
                    priority_queue.print_contents()
                    nameVal = ""
                    keyVal = ""
                    # Draw a message box showing whether empty is true or false
                    message_text = message_font.render("Removed patient: "+ removed_patient[0], True, (0, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)  
                except ValueError:
                    print("Invalid input. Please enter a valid name and priority.")
                    nameVal = ""
                    keyVal = ""
                    # Draw a message box showing whether empty is true or false
                    message_text = message_font.render("Invalid input!!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000)  
                if priority_queue.is_empty():
                    print("No patients to remove.")
                    # Draw a message box showing whether empty is true or false
                    message_text = message_font.render("No patients to remove!!", True, (255, 0, 0))
                    message_rect = message_text.get_rect(center=(150, 200))
                    screen.blit(message_text, message_rect.topleft)

                    pygame.display.flip()
                    pygame.time.delay(1000) 

            if len_.draw(screen):
                print(f"Queue length: {len(priority_queue)}")
                pr_len = str(len(priority_queue))
                # Draw a message box showing whether empty is true or false
                message_text = message_font.render("Queue length: " + pr_len, True, (0, 0, 0))
                message_rect = message_text.get_rect(center=(150, 200))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(1000) 

            if is_empty.draw(screen):
                print(f"Is the queue empty? {priority_queue.is_empty()}")
                pr_empty = str(priority_queue.is_empty())
                # Draw a message box showing whether empty is true or false
                message_text = message_font.render("Is the queue empty?" + pr_empty, True, (0, 0, 0))
                message_rect = message_text.get_rect(center=(150, 200))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(1000) 
                
            if update_priority.draw(screen):
                try:
                    # patient_name = nameVal
                    # patient_priority = int(keyVal)
                    # priority_queue.update_priority(patient_priority, patient_name, patient_priority)
                    # priority_queue.print_contents()
                    # nameVal = ""
                    # keyVal = ""
                    input_rect_new_priority = pygame.Rect(150, 130, 140, 32)
                    pygame.draw.rect(screen, (255, 255, 255), input_rect_new_priority)
                    pygame.draw.rect(screen, (0, 0, 0), input_rect_new_priority, 2)
                    text_new_priority = font.render(str(newPriorityVal), True, (0, 0, 0))
                    screen.blit(text_new_priority, (input_rect_new_priority.x + 5, input_rect_new_priority.y + 5))
                    input_rect_new_priority.w = max(100, text_new_priority.get_width() + 10)

                    newPriorityText = message_font.render("New Priority: ", True, (0, 0, 0))
                    newPriorityRect = newPriorityText.get_rect(center=(100, 150))
                    screen.blit(newPriorityText, newPriorityRect.topleft)
                    newPriorityVal = ""  # Clear the new priority field
                    newPriorityRectActive = True  # Activate the new priority field
                except ValueError:
                    print("Invalid input. Please enter a valid name and priority.")
                    nameVal = ""
                    keyVal = ""
                    newPriorityVal = ""
                    newPriorityRectActive = False

        if event.type == pygame.KEYDOWN:
            if nameRectActive:
                if event.key == pygame.K_RETURN:
                    print("Name:", nameVal)
                    nameVal = ""
                elif event.key == pygame.K_BACKSPACE:
                    nameVal = nameVal[:-1]
                else:
                    nameVal += event.unicode

            if keyRectActive:
                if event.key == pygame.K_RETURN:
                    try:
                        keyVal = int(keyVal)
                        print("Age:", keyVal)
                    except ValueError:
                        print("Invalid age. Please enter an integer.")
                        keyVal = ""
                elif event.key == pygame.K_BACKSPACE:
                    keyVal = keyVal[:-1]
                else:
                    keyVal += event.unicode
                    
                if newPriorityRectActive:
                    if event.key == pygame.K_RETURN:
                        try:
                            new_priority = int(newPriorityVal)
                            print("New Priority:", new_priority)
                            patient_name = nameVal
                            patient_priority = int(keyVal)
                            priority_queue.update_priority(patient_priority, patient_name, new_priority)
                            priority_queue.print_contents()
                            nameVal = ""
                            newPriorityVal = ""
                            newPriorityRectActive = False
                        except ValueError:
                            print("Invalid priority. Please enter an integer.")
                            newPriorityVal = ""
                    elif event.key == pygame.K_BACKSPACE:
                        newPriorityVal = newPriorityVal[:-1]
                    else:
                        newPriorityVal += event.unicode

    screen.fill((255, 255, 255))

    input_rect_name = pygame.Rect(150, 50, 140, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect_name)
    pygame.draw.rect(screen, (0, 0, 0), input_rect_name, 2)
    text = font.render(nameVal, True, (0, 0, 0))
    screen.blit(text, (input_rect_name.x + 5, input_rect_name.y + 5))
    input_rect_name.w = max(100, text.get_width() + 10)

    input_rect_key = pygame.Rect(150, 90, 140, 32)
    pygame.draw.rect(screen, (255, 255, 255), input_rect_key)
    pygame.draw.rect(screen, (0, 0, 0), input_rect_key, 2)
    text_key = font.render(str(keyVal), True, (0, 0, 0))
    screen.blit(text_key, (input_rect_key.x + 5, input_rect_key.y + 5))
    input_rect_key.w = max(100, text_key.get_width() + 10)
    
    # input_rect_new_priority = pygame.Rect(150, 130, 140, 32)
    # pygame.draw.rect(screen, (255, 255, 255), input_rect_new_priority)
    # pygame.draw.rect(screen, (0, 0, 0), input_rect_new_priority, 2)
    # text_new_priority = font.render(str(newPriorityVal), True, (0, 0, 0))
    # screen.blit(text_new_priority, (input_rect_new_priority.x + 5, input_rect_new_priority.y + 5))
    # input_rect_new_priority.w = max(100, text_new_priority.get_width() + 10)

    # newPriorityText = message_font.render("New Priority: ", True, (0, 0, 0))
    # newPriorityRect = newPriorityText.get_rect(center=(100, 150))
    # screen.blit(newPriorityText, newPriorityRect.topleft)

    nameText = message_font.render("Name: ", True, (0, 0, 0))
    nameRect = nameText.get_rect(center=(110, 70))
    screen.blit(nameText, nameRect.topleft)

    keyText = message_font.render("Priority: ", True, (0, 0, 0))
    keyRect = keyText.get_rect(center=(100, 100))
    screen.blit(keyText, keyRect.topleft)

    # Draw reception
    screen.blit(reception, (0, 370))

    # Draw patients
    for i, patient in enumerate(reversed(priority_queue)):
        screen.blit(person, (200 + i * 100, 400))  # increased spacing
        patient_text = message_font.render(f"{patient[1]} - {patient[0]}", True, (0, 0, 0))
        screen.blit(patient_text, (270 + i * 100, 350))  # increased spacing
        

    # Draw buttons
    add_button.draw(screen)
    removemin.draw(screen)
    removeany.draw(screen)
    len_.draw(screen)
    is_empty.draw(screen)
    update_priority.draw(screen)

    pygame.display.update()  # update screen
    pygame.time.delay(25)

pygame.quit()  # quit pygame
