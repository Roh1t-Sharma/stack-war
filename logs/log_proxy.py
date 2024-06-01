from .logger import get_logger

class LogProxy:
    """
    A proxy class that logs actions before executing them.
    """
    def __init__(self, target):
        self._target = target
        self._logger = get_logger()

    def __getattr__(self, attr):
        original_attr = self._target.__getattribute__(attr)

        if callable(original_attr):
            def hooked(*args, **kwargs):
                self._logger.debug(f"Calling {attr} with args {args} and kwargs {kwargs}")
                result = original_attr(*args, **kwargs)
                self._logger.debug(f"{attr} returned {result}")
                return result
            return hooked
        else:
            return original_attr
