def print_class_meth_name(*initial_args, **initial_kwargs):

    def _print_class_meth_name(method):

        def wrapper_initial(instance, *method_args, **method_kwargs):
            print_args_kwargs(*initial_args, **initial_kwargs)
            print(f"Before \"{instance.__class__.__name__}.{method.__name__}\"")
            result = method(instance, *method_args, **method_kwargs)
            return result

        return wrapper_initial

    return _print_class_meth_name


def print_callable_name(*initial_args, **initial_kwargs):

    def _print_callable_name(_callable):

        def wrapper_initial(*callable_args, **callable_kwargs):
            print_args_kwargs(*initial_args, **initial_kwargs)
            print(f"Before \"{_callable.__name__}\"")
            result = _callable(*callable_args, **callable_kwargs)
            return result

        return wrapper_initial

    return _print_callable_name


def print_args_kwargs(*args, **kwargs):
    if args:
        for a in args:
            print(a)
    if kwargs:
        print(kwargs)
