from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 12  #  количество элементов на странице
    page_query_param = 'page'  # Параметр для запроса страниц, по умолчанию 'page'
    page_size_query_param = 'page_size'  # Разрешить клиенту переопределить размер страницы с помощью этого параметра запроса
    max_page_size = 100  # Максимальный лимит для размера страницы