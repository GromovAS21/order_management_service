from typing import Union

from django.core.paginator import Paginator
from django.db.models import QuerySet


class PaginationService:
    """Сервис для работы с пагинацией"""

    @staticmethod
    def paginate(queryset: QuerySet, page_size: int, page_number: int) -> Paginator:
        paginator = Paginator(queryset, page_size)
        page = paginator.get_page(page_number)
        return page


def number_of_lines(items: Union[list, QuerySet]) -> list[int]:
    """
    Нумерация строк в списке
    """
    number = [number for number in range(1, len(items) + 1)]
    return number
