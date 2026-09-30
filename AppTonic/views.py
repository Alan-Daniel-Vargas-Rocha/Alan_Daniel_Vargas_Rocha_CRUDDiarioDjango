from django.shortcuts import render
from .models import *
from .forms import UserProfileForm
from django.urls import reverse_lazy

#GENERICS CREATEVIEW
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


class CreateProfile(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('profile_createuser')
    template_name = "form_createuser.html"
    
    
class DiarioListView(ListView):
    model = DiarioMiki
    template_name = "diario_list.html"
    context_object_name = "entradas"

    def get_queryset(self):
        return DiarioMiki.objects.filter(user=self.request.user)

class DiarioDetailView(DetailView):
    model = DiarioMiki
    template_name = "diario_detail.html"
    context_object_name = "entrada"
    
class DiarioUpdateView(UpdateView):
    model = DiarioMiki
    fields = ["titulo", "contenido"]
    template_name = "diario_form.html"
    success_url = reverse_lazy("diario_list")
    
class DiarioDeleteView(DeleteView):
    model = DiarioMiki
    template_name = "diario_confirm_delete.html"
    success_url = reverse_lazy("diario_list")
    

class DiarioCreateView(CreateView):
    model = DiarioMiki
    fields = ["titulo", "contenido"]
    template_name = "diario_form.html"
    success_url = reverse_lazy('profile_createuser')
    
    #Con esta función se asinga automaticamente el usuario logueado
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)