def print_class_meth_name(*initial_args, **initial_kwargs):

    def _print_class_meth_name(method):

        def wrapper_initial(instance, *method_args, **method_kwargs):
            # TODO: make use of initial_args and initial_kwargs there
            print(f"From {instance.__class__.__name__}.{method.__name__}")
            result = method(instance, *method_args, **method_kwargs)
            return result

        return wrapper_initial

    return _print_class_meth_name
