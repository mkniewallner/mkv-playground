from contextlib import closing
from urllib.request import Request
from urllib.request import urlopen

request = Request("https://pypi.org/pypi/poetry/json", headers={"User-Agent": "Python Poetry"})

with closing(urlopen(request)) as r:
    print(r.read())
