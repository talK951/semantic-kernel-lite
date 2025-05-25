from typing import Callable, Optional

def kernel_function(name: str="", description: str=""):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f"Calling kernel function: {name}")
            print(f"function description={description}")
            result = func(*args, **kwargs)
            print(f"Result: {result}")
            return result

        wrapper.kernel_name = name
        wrapper.kernel_description = description
        return wrapper
    return decorator