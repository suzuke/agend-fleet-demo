"""Tests for string_utils — kept tiny + obvious for demo readability."""

from string_utils import camel_to_snake, is_palindrome, slugify, truncate


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_chars():
    assert slugify("Foo! Bar?") == "foo-bar"


def test_slugify_strips_leading_trailing():
    assert slugify("  spaced  ") == "spaced"


def test_truncate_short_passes_through():
    assert truncate("hi", 10) == "hi"


def test_truncate_long_appends_suffix():
    assert truncate("hello world", 8) == "hello..."


def test_camel_to_snake_basic():
    assert camel_to_snake("camelCase") == "camel_case"


def test_camel_to_snake_multiple_caps():
    assert camel_to_snake("HTTPSConnection") == "https_connection"


def test_is_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
