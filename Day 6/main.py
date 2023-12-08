import json
from typing import Tuple
import math

"""
What's the idea behind this solution?
It's simple mathematical prolbem. This can be resolved by finding two zeros of the quadratic equation.
Quadratic equation schema looks like:
    a*x^2 + b*x + c > 0
In our cases it takes form of:
    1*Tl^2 - T*Tl + x < 0
where:
    Tl: Loading Time,
    T: Total Time,
    x: distance
"""

def calculate_zeros_of_the_functions(total_time: int, distance: int) -> Tuple[int, int]:
    delta = (total_time**2) - (4 * distance)
    lower_threshold = (-total_time - math.sqrt(delta)) / 2
    upper_threshold = (-total_time + math.sqrt(delta)) / 2
    return lower_threshold, upper_threshold

def get_all_integers_between_two_floats(
    lower_threshold: float, upper_threshold: float
) -> list[int]:
    return list(range(math.ceil(lower_threshold), math.floor(upper_threshold) + 1))

def calculate_number_of_unique_solutions(time: int, distance: int) -> int:
    lower_threshold, upper_threshold = calculate_zeros_of_the_functions(time, distance)
    unique_solution = get_all_integers_between_two_floats(
        lower_threshold, upper_threshold
    )
    return len(unique_solution)

if __name__ == "__main__":
    with open('input_puzzle.json', 'r') as file:
        input_puzzle: dict[str, list] = json.load(file)
        
    for time, distance in zip(input_puzzle["time"], input_puzzle["distance"]):
        print(calculate_number_of_unique_solutions(time, distance))