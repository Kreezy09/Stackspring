import pygame, Stackspring.button as button, Stackspring.stack as stack

pygame.init() #initialize pygame

#constants
WIDTH, HEIGHT = 800, 600 #set width and height
WHITE = (255, 255, 255)
CANDY_COLOR = (255, 0, 0) 
CANDY_CENTRE = (410, 327)  # Center coordinates
CANDY_RADIUS = 30  # Radius of the circle

#create screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

#title
pygame.display.set_caption("Hospital")

rect_1 = pygame.Rect(365, 182, 220, 600) #create rectangle

#load spring
spring = pygame.image.load("spring.png") #load spring image
springWidth, springHeight = spring.get_size() #get size of spring

#load buttons' images
pop_Img = pygame.image.load("button_pop.png").convert_alpha() #load pop image
push_Img = pygame.image.load("button_push.png").convert_alpha() #load push image
top_Img = pygame.image.load("button_top.png").convert_alpha() #load top image
len_Img = pygame.image.load("button_length.png").convert_alpha() #load len image
is_empty_Img = pygame.image.load("button_is-empty.png").convert_alpha() #load is empty image
        
#create button instances
pop_img = button.Button(50, 50, pop_Img)
push_img = button.Button(50, 150, push_Img)
top_img = button.Button(50, 250, top_Img)
len_img = button.Button(50, 350, len_Img)
is_empty_img = button.Button(50, 450, is_empty_Img)

#create stack
dispenserStack = stack.ArrayStack() 

k = 0
candy_names = []

#Fonts
font = pygame.font.Font(None, 16)
message_font = pygame.font.Font(None, 36)

running = True #set running to true
while running: #while running is true
    for event in pygame.event.get(): #for all events
        if event.type == pygame.QUIT: #if the event is quit
            running = False #set running to false
        elif pop_img.draw(screen): #if pop button is clicked
            try:
                popped_candy_number = dispenserStack.pop()
                print("Popped candy no: ", popped_candy_number)
                popped_candy_name = candy_names[popped_candy_number - 1]  # Get the name of the popped candy
                print("Popped candy name:", popped_candy_name)
                
                candy_names.pop()
                k -= 1
                pygame.draw.line(screen, (255, 255, 255), (371, 176), (580, 176), 10) #590
                pygame.draw.line(screen, (0, 0, 0), (362, 170), (580, 50), 10) 


                # Draw a message box with the popped candy's name
                message_text = message_font.render("Popped Candy: " + popped_candy_name, True, (0, 0, 0))
                message_rect = message_text.get_rect(center=(600, 150))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(500)  # Display the message box for 2 seconds (2000 milliseconds)
                    
            except stack.Empty:
                print("Dispenser is empty")
                # Display message
                message_text = message_font.render("Dispensor empty!!!", True, (255, 0, 0))
                message_rect = message_text.get_rect(center=(600, 150))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(500)  # Display the message for 1/2 a second         
             
        elif push_img.draw(screen):
            if len(dispenserStack) < 15:

                k+=1
                candyName = f'Candy {k}'
                candy_names.append(candyName)
                dispenserStack.push(k)
                pygame.draw.line(screen, (255, 255, 255), (371, 176), (580, 176), 10) #590
                pygame.draw.line(screen, (0, 0, 0), (362, 170), (580, 50), 10) 
                pygame.display.flip()
                pygame.time.delay(500)
            else:
                print("Dispenser is full")
                # Display message
                message_text = message_font.render("Dispenser is full!!", True, (255, 0, 0))
                message_rect = message_text.get_rect(center=(600, 150))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(500)
                
        elif top_img.draw(screen):
            try:
                print(dispenserStack.top())
                top_candy_number = dispenserStack.top()
                top_candy_name = candy_names[top_candy_number - 1]  # Get the name of the popped candy
                print("Top candy name:", top_candy_name)

                # Display a message box with the top candy's name
                message_text = message_font.render("Top Candy: " + top_candy_name, True, (0, 0, 0))
                message_rect = message_text.get_rect(center=(600, 150))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(1000) 
    
            except stack.Empty:
                print("Dispenser is empty")
                # Draw a message box
                message_text = message_font.render("Dispensor empty!!!", True, (255, 0, 0))
                message_rect = message_text.get_rect(center=(600, 150))
                screen.blit(message_text, message_rect.topleft)

                pygame.display.flip()
                pygame.time.delay(1000) 
            
        elif len_img.draw(screen):
            print(len(dispenserStack))
            candyLength = str(len(dispenserStack))

            # Draw a message box showing no of candies
            message_text = message_font.render("Number of Candies: " + candyLength, True, (0, 0, 0))
            message_rect = message_text.get_rect(center=(600, 150))
            screen.blit(message_text, message_rect.topleft)

            pygame.display.flip()
            pygame.time.delay(1000) 

        
        elif is_empty_img.draw(screen):
            empty = str(dispenserStack.is_empty())
            print("Is empty?", empty)
            
            # Draw a message box showing whether empty is true or false
            message_text = message_font.render("Is Dispensor Empty? "+ empty, True, (0, 0, 0))
            message_rect = message_text.get_rect(center=(600, 150))
            screen.blit(message_text, message_rect.topleft)

            pygame.display.flip()
            pygame.time.delay(1000)  
            
    num_candies = len(dispenserStack._data)
                    
    screen.fill((0, 0, 255))
    
    #Draw buttons
    pop_img.draw(screen) 
    push_img.draw(screen)  
    top_img.draw(screen) 
    len_img.draw(screen) 
    is_empty_img.draw(screen)
    
    #draw rectangle with borders
    pygame.draw.rect(screen, (255, 255, 255), rect_1) #draw rectangle
    y = 360 + num_candies*10
    pygame.draw.line(screen, (0, 0, 0), (365, y), (585, y), 10)
    pygame.draw.line(screen, (0, 0, 0), (365, 172), (365, 800), 10)
    pygame.draw.line(screen, (0, 0, 0), (585, 172), (585, 800), 10)
    pygame.draw.line(screen, (0, 0, 0), (365, 176), (585, 176), 10)

    #Spring height and width manipulation
    spring_max_height = 300  # Adjust this value according to your maximum spring height
    new_springHeight = spring_max_height - num_candies * 10
    scale_factor = 0.75 #scale factor
    new_springWidth = int(springWidth * scale_factor) #new spring width
    resized_spring = pygame.transform.scale(spring, (new_springWidth, new_springHeight)) #resize spring
    screen.blit(resized_spring, (280, 332 + num_candies*10)) #blit resized spring
    
    #Candy coordinate logic
    num_columns = 3
    candy_spacing_x = 61  # Adjust this value according to your spacing preference
    candy_spacing_y = 61  # Adjust this value according to your spacing preference
    for i in range(num_candies):
        row = i // num_columns
        column = i % num_columns
        x = CANDY_CENTRE[0] + candy_spacing_x * column
        y = CANDY_CENTRE[1] - candy_spacing_y * row + num_candies*10
        centre_of_candy = (x, y) 
        candy_name = candy_names[i]
        # print("candy name: ", candy_name)
        pygame.draw.circle(screen, CANDY_COLOR, centre_of_candy, CANDY_RADIUS)
        text = font.render(candy_name, True, (0, 0, 0))
        text_rect = text.get_rect(center=centre_of_candy)  # Position the text below the candy
        screen.blit(text, text_rect)

        
    pygame.display.update() #update screen
    pygame.time.delay(25)
pygame.quit() #quit pygame 

    