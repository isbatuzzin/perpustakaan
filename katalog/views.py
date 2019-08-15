from django.shortcuts import render

# Create your views here.
from katalog.models import Book, Author, BookInstance, Genre, Language
from django.views import generic


def index(request):
    # Hitung data dari objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.count()

    # Buku Tersedia (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' selalu terdefinisi sebagai default
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        return Book.objects.all()[:5]

class BookDetail_View(generic.DetailView):
    model = Book
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary)
        except Book.DoesNoExist:
            raise Http404('Book does not exist')
        return render(request,'katalog/book_detail.html',context={'book': book})

class AuthorListView(generic.ListView):
    model = Author
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        return Author.objects.all()[:5]

class AuthorDetailView(generic.DetailView):
    model = Author
    def author_detail_view(request, primary_key):
        try:
            author = Author.objects.get(pk=primary)
        except Author.DoesNoExist:
            raise Http404('Book does not exist')
        return render(request,'katalog/author_detail.html',context={'author': author})
