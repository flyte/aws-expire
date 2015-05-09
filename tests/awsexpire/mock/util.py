import logging
log = logging.getLogger("mockboto")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)


def log_args(func):
    def log_args_wrapper(*args, **kwargs):
        arg_strs = []
        [arg_strs.append(x) for x in args]
        [arg_strs.append("%s=%s" % (k, v)) for k, v in kwargs.items()]
        msg = "%s(%s)" % (func.func_name, ", ".join(arg_strs))
        log.info("MOCK FUNCTION: %s" % msg)
        func(*args, **kwargs)
    return log_args_wrapper
