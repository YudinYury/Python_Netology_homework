"""lesson_3_8_Classwork "Patterns"

"""

current_value = 0
STORAGE = {}


def register(command):
    def decorator(fn):
        STORAGE[command] = fn

        return fn

    return decorator


@register('+')
def cmd_add(data):
    global current_value
    current_value += int(data[1:])


@register('-')
def cmd_sub(data):
    global current_value
    current_value -= int(data[1:])


@register('C')
def cmd_sub(data):
    global current_value
    current_value = 0


while True:
    data = input('+ , - , C')
    cmd = data[0]
    if cmd in STORAGE:
        STORAGE[cmd](data[1:])
    else:
        print('Unknow command')
    print(current_value)


# def main():
#     pass
#     # current_value = 0
#     # while True:
#     #     data = input('+ , - , C')
#     #     if data[0] == '+':
#     #         current_value += int(data[1:])
#     #     elif data[0] == '-':
#     #         current_value -= int(data[1:])
#     #     elif data[0].upper() == 'C':
#     #         current_value = 0
#
#
# if __name__ == '__main__':
#     main()
