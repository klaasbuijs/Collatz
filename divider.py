""" this script runs a recursive function to test the Collatz conjecture. This conjecture states that a number leads to
1 if it is continuously divided by 2, when it cannot be divided by two it is multiplied by three and 1 added,
and the cycle continuous. Started of as a diner conversation. See: https://en.wikipedia.org/wiki/Collatz_conjecture """
from numpy.random import randint, seed
from numbers import Integral
from sys import setrecursionlimit

# increase recursion depth limit to avoid hitting it (1000 works with numbers up to default highest number of 1000
setrecursionlimit(1000)


def is_divisible_by_two(input_number, progress_tracker=None):
    """ this function checks if a number can be divided by 2, if so it return the result of that division,
    else it multiplies by 3 and add 1 to input number.
    If the input number is equal to 1 the function stops calling itself. """
    if progress_tracker is None:
        # first time the function is being run, initialize tracker
        progress_tracker = list()

    if input_number != 1 and input_number % 2 == 0:
        # is divisible by 2
        output_number = input_number // 2
        output_string = "{:8d} is divisible by 2. Output number is {:d}".format(input_number, output_number)
    elif input_number != 1 and input_number % 2 != 0:
        # is not divisible by 2
        output_number = input_number * 3 + 1
        output_string = "{:8d} is **not** divisible by 2. Output number is {:d}".format(input_number, output_number)
    else:
        # means input equal to 1, end recursion
        output_string = "Input number is {:d}, the end has been reached".format(input_number)
        progress_tracker.append(output_string)
        return input_number, progress_tracker

    # call function again with new output_number
    progress_tracker.append(output_string)
    return is_divisible_by_two(output_number, progress_tracker=progress_tracker)


def analyse_number(input_number, report_steps_taken=True, report_final_result=True):
    """
    This function serves as a wrapper for the is_divisible_by_two function
    :param input_number: a single integer that one wants to check
    :param report_steps_taken: should each iteration be printed out?
    :param report_final_result: should the final conclusion be printed?
    :return: None
    """
    # check the input_number type (became redundant after adding generate_number_array())
    # the numbers.Integral ensures that np.int32 is recognized as an integer (abstract class)
    # alternative to numbers.Integral: operator.index()
    assert isinstance(input_number, Integral) is True, "{} is not an integer".format(input_number)

    if input_number != 0:
        final_number, progress_list = is_divisible_by_two(input_number)
        if report_final_result is True:
            print("{:8d} led to final number: {:d}".format(input_number, final_number))
        if report_steps_taken is True:
            for line in progress_list:
                print(line)
    else:
        # zero is not divisible
        if report_final_result is True:
            print("{:8d} is indivisible".format(input_number))

    return None


def generate_number_array(number_of_integers=10, lowest_number=0, highest_number=1000, number_type=int):
    """ this function generates an array of random integers 
    :rtype: np.array
    """
    seed(1234)  # numpy.random.seed seeds the random number generator (for reproducibility purposes)

    number_array = randint(low=lowest_number, high=highest_number, size=number_of_integers, dtype=number_type)

    return number_array


if __name__ == "__main__":
    # add visualization
    # implement multiprocessing
    # make number_of_numbers an input argument for the script
    number_of_numbers = 1000
    test_number_array = generate_number_array(number_of_numbers)

    for number in test_number_array:
        try:
            analyse_number(input_number=number, report_steps_taken=False, report_final_result=True)
        except RuntimeError as e:
            print("Recursion depth exceeded with number {:d}, please increase recursion limit at top of the file."
                  .format(number))
        except Exception as e:
            print("Unexpected error: {}".format(e))
