#!/usr/bin/env python3
import random

from ROBOT_API import whats_my_name
from ROBOT_API import add_to_bucket
from ROBOT_API import get_seconds_passed
from ROBOT_API import get_data

who_was_here = whats_my_name()
items_in_bucket = add_to_bucket(1)
seconds = get_seconds_passed()

print(get_data())
# print(who_was_here)
# print(f"{seconds} seconds have passed.")
# print(f"There are {items_in_bucket} items in the bucket")