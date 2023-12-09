import re
from typing import Tuple

limit:dict = {
    "red":12,
    "green":13,
    "blue":14
}

def get_number_per_color(sets_str,pattern)->int:
   matches =  re.findall(pattern,sets_str)
   if not matches:
       return 0
   matches_int:list[int] = [int(match) for match in matches]
   return max(matches_int)
   
def get_number_of_cubes(sets_str:str)->dict[str,int]:
    red_regex = r'(\d+) red'
    blue_regex = r'(\d+) blue'
    green_regex = r'(\d+) green'
    
    cubes_per_color:dict = {
    "red": get_number_per_color(sets_str, red_regex),
    "green": get_number_per_color(sets_str, green_regex),
    "blue": get_number_per_color(sets_str, blue_regex)
    }
    return cubes_per_color

    
def get_game_id_and_count_cubes(puzzle:str)-> Tuple[int,dict[str,int]]:
    game_id_str, sets_str = puzzle.split(":")
    id_str = re.findall(r'\d+',game_id_str)[0]
    id:int = int(id_str)
    cubes_per_color:dict = get_number_of_cubes(sets_str)
    return id, cubes_per_color

def check_if_number_of_cubes_is_over_the_limit(puzzle:str)->int:
    game_id, cubes_per_color = get_game_id_and_count_cubes(puzzle)
    for color, amount in cubes_per_color.items():
        limit_per_color = limit.get(color)
        if amount > limit_per_color:
            return 0
    return game_id

def get_power_of_fewest_number_of_cubes_per_color(puzzle:str)->int:
    _, cubes_per_color = get_game_id_and_count_cubes(puzzle)
    power = 1
    for amount in cubes_per_color.values(): 
        power*=amount
    return power

if __name__ == "__main__":
    with open('Day 2/input_puzzle.txt', 'r') as file:
        puzzle_input = file.read().splitlines()
        
    # results = [check_if_number_of_cubes_is_over_the_limit(puzzle) for puzzle in puzzle_input]
    # print(sum(results))
    
    results = [get_power_of_fewest_number_of_cubes_per_color(puzzle) for puzzle in puzzle_input]
    print(sum(results))