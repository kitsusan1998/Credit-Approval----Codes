# -*- coding: utf-8 -*-


def _init():  # initialization
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    # define a globle val
    _global_dict[key] = value

    print(_global_dict.keys())


def get_value(key):
    print(_global_dict.keys())
    # get a global var
    try:
        return _global_dict[key]
    except:
        print('read' + key + 'failed\r\n')
    finally:
        return None
