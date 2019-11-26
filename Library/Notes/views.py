from django.shortcuts import render,render_to_response, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

from .forms import BookForm
from .models import Book


class Home(TemplateView):
    template_name = 'home.html'

def logout_user(request):
    logout(request)
    return redirect("home")


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user: 
                user = User.objects.create_user(
                    form.cleaned_data['username'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                
                # Login the user
                login(request, user)
                
                # redirect to accounts page:
                return HttpResponseRedirect('')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})