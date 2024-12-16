import numpy as np
import matplotlib.pyplot as plt
import random 

# Instructions
print("Welcome to Mario Party - Scuffed Board Game Edition!")
print("The goal of the game is to reach the finish line.")

#Characters - Mario, Luigi, Peach, Daisy
characters_list = ["Mario", "Luigi", "Peach", "Bowser"]
colours_list = ["red", "green", "pink", "yellow"]
print("Choose your character:")
print(characters_list)

# journey path
x = [1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 6]
y = [1, 2, 2, 2, 2, 3, 4, 4, 4, 5, 6]
plt.plot(x,y)
plt.xlim(0, 7)
plt.ylim(0, 7)
plt.title("Mario Party - Scuffed Game Board")



# start at home base
plt.scatter(x[0], y[0], color="cyan", s=100, marker="^")

# finish line
plt.scatter(x[-1], y[-1], color="magenta", s=100, marker="^")

# plot characters
plt.scatter(x[0] + random.uniform(-0.25, 0.25), y[0]+ random.uniform(-0.25, 0.25), color=colours_list[0], s=50, marker="o")
plt.scatter(x[0] + random.uniform(-0.25, 0.25), y[0] + random.uniform(-0.25, 0.25), color=colours_list[1], s=50, marker="o")
plt.scatter(x[0] + random.uniform(-0.25, 0.25), y[0] + random.uniform(-0.25, 0.25), color=colours_list[2], s=50, marker="o")
plt.scatter(x[0] + random.uniform(-0.25, 0.25), y[0] + random.uniform(-0.25, 0.25), color=colours_list[3], s=50, marker="o")
plt.savefig("board.png")

# players first rolls
dice_size = 6
char_1 = random.randint(1, dice_size)
plt.scatter(x[char_1] + random.uniform(-0.25, 0.25), y[char_1] + random.uniform(-0.25, 0.25), color=colours_list[0], s=50, marker="o")
plt.title(characters_list[0] + ' first move, rolled ' + str(char_1))
plt.savefig("p1_first.png")

char_2 = random.randint(1, dice_size)
plt.scatter(x[char_2] + random.uniform(-0.25, 0.25), y[char_2] + random.uniform(-0.25, 0.25), color=colours_list[1], s=50, marker="o")
plt.title(characters_list[1] + ' first move, rolled ' + str(char_2))
plt.savefig("p2_first.png")

char_3 = random.randint(1, dice_size)
plt.scatter(x[char_3] + random.uniform(-0.25, 0.25), y[char_3] + random.uniform(-0.25, 0.25), color=colours_list[2], s=50, marker="o")
plt.title(characters_list[2] + ' first move, rolled ' + str(char_3))
plt.savefig("p3_first.png")

char_4 = random.randint(1, dice_size)
plt.scatter(x[char_4] + random.uniform(-0.25, 0.25), y[char_4] + random.uniform(-0.25, 0.25), color=colours_list[3], s=50, marker="o")
plt.title(characters_list[2] + ' first move, rolled ' + str(char_4))
plt.savefig("p4_first.png")

# determine winners
plt.show()
