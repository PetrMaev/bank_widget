import os
from functools import wraps
from typing import Optional, Callable, Any


def log(filename: Optional[str]=None)-> Callable:
    """ Декоратор, который записывает логи работы функции """

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename:
                try:
                    result = func(*args, **kwargs)
                except Exception as error:
                    with open(os.path.join(f'{filename}.txt'), 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n')
                else:
                    with open(os.path.join(f'{filename}.txt'), 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ok\n')
                    return result
            else:
                try:
                    result = func(*args, **kwargs)
                except Exception as error:
                    print(f'{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n')
                else:
                    print(f'{func.__name__} ok')
                    return result
        return wrapper
    return my_decorator
