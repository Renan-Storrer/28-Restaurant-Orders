from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = {}

    with open(inventory_file_path, encoding="utf-8") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ingredient in recipe:
            not_available = ingredient not in self.inventory
            not_have_qnt = self.inventory.get(ingredient, 0) < int(recipe[ingredient])

            if not_available or not_have_qnt:
                return False

        return True

    def consume_recipe(self, recipe: Recipe) -> None:
        if not self.check_recipe_availability(recipe):
            raise ValueError("Recipe ingredients not available in inventory.")

        for ingredient, amount in recipe.items():
            self.inventory[ingredient] -= int(amount)
