from django.urls import path

from task_and_tags.views import index, TagsCreateView, TagsUpdateView, TagsDeleteView, TagListView

urlpatterns = [
    path("", index, name="home-page"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag-delete"),
]

app_name = "task_and_tags"
