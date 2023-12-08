red_limit = 12
green_limit = 13
blue_limit = 14

def process_game(game_str):
    games = game_str.split(";")
    for game in games:
        cubes = game.split(",")
        for cube in cubes:
            colors = cube.split(" ")
            if colors[2] == "red" and int(colors[1]) > red_limit:
                return False
            elif colors[2] == "green" and int(colors[1]) > green_limit:
                return False
            elif colors[2] == "blue" and int(colors[1]) > blue_limit:
                return False
    return True

raw_input = []
result = 0
with(open("input.txt") as file):
    raw_input = file.read().splitlines()
for idx, line in enumerate(raw_input):
    if process_game(line.split(":")[1]) :
        result += idx + 1
print(result)
#2449