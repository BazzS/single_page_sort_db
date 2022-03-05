from django.db.models.query import QuerySet
from django.core.paginator import Paginator


def pagination_manager(model_objects: QuerySet, per_page: int,
                       orphans: int, request_page: int):
    """Returns page_obj and pages numbers"""
    paginator = Paginator(model_objects, per_page=per_page, orphans=orphans)
    page_obj = paginator.get_page(request_page)

    start_page, end_page = page_obj.start_index(), page_obj.end_index()
    current_page = page_obj.number

    prev_page = current_page - 1 if current_page != start_page else None
    next_page = current_page + 1 if current_page != end_page else None

    return page_obj, {
        "start_page": start_page,
        "end_page": end_page,
        "current_page": current_page,
        "prev_page": prev_page,
        "next_page": next_page,
    }
