def snake_to_pascal(snake_string: str):
    return snake_string.replace("_", " ").title().replace(" ", "")
