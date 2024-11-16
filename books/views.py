from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm

# Read: Menampilkan daftar buku
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
    
# Create: Menambahkan buku baru
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# Update: Mengedit buku yang sudah ada
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

# Delete: Menghapus buku
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
