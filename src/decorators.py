import os
from functools import wraps
from typing import Optional, Callable, Any
from config import path


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который записывает логи работы функции"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename:
                try:
                    result = func(*args, **kwargs)
                except Exception as error:
                    with open(
                        os.path.join(path, f"{filename}.txt"), "a", encoding="utf-8"
                    ) as file:
                        file.write(
                            f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n"
                        )
                else:
                    with open(
                        os.path.join(path, f"{filename}.txt"), "a", encoding="utf-8"
                    ) as file:
                        file.write(f"{func.__name__} ok\n")
                    return result
            else:
                try:
                    result = func(*args, **kwargs)
                except Exception as error:
                    print(
                        f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n"
                    )
                else:
                    print(f"{func.__name__} ok")
                    return result

        return wrapper

    return my_decorator


if __name__ == "__main__":  # pragma: no cover

    @log()
    def example_function(a, b):
        """Складывает два числа"""
        return a + b

    @log(filename="my_log")
    def example_function(a, b):
        """Складывает два числа"""
        return a + b

    example_function("3", 2)
    example_function(3, 2)
    print(example_function(3, 2))
    example_function()
