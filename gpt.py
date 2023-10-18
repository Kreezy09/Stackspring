import pygame
from pygame.locals import *
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
DISPENSER_WIDTH, DISPENSER_HEIGHT = 200, 400
CANDY_RADIUS = 20
SPRING_HEIGHT = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Dispenser with Stack")

# Initialize stack for candies
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

# Initialize stack
candy_stack = ArrayStack()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_p:
                # Pop operation: remove candy from the stack
                try:
                    candy_stack.pop()
                except Empty:
                    print("Stack is empty!")
            elif event.key == K_o:
                # Push operation: add candy to the stack
                candy_stack.push((WIDTH // 2, HEIGHT - DISPENSER_HEIGHT - SPRING_HEIGHT - CANDY_RADIUS))

    # Draw everything
    screen.fill(WHITE)

    # Draw dispenser
    pygame.draw.rect(screen, RED, (WIDTH // 2 - DISPENSER_WIDTH // 2, HEIGHT - DISPENSER_HEIGHT, DISPENSER_WIDTH, DISPENSER_HEIGHT))

    # Draw spring
    pygame.draw.line(screen, BLACK, (WIDTH // 2, HEIGHT - DISPENSER_HEIGHT - SPRING_HEIGHT), (WIDTH // 2, HEIGHT - DISPENSER_HEIGHT))

    # Draw candies
    for pos in candy_stack._data:  # Accessing _data directly for demonstration purposes
        pygame.draw.circle(screen, RED, pos, CANDY_RADIUS)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
