def rgb(r: int, g: int, b: int) -> tuple[float, float, float]:
    return normalize_integer(r), normalize_integer(g), normalize_integer(b)


def rgba(r: int, g: int, b: int, a: int) -> tuple[float, float, float, float]:
    r, g, b = rgb(r, g, b)
    a = normalize_integer(a)
    return r, g, b, a


def normalize_integer(integer) -> float:
    minimum = 0
    maximum = 255
    return (integer - min(integer, minimum)) / (max(integer, maximum) - min(integer, minimum))  # Normalizes into 0 - 1
