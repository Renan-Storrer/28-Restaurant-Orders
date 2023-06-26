# Req 3
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient
from collections import defaultdict


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.read_file(source_path)

    def read_file(self, source_path):
        with open(source_path) as file:
            reader = csv.reader(file)
            next(reader)
            self.load_data(reader)

    def load_data(self, reader):
        dish_data = defaultdict(set)

        for row in reader:
            dish_name = row[0]
            dish_price = float(row[1])
            dish_ingredient = row[2]
            dish_recipe_amount = int(row[3])

            dish = dish_data.setdefault(dish_name, Dish(dish_name, dish_price))

            dish.add_ingredient_dependency(
                Ingredient(dish_ingredient), dish_recipe_amount
            )

        self.dishes = set(dish_data.values())