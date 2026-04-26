def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.light_validator import validate_ingredients
    validated_result = validate_ingredients(ingredients)
    if "VALID" in validated_result:
        return (f"Spell recorded: {spell_name} ({validated_result})")
    return "Spell not recorded!"
