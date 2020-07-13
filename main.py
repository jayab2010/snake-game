import random
import curses

s = curses.initscr()
# Set up the curser to zero so it dosent show up on screen
curses.curs_set(0)
sh, sw = s.getmaxyx()
# create new window
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
# refresh window every 100 milisec
w.timeout(100)
#snakes initial position
snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
#create food at the center of screen
food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
# set initial direction of snake going to the right direction.
key = curses.KEY_RIGHT
#infite loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
# to check the person lost a game
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
# staring of new head
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)
# to checj whether snake ran into food or not
    if snake[0] == food:
        food = None
        while food is None:
#new food location          
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
#add head of snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)