import argparse

from .status import ExitStatus
from .cli import process_args
from .airdis import (
    calculate_haversine_distance,
    read_places_from_csv,
    create_places_list,
    sort_places_by_distance,
    calculate_average_distance,
    find_the_closest_pair
)

from typing import Union, List


def print_places_pairs(places: List[Union[str, float]]) -> ExitStatus:
    try:
        col_width = max(len(str(word)) for row in places for word in row) + 2  # padding
        for row in places:
            distance = "".join(word.ljust(col_width) if isinstance(word, str) else str(word).ljust(20) + " km" for word in row)
            print("{}".format(distance))
        return ExitStatus.SUCCESS
    except:
        print("ERROR: Something wrong happened while printing the pairs!")
        return ExitStatus.ERROR


def print_average_distance_and_closest_pairs(places: List[Union[str, float]]) -> ExitStatus:
    try:
        average_distance = calculate_average_distance(places)
        closest_pair = find_the_closest_pair(places, average_distance)
        print("Average distance: {:.2f} km. Closest pair: {} - {} {:.2f} km".format(average_distance, closest_pair[0], closest_pair[1], closest_pair[2]))
        return ExitStatus.SUCCESS
    except:
        print("ERROR: Something wrong happened while printing the average distance and closest pairs!")
        return ExitStatus.ERROR

    
def main() -> ExitStatus:
    n, places_csv_path = process_args(parser=argparse.ArgumentParser())
    csv_header, csv_data = read_places_from_csv(places_csv_path)
    data = sort_places_by_distance(
        create_places_list(csv_data, n),
        calculate_haversine_distance
    )

    print_data = print_places_pairs([csv_header] + [["", "", ""]] + data)

    if ExitStatus.ERROR == print_data:
        return ExitStatus.ERROR

    print("") # --- Separator blank line
    print_data = print_average_distance_and_closest_pairs(data)

    if ExitStatus.ERROR == print_data:
        return ExitStatus.ERROR
    
    return ExitStatus.SUCCESS
