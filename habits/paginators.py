from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Выводит по 5 привычек на одной странице
    """
    page_size = 5
