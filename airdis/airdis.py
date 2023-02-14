import argparse
import random
import math
import sys
import os

from typing import Tuple, Union, List, Callable



def calculate_haversine_distance(start: List[Union[str, float]], end: List[Union[str, float]]) -> float:
    """
    This function calculates the Haversine distance between two points on Earth,
    represented by their latitude and longitude coordinates.
    The Haversine formula is used to calculate the great-circle distance between two points,
    which is the shortest distance on the surface of a sphere.
    The formula assumes a perfect sphere, so the Earth's radius is used as a constant.

    Args:
    - start : List[Union[str, float]], Latitude and Longitude of the start point in degrees.
    - end :  List[Union[str, float]]: Latitude and Longitude of the end point in degrees.

    Returns:
    - float: The Haversine distance in kilometers between the start and end points.
    """
    EARTH_RADIUS = 6371
    latitude_difference = math.radians(end[1] - start[1])
    longitude_difference = math.radians(end[2] - start[2])
    start_latitude = math.radians(start[1])
    end_latitude = math.radians(end[1])
    a = (
        math.sin(latitude_difference / 2) ** 2
        + math.cos(start_latitude) * math.cos(end_latitude) * math.sin(longitude_difference / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    return EARTH_RADIUS * c

def create_places_list(places: List[Union[str, float]], n: int) -> List[Union[str, float]]:
    """
    Creates a list of n random places from the given list of places.

    Args:
    - places: A list of places where each place is represented as a list of
    name (string), latitude (float), and longitude (float) of the place.
    - n: An integer representing the number of places to pick randomly.

    Returns:
    - A list of n randomly picked places from the given list. If n is less than
    or equal to 0 or greater than the number of places, it returns the entire list of places.

    """
    if n <= 0 or n > len(places):
        return places
    return random.sample(places, n)

def sort_places_by_distance(places: List[Union[str, float]], fn: Callable[[float, float, float, float], float]) -> List[Union[str, float]]:
    """
    Sorts the given list of places based on the Haversine distance between each pair of places.

    Args:
    - places: A list of places where each place is represented as a list of
    name (string), latitude (float), and longitude (float) of the place.

    Returns:
    - A list of tuples, each tuple contains the name of two places and the Haversine
    distance between them. The list is sorted in ascending order based on the Haversine distance.

    """
    result = []
    for i in range(len(places)):
        for j in range(i+1, len(places)):
            distance = fn(places[i], places[j])
            result.append([places[i][0], places[j][0], distance])
    return sorted(result, key=lambda x: x[2])

def calculate_average_distance(places: List[Union[str, float]]) -> float:
    """
    Calculates the average distance between all the places in the list.

    Parameters:
    - places ([[str, float, float]]): List of places with each place being represented as a list [name (str), latitude (float), longitude (float)].

    Returns:
    - float: Average distance between all the places in the list.
    """
    total_distance = 0
    for pair in places:
        total_distance += pair[2]
    return total_distance / len(places)

def find_the_closest_pair(places: List[Union[str, float]], average_distance: float) -> List[Union[str, float]]:
    """
    Finds the pair of places from the list which have distance closest to the average distance.

    Parameters:
    - places (List[List[str, float, float]]): List of places with each place being represented as a list [name (str), latitude (float), longitude (float)].
    - average_distance (float): Average distance between all the places in the list.

    Returns:
    - List[str, float, float]: Pair of places with distance closest to the average distance represented as [name1 (str), name2 (str), distance (float)].
    """
    closest_pair = places[0]
    min_distance = abs(places[0][2] - average_distance)
    for pair in places:
        distance = abs(pair[2] - average_distance)
        if distance < min_distance:
            min_distance = distance
            closest_pair = pair
    return closest_pair
