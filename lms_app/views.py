from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from .froms import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
           add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
           add_category.save()
          
        return redirect('index')
    context = {
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        'form':BookForm(),
        'formcat':CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),#لتحديد الاعداد 
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavailble':Book.objects.filter(status='availble').count(),
    }
    
    return render(request, 'pages/index.html' , context)

def update(request, id ):
    book_id = Book.objects.get(id=id)
    if request.method=='POST':
        book_save = BookForm(request.POST , request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
        return redirect('index')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form' :book_save, 
        }
    return render(request, 'pages/update.html', context)


    
def books(request):
    search = Book.objects.all()
    title = None 
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
            
    context = {
        'category':Category.objects.all(),
        'bookss':search,
    }
    return render(request, 'pages/books.html' , context)

# Book delete
def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)  
    if request.method == 'POST':
        book_delete.delete()
        return redirect('index')
    return render(request, 'pages/delete.html')

