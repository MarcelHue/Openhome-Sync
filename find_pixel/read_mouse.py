import ctypes
import pyautogui
import os
import sys


def get_pixel(position_list):
    if sys.platform.startswith("win32") or sys.platform.startswith("cygwin") or sys.platform.startswith("msys"):
        result_lst = []

        DLL_PATH = os.path.join(os.path.dirname(__file__), "win_readmouse.dll")
        dll = ctypes.CDLL(DLL_PATH)

        dll.get_pixel.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        dll.get_pixel.restype = None

        rgb = (ctypes.c_int * 3)()

        for pos in position_list:
            dll.get_pixel(pos[0], pos[1], rgb)
            result_lst.append([rgb[0], rgb[1], rgb[2]])

        #print("R =", rgb[0])
        #print("G =", rgb[1])
        #print("B =", rgb[2])

        return result_lst
    elif sys.platform.startswith('linux'):
        result_lst = []

        for pos in position_list:
            r, g, b = pyautogui.pixel(pos)
            result_lst.append([r, g, b])

        return result_lst

    else:
        raise Exception("Not an supported Platform yet!")