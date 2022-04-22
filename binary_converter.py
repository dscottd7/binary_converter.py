# Author: D. Scott DiPerna
# GitHub username: dscottd7
# Date: 4/21/2022
# Description: a recursive function that converts a positive integer into a binary string

def recursive_binary_function(number, bin_string):
    """
    function that takes an integer and a string and continues to call itself until it has completed the translation
    into a binary string
    :param number:
    :param bin_string:
    :return: string of binary number
    """
    remainder = number % 2
    bin_string = str(remainder) + bin_string
    while number > 1:
        return recursive_binary_function(int(number / 2), bin_string)
    for places in range(4 - len(bin_string) % 4):
        bin_string = "0" + bin_string
    return bin_string

def main():
    integer = int(input("Enter a positive integer: "))
    string = ""
    print(recursive_binary_function(integer, string))

if __name__ == '__main__':
    main()

