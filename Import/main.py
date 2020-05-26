# import config
from config import *
import sys

def func_():
	print("Hello")
	return

# sys.path.append("....")
# print(globals())
# print(locals())
# print(dir(config))
# print(config.token)

try:
    print(dontimportthis)
except NameError:
    print(f"dontimportthis was not imported - it is okey")
print(token)
token = __name__ + "/token"

#from config import token
print(token)