from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):

    page_size = 6

    ordering = 'id'

    # cursor_query_param = 'cu'