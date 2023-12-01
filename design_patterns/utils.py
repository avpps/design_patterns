def print_class_meth_name(method, *method_args, **method_kwargs):

    def wrapper_initial(instance, *initial_args, **initial_kwargs):

        def wrapper():
            print(f"From {instance.__class__.__name__}.{method.__name__}")
            return method(instance, *initial_args, **initial_kwargs)

        return wrapper()

    return wrapper_initial
