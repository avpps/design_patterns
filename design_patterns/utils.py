def print_class_meth_name(*initial_args, **initial_kwargs):

    def _print_class_meth_name(method):

        def wrapper_initial(instance, *method_args, **method_kwargs):
            print_args_kwargs(*initial_args, **initial_kwargs)
            print(f"Before \"{instance.__class__.__name__}.{method.__name__}\"")
            result = method(instance, *method_args, **method_kwargs)
            return result

        return wrapper_initial

    return _print_class_meth_name


def print_callable_name(*args, **kwargs):

    def wrapper(func):
        print_args_kwargs(*args, **kwargs)
        print(f"Before \"{func.__name__}\"")
        return func

    return wrapper


def print_args_kwargs(*args, **kwargs):
    if args:
        print(args)
    if kwargs:
        print(kwargs)
