"""Console script for airdis."""
import argparse
import sys
import os

from typing import Tuple

def process_args(parser: argparse.ArgumentParser) -> Tuple[int, str]:
    """
    This function is used to process the command-line arguments passed to the script.
    It returns a tuple of two values: number of random places to pick and the path to the places.csv.

    Returns:
    - Tuple[int, str] -- Tuple of two values: number of random places to pick and the path to the places.csv.
    """
    parser.add_argument(
        '-n',
        '--number',
        help="Number of random places to pick form the places list",
        type= int,
        default= 0
    )
    
    parser.add_argument(
        '-p',
        '--path',
        help="Path to the places.csv",
        type= str,
        default= os.path.join(os.path.dirname(__file__), '../data/places.csv')
    )
    
    args = parser.parse_args()
    return args.number, args.path
