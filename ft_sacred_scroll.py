import alchemy

if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}\
")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}\
")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n")
    print("Testing package-level access (controlled by __init__.py):")
    for name in ("create_fire", "create_water", "create_earth", "create_air"):
        print(f"alchemy.{name}(): ", end="")
        func = getattr(alchemy, name, None)
        if func is None:
            print("AttributeError - not exposed")
        else:
            print(func())
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
