from ROBOT_API import *

who_was_here = whats_my_name()
items_in_bucket = add_to_bucket(1)
seconds = get_seconds_passed()

print(who_was_here)
print(f"{seconds} seconds have passed.")
print(f"there are {items_in_bucket} items in the bucket")