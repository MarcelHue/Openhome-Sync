import ctypes
import pyautogui
import os
import sys

_dll = None
_dll_get_pixel = None


def _get_dll():
    global _dll, _dll_get_pixel
    if _dll is None:
        dll_path = os.path.join(os.path.dirname(__file__), "win_readmouse.dll")
        _dll = ctypes.CDLL(dll_path)
        _dll.get_pixel.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        _dll.get_pixel.restype = None
        _dll_get_pixel = _dll.get_pixel
    return _dll_get_pixel


def get_pixel(position_list):
    if sys.platform.startswith("win32") or sys.platform.startswith("cygwin") or sys.platform.startswith("msys"):
        result_lst = []
        dll_get_pixel = _get_dll()
        rgb = (ctypes.c_int * 3)()

        for pos in position_list:
            dll_get_pixel(pos[0], pos[1], rgb)
            result_lst.append([rgb[0], rgb[1], rgb[2]])

        return result_lst
    elif sys.platform.startswith('linux'):
        result_lst = []

        for pos in position_list:
            r, g, b = pyautogui.pixel(pos)
            result_lst.append([r, g, b])

        return result_lst

    else:
        raise Exception("Not an supported Platform yet!")