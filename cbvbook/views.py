from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import BOOK
from.forms import BookCreateForm
from django.urls import reverse_lazy
# Create your views here.


class BookList(TemplateView):
    model=BOOK
    context={}
    template_name = "cbvbook/book_list.html"
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all
        self.context["books"]=books
        return render(request,self.template_name,self.context)

# class BookList(ListView):
    # context_object_name = "books"
    # can give intended names in the for in templates instead of object_list
    # template_name="cbvbook/books.html" to give intended html page\

# class BookView(DetailView):
#     model=BOOK
#     context_object_name = "book"
#     template_name = "cbvbook/bookdetail.html"

class BookView(TemplateView):
    model=BOOK
    template_name = "cbvbook/bookdetail.html"
    context={}
    def get(self, request, *args, **kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        book=self.model.objects.get(id=id)
        self.context["book"]=book
        return render(request,self.template_name,self.context)


# class BookCreate(CreateView):
#     model=BOOK
#     form_class=BookCreateForm
#     template_name = "cbvbook/bookcreate.html"
#     success_url = reverse_lazy("list")

class BookCreate(TemplateView):
    model=BOOK
    form_class=BookCreateForm
    template_name = "cbvbook/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        return render(request,self.template_name,form)

# class BookUpdate(UpdateView):
#     model=BOOK
#     form_class=BookCreateForm
#     template_name = "cbvbook/bookcreate.html"
#     success_url = reverse_lazy("list")

class BookUpdate(TemplateView):
    model=BOOK
    form_class=BookCreateForm
    template_name = "cbvbook/bookcreate.html"
    context={}
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        # book=self.model.objects.get(id=id)
        book = self.get_object(id)
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        book = self.get_object(id)
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("list")
        self.context["form"]=form
        return render(request,self.template_name,self.context)

# class BookDelete(DeleteView):
#     model = BOOK
#     success_url = reverse_lazy("list")

class BookDelete(TemplateView):
    model = BOOK
    def gt_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        book=self.gt_object(id)
        book.delete()
        return redirect("list")


