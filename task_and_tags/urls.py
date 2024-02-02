from django.urls import path

from task_and_tags.views import TaskListView, TagsCreateView, TagsUpdateView, TagsDeleteView, TagListView, \
    TaskCreateView, TaskDeleteView, TaskUpdateView, TaskChangeStatus

urlpatterns = [

    # tasks urls

    path("", TaskListView.as_view(), name="home-page"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/update-status/", TaskChangeStatus.as_view(), name="task-change-status"),

    # tag urls

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag-delete"),

]

app_name = "task_and_tags"
