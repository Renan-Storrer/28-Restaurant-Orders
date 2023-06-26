import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str):
        dish_data = {}

        with open(source_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho

            for row in reader:
                dish_name = row[0]
                dish_price = float(row[1])
                dish_ingredient = row[2]
                dish_recipe_amount = int(row[3])

                dish = dish_data.get(dish_name)
                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    dish_data[dish_name] = dish

                dish.add_ingredient_dependency(Ingredient(dish_ingredient), dish_recipe_amount)

        return set(dish_data.values())
