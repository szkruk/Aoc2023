import re
from typing import Tuple

mapping:dict = {
    "one": "o1ne",
    "two": "tw2o",
    "three":"thre3e",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "ei8ht",
    "nine": "ni9ne"
}


def get_int_from_frist_and_last_digit(word:str) ->int:
    matches = re.findall(r'\d+', word)
    regexed_numbers = "".join(matches)
    first_match = regexed_numbers[0]
    last_match = regexed_numbers[-1]
    number = int(first_match+last_match)
    return number

def return_first_match(word:str)-> Tuple[str,str] or None:
    smallest_index:int or None = None
    first_match:str or None = None
    for letters in mapping.keys():
        try:
            index = word.index(letters)
            if(smallest_index==None):
                smallest_index = index
                first_match = letters
                continue
            if index < smallest_index:
                smallest_index = index
                first_match = letters
        except:
            pass
    return (first_match, mapping.get(first_match)) if first_match else None


def replace_words_by_digit(word:str) -> str:
    while(True):
        match = return_first_match(word)
        if not match:
            break
        word = word.replace(match[0],match[1])
    return word

def get_int_from_frist_and_last_digit_with_words_replacement(word:str)->int:
    word_with_replacement = replace_words_by_digit(word)
    number = get_int_from_frist_and_last_digit(word_with_replacement)
    return number
if __name__ == "__main__":
    with open('Day 1/input_puzzle.txt', 'r') as file:
        puzzle_input = file.read().splitlines()
    # results_1 = [get_int_from_frist_and_last_digit(puzzle) for puzzle in puzzle_input]
    # print(sum(results_1))

    results_2 = [get_int_from_frist_and_last_digit_with_words_replacement(puzzle) for puzzle in puzzle_input]
    print(sum(results_2))
