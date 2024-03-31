from django.urls import path
from ex.views import add_comment, article_details


urlpatterns = [
    path("article/<int:article_id>/", article_details, name="article_detail"),
    path(
        "add_comment/<str:content_type>/<int:object_id>/",
        add_comment,
        name="add_comment",
    ),
]
