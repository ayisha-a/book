from django.shortcuts import render,redirect
from .forms import BookCreateForm,BookUpdateForm
from .models import Book

# Create your views here.
def home(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book/index.html",context)


#book/create
    #1)get:html page for creating oook,list
    #2)post:create book
def bookcreate(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    template_name="book/createbook.html"
    books=Book.objects.all()
    context["books"]=books
    if request.method=="POST":
        form=BookCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("create")
        else:
            context["form"]=form
            return render(request, template_name, context)
    return render(request,template_name,context)

#book/view/1
    #get:return buk with corress id
def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookview.html",context)

#book/view/1
    #get:return buk with corress id
    #post:update book
def update_book(request,id):
    book = Book.objects.get(id=id)
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")
        else:
            form=BookUpdateForm(request.POST, instance=book)
            context["form"]=form
            return render(request, "book/bookedit.html", context)
    return render(request,"book/bookedit.html",context)

#book/delete/1
    #get:delete buk with corres id
def delete_book(request,id):
    Book.objects.get(id=id).delete()
    return redirect("create")