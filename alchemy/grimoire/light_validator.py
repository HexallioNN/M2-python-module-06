from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ingredient_list = [i.strip().lower() for i in ingredients.split(",")]

    for ingredient in ingredient_list:
        if ingredient in allowed:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
