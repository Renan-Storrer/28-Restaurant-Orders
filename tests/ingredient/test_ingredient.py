from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("farinha")

    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient1) != hash(ingredient2)

    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2

    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert repr(ingredient2) == "Ingredient('farinha')"

    assert ingredient1.name == "queijo mussarela"
    assert ingredient2.name == "farinha"

    assert ingredient1.restrictions == {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient2.restrictions == {Restriction.GLUTEN}
