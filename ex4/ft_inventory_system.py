
import sys


def ft_inventory_system() -> dict[str, int]:

    inventory = {}

    for arg in sys.argv[1:]:

        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, quantity = arg.split(':')

        if item in inventory:
            print(f"Redudant item '{item} - discarding")
            continue

        try:
            inventory[item] = int(quantity)

        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")

    return inventory


if __name__ == '__main__':
    print("=== Inventory System Analysis ===")

    inventory = ft_inventory_system()
    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list {items}")

    amount = sum(inventory.values())
    print("Total quantity of the", len(items), "items:", amount)

    for item, quantity in inventory.items():

        percentage = round(quantity / amount * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant = items[0]
    least_abundant = items[0]

    for item, quantity in inventory.items():

        if quantity > inventory[most_abundant]:
            most_abundant = item
        if quantity < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant}"
          "with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant}"
          "with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Inventory update: {inventory}")
