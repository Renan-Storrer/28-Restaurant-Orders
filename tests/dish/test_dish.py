from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish1 = Dish("x-burguer", 25.0)
    dish2 = Dish("coxinha", 5.0)
    dish1.add_ingredient_dependency(Ingredient("queijo mussarela"), 2)
    dish2.add_ingredient_dependency(Ingredient("farinha"), 1)

    assert dish1.name == "x-burguer"
    assert dish2.name == "coxinha"

    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)

    assert dish1 == dish1
    assert dish1 != dish2

    assert repr(dish1) == "Dish('x-burguer', R$25.00)"
    assert repr(dish2) == "Dish('coxinha', R$5.00)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("x-burguer", "25.0")
    with pytest.raises(ValueError, match="Dish price must be greater than zero."):
        Dish("coxinha", 0)

    assert dish1.recipe.get(Ingredient("queijo mussarela")) == 2
    assert dish2.recipe.get(Ingredient("farinha")) == 1

    assert dish1.get_restrictions() == {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert dish2.get_restrictions() == {Restriction.GLUTEN}

    assert dish1.get_ingredients() == {Ingredient("queijo mussarela")}
    assert dish2.get_ingredients() == {Ingredient("farinha")}
