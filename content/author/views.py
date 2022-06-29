from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class MyViews(CreateView):
    model= Post
    fields = ["writter",
            'text']

    template_name = "index.html"
    success_url= "list"

class MyList(ListView):
    model = Post
    template_name= "list.html"

class MyDetailView(DetailView):
    model = Post
    template_name= "detail.html"


class MyUpdateView(UpdateView):
    model = Post
    fields = [
        'text'
    ]
    template_name = "update.html"
    success_url = '/'


class MyDeleteView(DeleteView):
    model= Post
    template_name= "delete.html"
    success_url= '/'