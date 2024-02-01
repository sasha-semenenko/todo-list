from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView

from task_and_tags.models import Tasks, Tag

class TagListView(generic.ListView):
    model = Tag
    template_name = "task_and_tags/tag_list.html"
    queryset = Tag.objects.all()


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_and_tags:tag-list")
    template_name = "task_and_tags/tags_create.html"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "task_and_tags/tag_confirm_delete.html"
    success_url = reverse_lazy("task_and_tags:tag-list")


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_and_tags:tag-list")
    template_name = "task_and_tags/tags_create.html"


class TaskListView(generic.ListView):
    model = Tasks
    fields = "__all__"
    queryset = Tasks.objects.prefetch_related("tags")
    template_name = "task_and_tags/index.html"


class TaskCreateView(generic.CreateView):
    model = Tasks
    fields = "__all__"
    template_name = "task_and_tags/task_create.html"
    success_url = reverse_lazy("task_and_tags:home-page")


class TaskUpdateView(generic.UpdateView):
    model = Tasks
    fields = "__all__"
    template_name = "task_and_tags/task_create.html"
    success_url = reverse_lazy("task_and_tags:home-page")


class TaskDeleteView(generic.DeleteView):
    model = Tasks
    template_name = "task_and_tags/task_confirm_delete.html"
    success_url = reverse_lazy("task_and_tags:home-page")


class TaskChangeStatus(generic.UpdateView):

    def post(self, request, *args, **kwargs):

        task = get_object_or_404(Tasks, pk=kwargs["pk"])

        if not task.task_is_done:
            task.task_is_done = True
            task.save()

            return redirect("task_and_tags:home-page")

        else:
            task.task_is_done = False
            task.save()

        return redirect("task_and_tags:home-page")
