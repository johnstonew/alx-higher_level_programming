#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_c = tuple_a + (0,0)
    tuple_b_c = tuple_b + (0,0)
    new_tuple = tuple_a_c[0] + tuple_b_c[0], tuple_a_c[1] + tuple_b_c[1]
    return new_tuple
