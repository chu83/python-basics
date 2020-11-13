#레퍼런스 카운트

import sys

x = object()
print(type(x))
print(sys.getrefcount(x))