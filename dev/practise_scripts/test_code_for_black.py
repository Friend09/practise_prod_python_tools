import os

list_of_numbers = [1, 2, 3]

large_dictionary = {
    1: 2,
    3: 4,
    5: 6,
    7: 8,
    9: 10,
    11: 12,
    13: 14,
    15: 16,
    17: 18,
    19: 20,
    21: 22,
    23: 24,
}


def open_up_this_here_file(
    filepath: os.PathLike,
    read_method: str = "w",
    verbose: bool = True,
    debug: bool = False,
):
    """Does a whole bunch of things this one function does right here."""
    with open(filepath, read_method) as f:
        print(f.read())
