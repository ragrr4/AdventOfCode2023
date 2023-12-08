def process_game(game_str):
    min_blue = 0
    min_red = 0
    min_green = 0
    games = game_str.split(";")
    for game in games:
        cubes = game.split(",")
        for cube in cubes:
            colors = cube.split(" ")
            if colors[2] == "red" and int(colors[1]) > min_red:
                min_red = int(colors[1])
            elif colors[2] == "green" and int(colors[1]) > min_green:
                min_green = int(colors[1])
            elif colors[2] == "blue" and int(colors[1]) > min_blue:
                min_blue = int(colors[1])
    return min_blue * min_green * min_red

raw_input = []
result = 0
with(open("input.txt") as file):
    raw_input = file.read().splitlines()
for idx, line in enumerate(raw_input):
    result += process_game(line.split(":")[1])
print(result)
#63981