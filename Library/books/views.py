from django.shortcuts import render,render_to_response, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

from .forms import BookForm
from .models import Notes


class Home(TemplateView):
    template_name = 'home.html'




def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def books_list(request):
    books = Notes.objects.all()
    return render(request, 'notes_list.html', {
        'notes': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'upload_note.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Notes.objects.get(pk=pk)
        book.delete()
    return redirect('books_list')





class UploadBookView(CreateView):
    model = Notes
    form_class = BookForm
    success_url = reverse_lazy('notes_list')
    template_name = 'upload_note.html'
