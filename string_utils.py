"""Small string utility library — demo target for agend-terminal fleet."""

import re


def slugify(text: str) -> str:
    """Convert text to a URL-safe slug.

    Lowercases, replaces runs of non-alphanumeric characters with a single
    hyphen, and strips leading/trailing hyphens.
    """
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncate text to max_len characters, appending suffix when cut.

    If text fits within max_len, return as-is. Otherwise cut so the final
    string (including suffix) is exactly max_len characters.
    """
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix


def camel_to_snake(name: str) -> str:
    """Convert CamelCase / camelCase to snake_case.

    Handles consecutive capitals (e.g. ``HTTPSConnection`` →
    ``https_connection``).
    """
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()
