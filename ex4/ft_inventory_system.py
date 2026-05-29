#!/usr/bin/env python3

import sys

if __name__ == "__main__":
   print("=== Inventory System Analysis ===") 

   args = sys.argv[1:]
   inventory = {}
   for arg in args:
       key, seperator, value = arg.partition(':')

       if not seperator:
           print(f"Error - invalid parameter '{arg}'")
           continue

       if key in inventory:
           print(f"Redundant item '{key}' - discarding")
           continue

       try:
           val = int(value)
           if val <= 0:
               raise Exception(f"Error - for item '{key}' value must be greater than 0")
           inventory[key] = val

       except ValueError as e:
           print(f"Quantity error for '{key}': {e}")
       except Exception as e:
           print(e)

   if inventory:
       keys = list(inventory.keys())
       sum_values = sum(inventory.values())

       print(f"Got inventory: {inventory}")
       print(f"Item list: {keys}")
       print(f"Total quantity of the {len(keys)} items: {sum_values}")

       for key in keys:
           percentage = round((inventory[key] / sum_values) * 100, 1)
           print(f"Item {key} represents {percentage}%")

           max_key = max(inventory, key=inventory.get)
           min_key = min(inventory, key=inventory.get)

           print(f"Item most abundant: {max_key} with quantity {inventory[max_key]}")
           print(f"Item least abundant: {min_key} with quantity {inventory[min_key]}")

           inventory["magic_item"] = int(1)

           print(f"Updated inventory: {inventory}")
