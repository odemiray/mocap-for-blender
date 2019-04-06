import ctypes
import os

lib = ctypes.cdll.LoadLibrary(
    'c:\\Users\\Nacnoad\\Desktop\\CLEye\\test\\multicam.so')
a = lib.getUid()
print(a)
