from django.shortcuts import render, get_object_or_404
from .models import Eco
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Page
from django.views.generic import DetailView
from django.urls import reverse_lazy


class EcoCreateView(LoginRequiredMixin, CreateView):
    model = Eco
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "blog/eco_form.html"
    success_url = reverse_lazy("pages")


class EcoUpdateView(LoginRequiredMixin, UpdateView):
    model = Eco
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "blog/eco_form.html"
    success_url = reverse_lazy("pages")
    


class EcoDeleteView(LoginRequiredMixin, DeleteView):
    model = Eco
    template_name = "blog/eco_confirm_delete.html"
    success_url = reverse_lazy("pages")
    
class PageListView(ListView):
    model = Page
    template_name = "blog/pages_list.html"
    
class PageDetailView(DetailView):
    model = Page
    template_name = "blog/page_detail.html"

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("pages")

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "blog/page_form.html"
    success_url = reverse_lazy("pages")

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "blog/page_confirm_delete.html"
    success_url = reverse_lazy("pages")



def inicio(request):
    return render(request, 'blog/inicio.html')

def about(request):
    return render(request, 'blog/about.html')

def pages(request):
    ecos = Eco.objects.all().order_by("-fecha")
    return render(request, "blog/pages.html", {"ecos": ecos})

def page_detail(request, slug):
    eco = get_object_or_404(Eco, slug=slug)
    return render(request, "blog/page_detail.html", {"eco": eco})

def about(request):
    return render(request, "blog/about.html")



class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "blog/page_form.html"
    success_url = "/pages/"

def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)