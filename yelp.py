'''
This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going
forward from that element. Write a function to return the minimum number of jumps you must take in order to get from
the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping
from 6 to 5, and then from 5 to 9.
'''


def yelp(my_list):
    if my_list[0] == 0:
        return 0
    start = my_list[0]
    counter = 1
    while start < len(my_list):
        jump_list = my_list[(my_list.index(start) + 1):(start + 1)]
        start = max(jump_list)
        my_list = my_list[start:(len(my_list) - 1)]
        counter += 1
    return counter


assert yelp([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == 2
