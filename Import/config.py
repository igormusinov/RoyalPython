__all__ = [
    'token'
]

print(f"{__file__} is importing")

from time import sleep
sleep(2)

token = __name__ + "/token"
dontimportthis = __name__ + "/XXX"
print(f"Finish importing {__file__}")

