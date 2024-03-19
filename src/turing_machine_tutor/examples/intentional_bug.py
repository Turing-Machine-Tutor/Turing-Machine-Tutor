from typing import Optional


class intentional_bug:  # noqa don't check class name
    default_activated = False

    def __init__(self, activated: Optional[bool] = None):
        self._activated = activated

    def __call__(self, func):
        on = self.default_activated if self._activated is None else self._activated
        if on:
            func()
        return func
