# Image to RGB Pointilism Generator
# Georgia Brown

# import statements
import pygame
import random

# loading the source image from input
imgName = input("Input the name of an image file: ")
srcImg = pygame.image.load(imgName)
# factor refers to the amount the pixels spread in each direction in the 
# pointilism recreation
factor = 5
(w, h) = srcImg.get_size()

# create window in pygame
canvas = pygame.display.set_mode((w * factor, h * factor))

# create nested loops to go through each pixel of source image
for y in range(h):
    for x in range(w):
        # get rgb values of given pixel
        (r, g, b, _) = srcImg.get_at((x, y))
        # assign a certain number of each colour of points depending on said rgb value
        numRed = int(r / 25)
        numGreen = int(g / 25)
        numBlue = int(b / 25)

        # draw corresponding number of each colour
        # with a random spread of +- 5 pixels in each direction
        for i in range(numRed):
            randomVert = random.randint(-5, 5)
            randomHoriz = random.randint(-5, 5)
            pygame.draw.circle(canvas, (255, 0, 0), (x * factor + randomHoriz, y*factor + randomVert), 1)
        for i in range(numGreen):
            randomVert = random.randint(-5, 5)
            randomHoriz = random.randint(-5, 5)
            pygame.draw.circle(canvas, (0, 255, 0), (x * factor + randomHoriz, y * factor + randomVert), 1)
        for i in range(numBlue):
            randomVert = random.randint(-5, 5)
            randomHoriz = random.randint(-5, 5)
            pygame.draw.circle(canvas, (0, 0, 255), (x * factor + randomHoriz, y * factor + randomVert), 1)

# display pointillism recreation
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()