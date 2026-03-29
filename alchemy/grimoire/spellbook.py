def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    new_ingredients = validate_ingredients(ingredients)
    if "INVALID" not in new_ingredients:
        return f"Spell recorded: {spell_name} ({new_ingredients})"
    else:
        return f"Spell rejected: {spell_name} ({new_ingredients})"
