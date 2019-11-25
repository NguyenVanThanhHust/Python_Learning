__my_name__ = 'Nguyen Van Thanh'
__mail__ = "NguyenVanThanhHust@gmail.com"
__content__ = "done use this code"

from builtins import print as _print
def my_print(*args, **kwargs):
    _print(*args, **kwargs)
    _print(f'Follow me on facebook: @{__content__}'.rjust(80, ' '))

if __name__ == '__main__':
    my_print(__my_name__)
    my_print(__mail__)