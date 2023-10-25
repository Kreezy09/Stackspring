import pygame, button, stack

pygame.init() #initialize pygame
#const
WIDTH, HEIGHT = 800, 600 #set width and height
WHITE = (255, 255, 255)
CANDY_COLOR = (255, 0, 0) 
CANDY_CENTRE = (330, 395)  # Center coordinates
CANDY_RADIUS = 30  # Radius of the circle

#create screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
#title
pygame.display.set_caption("Candy Dispenser")

rect_1 = pygame.Rect(300, 200, 220, 600) #create rectangle

spring = pygame.image.load("spring.png") #load spring image
springWidth, springHeight = spring.get_size() #get size of spring

animation_speed = 2 #animation speed
max_strecth = 1 #max stretch
min_stretch = 0.5 #min stretch

scale_factor = 0.5 #scale factor

new_springWidth = int(springWidth * scale_factor) #new spring width
# new_springHeight = int(springHeight * scale_factor) #new spring height

# resized_spring = pygame.transform.scale(spring, (new_springWidth, new_springHeight)) #resize spring

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

#drawnCandies = []

dispenserStack = stack.ArrayStack() #create stack
k = 0


running = True #set running to true
stretch_factor = min_stretch #set stretch factor to min stretch
while running: #while running is true
    for event in pygame.event.get(): #for all events
        if event.type == pygame.QUIT: #if the event is quit
            running = False #set running to false
        elif pop_img.draw(screen): #if pop button is clicked
            try:
                k-=1
                dispenserStack.pop()
                
                # if len(drawnCandies) > 0:
                #     drawnCandies.pop()
            except stack.Empty:
                print("Dispenser is empty")
          
             
        elif push_img.draw(screen):
            if len(dispenserStack) < 7:
                k+=1
                dispenserStack.push(k)
                print(dispenserStack.is_empty())
                # print(len(dispenserStack))
                dispenserStack.print_stack()
            else:
                print("Dispenser is full")
                
        elif top_img.draw(screen):
            try:
                print(dispenserStack.top())
            except stack.Empty:
                print("Dispenser is empty")
            
        elif len_img.draw(screen):
            print(len(dispenserStack))
        
        elif is_empty_img.draw(screen):
            print(dispenserStack.is_empty())
                    
    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (255, 255, 255), rect_1) #draw rectangle
    
    stretched_height = int(springHeight * stretch_factor) #stretched height
    stetched_width = springWidth
    new_springIcon = pygame.transform.scale(spring, (stetched_width, stretched_height)) #new spring icon
    
    # screen.blit(new_springIcon, (147, rect_1.y + rect_1.height - stretched_height)) #blit spring icon
    num_candies = len(dispenserStack._data)
    num_rows = 3
    num_columns = 3
    candy_spacing_x = 61  # Adjust this value according to your spacing preference
    candy_spacing_y = 61  # Adjust this value according to your spacing preference
    
    spring_min_height = 50  # Adjust this value according to your minimum spring height
    spring_max_height = 150  # Adjust this value according to your maximum spring height

    new_springHeight = max(spring_min_height, spring_max_height - num_candies * 10)
    # print(new_springHeight)
    height_difference = new_springHeight - spring_max_height

    resized_spring = pygame.transform.scale(spring, (new_springWidth, new_springHeight)) #resize spring

    # screen.blit(resized_spring, (280, 470 + height_difference)) #blit resized spring
    screen.blit(resized_spring, (280, 470 )) #blit resized spring

    pop_img.draw(screen) #draw pop button
    push_img.draw(screen) #draw push button  
    top_img.draw(screen) #draw top button
    len_img.draw(screen) #draw len button
    is_empty_img.draw(screen) #draw is empty button
    

    # for i in range(len(dispenserStack._data)):
    #     centreOfCandy = (CANDY_CENTRE[0] + 61 * i, CANDY_CENTRE[1])
    #     pygame.draw.circle(screen, CANDY_COLOR, centreOfCandy, CANDY_RADIUS)
    #     drawnCandies.append(centreOfCandy)


    for i in range(num_candies):
        row = i // num_columns
        column = i % num_columns
        # print('rox', row, 'col', column)
        x = CANDY_CENTRE[0] + candy_spacing_x * column
        y = CANDY_CENTRE[1] + candy_spacing_y * row
        centre_of_candy = (x, y)
        pygame.draw.circle(screen, CANDY_COLOR, centre_of_candy, CANDY_RADIUS)
        #drawnCandies.append(centre_of_candy)

    
    stretch_factor += 0.01 * animation_speed #increase stretch factor  
    if stretch_factor > max_strecth or stretch_factor < min_stretch:
        animation_speed *= -1 #reverse animation speed

        
    pygame.display.update() #update screen
    pygame.time.delay(25)
pygame.quit() #quit pygame 

    # for i in range(len(dispenserStack._data)):
    #     interim_x = 330
    #     interim_y = 395
    #     if  interim_x + 70 * i < 550:
    #         centreOfCandy = (330 + 70 * i, interim_y)
    #         pygame.draw.circle(screen, CANDY_COLOR, centreOfCandy, CANDY_RADIUS)
    #         drawnCandies.append(centreOfCandy)
    #     else:
    #         centreOfCandy = (interim_x, interim_y + 70 * i)
    #         pygame.draw.circle(screen, CANDY_COLOR, centreOfCandy, CANDY_RADIUS)
    #         drawnCandies.append(centreOfCandy)
    