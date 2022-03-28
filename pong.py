import pygame
import random
import sys

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Pong")
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BACKGROUND_COLOUR = (0, 0, 0)

paddle_size = [10, 80] 

bot_pos = [40, int(HEIGHT / 2)]

paddle_pos = [(WIDTH - 50), int(HEIGHT / 2)]

ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
ball_size = 10

myFont = pygame.font.SysFont("Consolas", 20)

score = 0
score2 = 0
total = 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

winner = ""

yList = [-2, -1, 1, 2]
xList = [- 1, 1]
velocity = [random.choice(xList), random.choice(yList)]	


font = pygame.font.Font(None, 30)



total = 0


def intro():
	point = 0
	start = False
	while not start:
		text = "PONG"
		label = pygame.font.Font(None, 50).render(text, True, WHITE)
		screen.blit(label, (int(WIDTH / 2) - 50, 0))
		text2 = "Press the number corresponding to "
		text3 = "the number of points to play to"
		label3 = pygame.font.SysFont("Consolas", 20).render(text3, True, WHITE)
		label2 = pygame.font.SysFont("Consolas", 20).render(text2, True, WHITE)
		screen.blit(label2, (200, int(HEIGHT / 3)))
		screen.blit(label3, (220, int(HEIGHT / 3) + 20))
		one = "1: 1 Points"
		two = "2: 5 Points"
		three = "3: 10 Points" 
		four = "4: 15 Points"
		five = "5: 20 Points"
		labelone = pygame.font.SysFont("Consolas", 15).render(one, True, WHITE)
		screen.blit(labelone, (205, int(HEIGHT / 2)))
		labeltwo = pygame.font.SysFont("Consolas", 15).render(two, True, WHITE)
		screen.blit(labeltwo, (205, int(HEIGHT / 2 + 20)))
		labelthree = pygame.font.SysFont("Consolas", 15).render(three, True, WHITE)
		screen.blit(labelthree, (205, int(HEIGHT / 2 + 40)))
		labelfour = pygame.font.SysFont("Consolas", 15).render(four, True, WHITE)
		screen.blit(labelfour, (205, int(HEIGHT / 2 + 60)))
		labelfive = pygame.font.SysFont("Consolas", 15).render(five, True, WHITE)
		screen.blit(labelfive, (205, int(HEIGHT / 2 + 80)))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					point = 1
					return point
				elif event.key == pygame.K_2:
					point = 5
					return point
				elif event.key == pygame.K_3:
					point = 10
					return point
				elif event.key == pygame.K_4:
					point = 15
					return point
				elif event.key == pygame.K_5:
					point = 20
					return point
				else:
					textinvalid = "Invalid number"
					invalid = pygame.font.SysFont("Consolas", 15).render(textinvalid, True, WHITE)
					screen.blit(invalid, (205, int(HEIGHT / 2) + 100))


		pygame.display.flip()

def countDown():
	counter = 3

	while counter > 0:
		pygame.display.flip()
		if counter > 0:
			screen.fill(BACKGROUND_COLOUR)
			text = str(counter)
			label = myFont.render(text, True, WHITE)
			screen.blit(label, (int(WIDTH / 2), int(HEIGHT / 2)))
			counter -= 1
				
				
		pygame.display.flip()


def show_Winner(playerA, playerB):
	if playerA > playerB:
		winner = "Player A"
	else:
		winner = "Player B"

	print(winner + " wins!")
	while True:

		screen.fill((BACKGROUND_COLOUR))
		text = winner + " is the winner!"
		label = font.render(text, True, WHITE)
		screen.blit(label, (int(WIDTH / 2) - 100, int(HEIGHT / 2)))

		text2 = "Press any key to exit"
		label2 = pygame.font.Font(None, 15).render(text2, True, WHITE)
		screen.blit(label2, (int(WIDTH / 2) - 50, HEIGHT - 100))
		pygame.display.update()


		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
				pygame.time.wait(1000)
				sys.exit()

		
total = int(intro())

if total != 0:
	countDown()
	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				while True:
					event = pygame.event.wait()
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						break

			if event.type == pygame.KEYDOWN:
				x = paddle_pos[0]
				y = paddle_pos[1]

				x2 = bot_pos[0]
				y2 = bot_pos[1]

				if event.key == pygame.K_RIGHT and y >= 0:
					y -= paddle_size[1]

				if event.key == pygame.K_LEFT and y <= (HEIGHT - 100):
					y += paddle_size[1] 

				paddle_pos = [x, y]

				if event.key == pygame.K_a and y2 >= 0:
					y2 -= paddle_size[1]

				if event.key == pygame.K_d and y2 <= (HEIGHT - 100):
					y2 += paddle_size[1]

				bot_pos = [x2, y2]

		x = ball_pos[0]
		y = ball_pos[1]
		x += velocity[0]
		y += velocity[1]

		ball_pos = [x, y]
		
		if ball_pos[0] + ball_size > WIDTH:
			score += 1
			if score != total:
				countDown()
				ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
				velocity = [-1, random.randint(1, 2)]
			else:
				game_over = True

		elif ball_pos[0] - ball_size < 0:
			score2 += 1
			if score2 != total:
				countDown()
				ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
				velocity = [1, random.randint(1, 2)]
			else:
				game_over = True



		if ball_pos[1] + ball_size > HEIGHT or ball_pos[1] < 0:
			velocity[1] = -velocity[1]

		
		if (ball_pos[0] >= paddle_pos[0] and ball_pos[0] < (paddle_pos[0] + paddle_size[0])) or (paddle_pos[0] >= ball_pos[0] and paddle_pos[0] < (ball_pos[0] + ball_size)):
			if(ball_pos[1] >= paddle_pos[1] and ball_pos[1] < (paddle_pos[1] + paddle_size[1])) or (paddle_pos[1] >= ball_pos[1] and paddle_pos[1] < (ball_pos[1] + ball_size)):
				velocity[0] = -velocity[0] - 1/2

		if (ball_pos[0] >= bot_pos[0] and ball_pos[0] < (bot_pos[0] + paddle_size[0])) or (bot_pos[0] >= ball_pos[0] and bot_pos[0] < (ball_pos[0] + ball_size)):
			if(ball_pos[1] >= bot_pos[1] and ball_pos[1] < (bot_pos[1] + paddle_size[1])) or (bot_pos[1] >= ball_pos[1] and bot_pos[1] < (ball_pos[1] + ball_size)):
				velocity[0] = -velocity[0]  + 1/2


		screen.fill(BACKGROUND_COLOUR)

		text = "Player A: " + str(score)	
		label = myFont.render(text, True, WHITE)

		text2 = "Player B: " + str(score2)
		label2 = myFont.render(text2, True, WHITE)

		screen.blit(label, (0, 0))
		screen.blit(label2, (WIDTH - 150, 0))

		pygame.draw.rect(screen, WHITE, (paddle_pos[0], paddle_pos[1], paddle_size[0], paddle_size[1]))
		pygame.draw.rect(screen, WHITE, (bot_pos[0], bot_pos[1], paddle_size[0], paddle_size[1]))
		pygame.draw.rect(screen, WHITE, (ball_pos[0], ball_pos[1], ball_size, ball_size))

		

		pygame.display.flip()
		clock.tick(250)


		
	
	show_Winner(score, score2)

