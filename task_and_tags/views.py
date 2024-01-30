from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from task_and_tags.models import Tasks, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Tasks.objects.count()

    context = {
        "num_tasks": tasks,
    }

    return render(request, "task_and_tags/index.html", context=context)


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
