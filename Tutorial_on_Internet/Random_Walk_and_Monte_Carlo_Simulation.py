import random

def random_walk(n):
    # Return coordinates after 'n' block random walk
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'W', 'E'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return (x, y)

def random_walk_2(n):
    # Return coordinates after 'n' block random walk
    x ,y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

def main():
    number_of_walks = 100000
    for walk_length in range(1, 31):
        no_transport = 0
        for i in range(number_of_walks):
            (x, y) = random_walk_2(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 4:
                no_transport += 1
        no_transport_percent = float(no_transport / number_of_walks)
        print("walk size = ", str(walk_length), " /% of no_transport = ", 100 * no_transport_percent)


if __name__ == '__main__':
    main()
