"""lesson_3_8_Classwork "Patterns"

"""


# import osa
# from xml.etree.ElementTree import fromstring, ElementTree

# def one():
#     return 1
#
# _one = one
# def two():
#     print('exec one()')
#     return _one()

# def decorator_factory(text_before='exec', text_after='finished'):
#     def decorator(fn):
#         def wrapper(*args, **kwargs):
#             print(text_before, fn, args, kwargs)
#             result = fn(*args, **kwargs)
#             print(text_after, fn, result)
#             return result
#
#         return wrapper
#     return decorator

def decorator(fn):
    # @wraps(fn)  #  чтобы видеть по команде help(my_sum_2) подсказку, которую сам написал
    def wrapper(*args, **kwargs):
        print('before', fn, args, kwargs)
        result = fn(*args, **kwargs)
        print('after', fn, result)
        return result

    return wrapper


@decorator
def one():
    return 1


@decorator
def two():
    return 2


# @decorator_factory('before_exec', 'after_exec')
# def my_sum(a,b):
#     return a+b

@decorator
def my_sum_2(a, b):
    return a + b


def main():
    # print(one())
    # print(two())
    print(my_sum_2(3, 5))
    print(my_sum_2)


if __name__ == '__main__':
    main()
