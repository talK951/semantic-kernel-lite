from typing import Callable, Optional

def kernel_function(name: str="", description: str=""):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        wrapper.kernel_name = name
        wrapper.kernel_description = description
        return wrapper
    return decorator