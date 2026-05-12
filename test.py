def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b

print(add(2, 3)) # Output:
# Calling add
# Done  

## Flow of Execution: 
# 1. The `add` function is defined and decorated with `@log_decorator`.
# 2. When `add(2, 3)` is called, it actually calls the `wrapper` function defined inside `log_decorator`.
# 3. The `wrapper` function prints "Calling add", then calls the original `add` function with the provided arguments (2 and 3).
# 4. The original `add` function executes and returns the result (5).
# 5. The `wrapper` function then prints "Done" and returns the result (5) to the caller.    
