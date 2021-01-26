import pygame
import random


class Fruit:
  color = (255,0,0)
  size = (10,10)

  def __init__(self):
    self.texture = pygame.Surface(self.size)
    self.texture.fill(self.color)
    x = random.randint(0,49) * 10
    y = random.randint(0,49) * 10
    self.position = (x,y)

  @staticmethod
  def create_fruit():
    x = random.randint(0,49) * 10
    y = random.randint(0,49) * 10

    if(x,y) in snake.body:
        Fruit.create_fruit()
    else:
      return (x,y)

class Snake:
  color = (255,255,255)
  size = {10,10}
  velocity = 10
  score = 0;

  def __init__(self):
    self.texture = pygame.Surface(self.size)
    self.texture.fill(self.color)
    self.direction = "right"
    self.body = [(100,100),(90,100),(80,100)]

  def walk(self):

    head = self.body[0]
    x = head[0]
    y = head[1]


    if self.direction == "right":
      self.body.insert(0,(x + self.velocity,y))
    elif self.direction == "left":
      self.body.insert(0,(x-self.velocity,y))
    elif self.direction == "up":
      self.body.insert(0,(x,y-self.velocity))
    elif self.direction == "down":
      self.body.insert(0,x,y+self.velocity)

    self.body.pop(-1)

  def collision_fruit(self,fruit):
      return self.body[0] == fruit.position

  def auto_collision(self):
    head = self.body[0]
    return if head in self.body[1:]
  
  def collision_wall(self):
      head = self.body[0]

      x = head[0]
      y = head[1]

      return if x<0 or y<0 or x>490 or x>490



  def eat(self):
      self.body.append(0,0)
      self.score += 1
      pygame.display.set_caption("Snake | Score: {}".format(self.score))

if __name__ = "__main__":

    pygame.init()

    resolution = (500,500)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    black = (0,1,2)
    screen.fill(black)
    pygame.display.update()

    fruits = Fruit()
    snake = Snake()

    while True:

      clock.tick(30)

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          exit()
        elif event.type == pygame.KEYDOWN:
          if event.type == pygame.K_UP:
            snake.direction == "up"
          if event.type == pygame.K_DOWN:
            snake.direction == "down"
          if event.type == pygame.K_RIGHT:
            snake.direction == "right"
          if event.type == pygame.K_LEFT:
            snake.direction == "left"

        if snake.colision_fruit(fruits):
          snake.eat()
          fruits = Fruit()
        
        if snake.colision_wall():
          snake = Snake()
        


      screen.blit(fruits.texture, fruits.position)
      
      for position in snake.body:
        screen.blit(snake.texture,position)
      pygame.display.update()