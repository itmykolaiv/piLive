import sys, pygame, copy
pygame.init()

size = width, height = 240, 240
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
current = [
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
]

new = copy.deepcopy(current)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(white)
    
    for y in range(0,len(current)):
        for x in range(0,len(current[y])):
            color = "white"
            if current[y][x]:
                color = "chocolate"
            pygame.draw.rect(screen, pygame.Color(color), (x*10,y*10,10,10), 0)
            pygame.draw.rect(screen, pygame.Color("black"), (x*10,y*10,10,10), 1)
            top = y - 1
            bottom = y + 1
            left = x - 1
            right = x + 1
            if y == 0:
                top = len(current) - 1
            if y == len(current) - 1:
                bottom = 0
            if x == 0:
                left = len(current[y]) - 1
            if x == len(current[y]) - 1:
                right = 0

            sum1 = current[top][left] + current[top][x] + current[top][right] + \
            current[y][left] + current[y][right] + current[bottom][left] + \
            current[bottom][x] + current[bottom][right]
            
            if current[y][x] == 0 and sum1 == 3:
                new[y][x] = 1
            elif current[y][x] == 1 and (sum1 == 2 or sum1 == 3):
                new[y][x] = 1
            else:
                new[y][x] = 0
           
    pygame.time.delay(200)   
    current = copy.deepcopy(new)
    pygame.display.flip()