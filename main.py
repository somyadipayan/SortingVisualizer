from operator import ge
from this import d
import pygame
import random

pygame.init()

class DrawInfo:
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0 , 0
    GREYS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
    BG_COLOR = WHITE
    SIDE_PADDING = 100
    TOP_PADDING = 200
    FONT = pygame.font.SysFont('Helvetica', 30)
    TITLE_FONT = pygame.font.SysFont('Helvetica', 40)

    def __init__(self, width, height, l):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Visualizer")
        self.set_list(l)

    def set_list(self, l):
        self.l = l
        self.min_val = min(l)
        self.max_val = max(l)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(l))
        self.block_height = round((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.start_x =  self.SIDE_PADDING // 2


def generate_list(n, min_val, max_val):
    l = []
    for _ in range(n):
        l.append(random.randint(min_val, max_val))
    return l

def draw(draw_info):
    draw_info.window.fill(draw_info.BG_COLOR)
    controls = draw_info.FONT.render("R: Reset | Space: Start Sorting | A: Ascending | D:Descending", 1, draw_info.GREYS[2])
    draw_info.window.blit(controls,(draw_info.width/2 - controls.get_width()/2, 5))
    sorting = draw_info.FONT.render("1. Insertion Sort | 2. Bubble Sort", 1, draw_info.GREYS[2])
    draw_info.window.blit(sorting,(draw_info.width/2 - sorting.get_width()/2, 40))
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info):
    l = draw_info.l
    for i, val in enumerate(l):
        x = draw_info.start_x + i*draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val)*draw_info.block_height
        color = draw_info.GREYS[i%3]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))



def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    l = generate_list(n, min_val, max_val)
    draw_info = DrawInfo(1280, 720, l)
    sorting = False
    ascending = True

    while run:
        clock.tick(60)

        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                l = generate_list(n, min_val, max_val)
                draw_info.set_list(l)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False

    
    pygame.quit()

if __name__ == "__main__":
    main()