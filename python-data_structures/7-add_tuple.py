#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples element-wise with missing values treated as 0."""
    a1, a2 = (tuple_a + (0, 0))[:2]  # Ensure at least two elements
    b1, b2 = (tuple_b + (0, 0))[:2]  # Ensure at least two elements
    return (a1 + b1, a2 + b2)
