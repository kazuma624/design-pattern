from settings import settings


settings.foo = 123

from settings import settings as s2

print(s2.foo)
