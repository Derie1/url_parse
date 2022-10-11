from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


"""
>>> o = urlparse("http://docs.python.org:80/3/library/urllib.parse.html?"
...              "highlight=params#url-parsing")
>>> o
ParseResult(scheme='http', 
            netloc='docs.python.org:80',
            path='/3/library/urllib.parse.html', 
            params='',
            query='highlight=params', 
            fragment='url-parsing')
"""


def make(url):
    return url


def get_scheme(data):
    url = urlparse(data)
    return url[0]


def set_scheme(data, scheme):
    url = urlparse(data)
    new_url = url._replace(scheme=scheme)
    return urlunparse(new_url)


def get_host(data):
    url = urlparse(data)
    return url[1]


def set_host(data, host):
    url = urlparse(data)
    new_url = url._replace(netloc=host)
    return urlunparse(new_url)


def get_path(data):
    url = urlparse(data)
    return url[2]


def set_path(data, path):
    url = urlparse(data)
    new_url = url._replace(path=path)
    return urlunparse(new_url)


def get_query_param(data, param_name, default=None):
    url = urlparse(data)
    url_qs = parse_qs(url[4])  # <--- dict {param_name: value, ...}
    if param_name in url_qs.keys():
        query_param = url_qs[param_name]
        return query_param[0]
    else:
        return default


def set_query_param(data, key, value):
    url = urlparse(data)
    url_qs = parse_qs(url[4])  # <--- dict {param_name: value, ...}
    new_qs = url_qs.copy()
    if value is None:
        if key in new_qs.keys():
            new_qs.pop(key)
    else:
        new_qs[key] = str(value)
    new_query = urlencode(new_qs, doseq=True)
    new_url = url._replace(query=new_query)
    return urlunparse(new_url)


def to_string(data):
    return str(data)
