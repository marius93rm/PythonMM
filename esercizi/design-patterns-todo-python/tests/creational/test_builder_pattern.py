from creational.builder_pattern import Meal, MealBuilder, prepare_combo


def test_builder_creates_meal_with_all_components() -> None:
    builder = MealBuilder()
    meal = (
        builder.add_main("Burger")
        .add_side("Fries")
        .add_drink("Cola")
        .build()
    )
    assert isinstance(meal, Meal)
    assert meal.main == "Burger"
    assert meal.side == "Fries"
    assert meal.drink == "Cola"


def test_prepare_combo_uses_builder_defaults() -> None:
    builder = MealBuilder()
    combo = prepare_combo(builder)
    assert combo.describe() == "Meal(main=Veggie Burger, side=Salad, drink=Lemonade)"
