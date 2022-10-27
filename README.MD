# url_parse
Реализация задачи по созданию, изменению и извлечению частей url-адреса через абстракции данных.
Пользователь может применять готовые функции и пользоваться ими без необходимости понимания, как они реализованы.

# Интерфейс:

### make(url)
 - Конструктор. Создает URL.

### get_scheme(data)
 - Селектор (геттер). Извлекает схему.

### set_scheme(data, scheme)
 - Сеттер. Меняет схему.

### get_host(data)
 - Геттер. Извлекает host.

### set_host(data, host)
 - Сеттер. Меняет host.

### get_path(data)
 - Геттер. Извлекает путь.

### set_path(data, path)
 - Сеттер. Меняет путь.

### get_query_param(data, param_name, default=None)
 - Геттер. Извлекает значение для параметра запроса. Третьим параметром функция принимает значение по умолчанию, 
которое возвращается тогда, когда в запросе не было такого параметра

### set_query_param(data, key, value)
 - Сеттер. Устанавливает значение для параметра 
запроса. Если передано значение None, то параметр отбрасывается.

### to_string(data)
 - Геттер. Преобразует URL в строковой вид.

Все сеттеры возвращают новый изменённый URL, а старый оставляют неизменным.


## Примеры применения ##
```
import url
u = url.make('https://hexlet.io/community?q=low')
u = url.set_scheme(u, 'http')
url.to_string(u)  # 'http://hexlet.io/community?q=low'
u = url.set_path(u, '/404')
url.to_string(u)  # 'http://hexlet.io/404?q=low'
url.get_query_param(u, 'q')  # 'low'
u = url.set_query_param(u, 'page', 5)
url.to_string(u)  # 'http://hexlet.io/404?q=low&page=5'
u = url.set_query_param(u, 'q', 'high')
url.to_string(u)  # 'http://hexlet.io/404?q=high&page=5'
u = url.set_query_param(u, 'q', None)
url.to_string(u)  # 'http://hexlet.io/404?page=5'
```