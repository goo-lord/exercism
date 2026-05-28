"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME: int = 40
PREPARATION_TIME: int = 2


def bake_time_remaining(elapsed_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    time_remaining: int = EXPECTED_BAKE_TIME - elapsed_time
    return time_remaining


def preparation_time_in_minutes(number_of_layers):
    """Calculates the time it takes to prepare the lasagna based on
         the number of layers being added.

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.

    Returns:
        int: Returns the time to prepare the lasagna.

    Function that takes the number of layers and uses `EXPECTED_BAKE_TIME`
    to calculate how long prepping should take. 
    """

    time_to_prepare: int = number_of_layers * PREPARATION_TIME
    return time_to_prepare


def elapsed_time_in_minutes(number_of_layers, elapsed_time):
    """Calculate the total time prepping and baking so far.

    Parameters:34
        number_of_layers (int): The number of layers added to the lasagna.

        elapsed_time (int): The time the lasagna has baked so far. 

    Returns:
        int: Returns the total time in the kitchen prepping and baking so far. 

    Function that takes the prepration time based on the number of layers 
    added to the lasagna and adds that to the time the lasagna
    has been in the oven using the  parameters number_of_layers and elapsed_time. 
    """

    total_elapsed_time: int = elapsed_time + preparation_time_in_minutes(number_of_layers)
    return total_elapsed_time