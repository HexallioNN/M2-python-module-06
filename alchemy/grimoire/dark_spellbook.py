from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validated_result = validate_ingredients(ingredients)
    if "VALID" in validated_result:
        return (f"Spell recorded: {spell_name} ({validated_result})")
    return "Spell not recorded!"
