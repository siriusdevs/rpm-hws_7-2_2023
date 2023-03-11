"""Greeting generator."""


def greeting(name: str) -> str:
    """Greeting generator - with a capitalized username.

    Args:
        name: Username

    Returns:
        str: the greeting and a capitalized username
    """
    cap_name = ' '.join([initial.capitalize() for initial in name.split()])
    return 'Привет, {0}'.format(cap_name)
