import yaspin

from utils.text import cstring

custom_spinner = yaspin.Spinner(
    [
        cstring("[&e⠋&r]"),
        cstring("[&e⠙&r]"),
        cstring("[&e⠹&r]"),
        cstring("[&e⠸&r]"),
        cstring("[&e⠼&r]"),
        cstring("[&e⠴&r]"),
        cstring("[&e⠦&r]"),
        cstring("[&e⠧&r]"),
        cstring("[&e⠇&r]"),
        cstring("[&e⠏&r]"),
    ],  # type: ignore
    80,
)
