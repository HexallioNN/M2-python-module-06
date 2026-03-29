def validate_ingredients(ingredients: str) -> str:
    ingredient_list = ["fire", "water", "earth", "air"]
    for x in ingredient_list:
        if x in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
