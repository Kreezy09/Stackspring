import pygame
import priorityqueue as pq
import button as b

pygame.init()  # initialize pygame

# constants
WIDTH, HEIGHT = 800, 600  # set width and height

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# title
pygame.display.set_caption("Hospital")

# load reception
reception = pygame.image.load("receptionist.png")  # load reception image
receptionWidth, receptionHeight = reception.get_size()  # get size of reception

# load smaller people image
person = pygame.image.load("people.png")
person = pygame.transform.scale(person, (200, 200))  # resize the people image

# load buttons' images
addimg = pygame.image.load("button_add-patient.png").convert_alpha()  # load add image
removeminImg = pygame.image.load("button_remove-min.png").convert_alpha()  # load remove min image
removeanyImg = pygame.image.load("button_remove-any.png").convert_alpha()  # load remove any image
len_Img = pygame.image.load("button_length.png").convert_alpha()  # load length image
is_empty_Img = pygame.image.load("button_is-empty.png").convert_alpha()  # load is empty image

# create button instances
add_button = b.Button(300, 50, addimg)
removemin = b.Button(550, 50, removeminImg)
removeany = b.Button(300, 130, removeanyImg)
len_ = b.Button(556, 130, len_Img)
is_empty = b.Button(500, 210, is_empty_Img)

# create queue
priority_queue = pq.SortedPriorityQueue()

# Fonts
font = pygame.font.Font(None, 32)
message_font = pygame.font.Font(None, 36)

nameVal = ""
keyVal = ""
nameRectActive = False
keyRectActive = False
nameState = False
keyState = False

patients = []  # to store patient data

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
                    patients.append((patient_name, patient_age))
                    patients.sort(key=lambda x: x[1], reverse=True)  # sort patients by priority
                    print(f"Added patient: {patient_name} with age {patient_age}")
                    nameVal = ""
                    keyVal = ""
                except ValueError:
                    print("Invalid age. Please enter an integer.")

            if removemin.draw(screen):
                try:
                    removed_patient = priority_queue.remove_min()
                    print(f"Removed patient with min priority: {removed_patient}")
                    # Remove the patient visually
                    if patients:
                        patients = sorted(patients, key=lambda x: x[1], reverse=True)
                        patients.pop()
                except pq.Empty as e:
                    print(e)

            if removeany.draw(screen):
                if patients:
                    # Remove the specified patient visually and from the queue
                    try:
                        removed_patient_name = nameVal
                        removed_patient_priority = int(keyVal)
                        removed_patient = (removed_patient_name, removed_patient_priority)
                        patients = [patient for patient in patients if patient != removed_patient]
                        print(f"Removed patient: {removed_patient}")
                        priority_queue.remove(removed_patient_priority, removed_patient_name)
                    except ValueError:
                        print("Invalid input. Please enter a valid name and priority.")
                else:
                    print("No patients to remove.")

            if len_.draw(screen):
                print(f"Queue length: {len(priority_queue)}")

            if is_empty.draw(screen):
                print(f"Is the queue empty? {priority_queue.is_empty()}")

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

    nameText = message_font.render("Name: ", True, (0, 0, 0))
    nameRect = nameText.get_rect(center=(110, 70))
    screen.blit(nameText, nameRect.topleft)

    keyText = message_font.render("Priority: ", True, (0, 0, 0))
    keyRect = keyText.get_rect(center=(120, 100))
    screen.blit(keyText, keyRect.topleft)

    # Draw reception
    screen.blit(reception, (0, 370))

    # Draw patients
    for i, patient in enumerate(patients):
        screen.blit(person, (200 + i * 100, 400))  # increased spacing
        patient_text = message_font.render(f"{patient[0]} - {patient[1]}", True, (0, 0, 0))
        screen.blit(patient_text, (270 + i * 100, 350))  # increased spacing

    # Draw buttons
    add_button.draw(screen)
    removemin.draw(screen)
    removeany.draw(screen)
    len_.draw(screen)
    is_empty.draw(screen)

    pygame.display.update()  # update screen
    pygame.time.delay(25)

pygame.quit()  # quit pygame
