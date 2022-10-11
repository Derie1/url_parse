import url_parse as url


def test_url():
    u = url.make('https://domain.org/community?q=low')
    assert url.to_string(u) == 'https://domain.org/community?q=low'

    u = url.set_host(u, 'hexlet.io')
    assert url.get_host(u) == 'hexlet.io'
    assert url.to_string(u) == 'https://hexlet.io/community?q=low'

    u = url.set_scheme(u, 'http')
    assert url.get_scheme(u) == 'http'
    assert url.to_string(u) == 'http://hexlet.io/community?q=low'

    u = url.set_path(u, '/404')
    assert url.get_path(u) == '/404'
    assert url.to_string(u) == 'http://hexlet.io/404?q=low'

    u = url.set_query_param(u, 'page', 5)
    assert url.to_string(u) == 'http://hexlet.io/404?q=low&page=5'

    u = url.set_query_param(u, 'q', 'high')
    assert url.to_string(u) == 'http://hexlet.io/404?q=high&page=5'
    assert url.get_query_param(u, 'q') == 'high'
    assert url.get_query_param(u, 'user', 'guest') == 'guest'
    assert url.get_query_param(u, 'b') is None

    u = url.set_query_param(u, 'q', None)
    assert url.to_string(u) == 'http://hexlet.io/404?page=5'

    u = url.set_query_param(u, 'missed', None)
    assert url.to_string(u) == 'http://hexlet.io/404?page=5'


def test_url_with_empty_params():
    u = url.make('https://hexlet.io/community')
    assert url.to_string(u) == 'https://hexlet.io/community'


def test_url_with_empty_path():
    u = url.make('https://hexlet.io/?q=high&page=5')
    assert url.to_string(u) == 'https://hexlet.io/?q=high&page=5'
