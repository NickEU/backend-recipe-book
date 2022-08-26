from typing import Tuple


def wrap_with_braces(values: Tuple[str]) -> str:
    return ','.join(map(lambda x: f"('{x}')", values))
