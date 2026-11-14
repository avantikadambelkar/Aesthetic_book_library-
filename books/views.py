from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count, Avg
from .models import Book
from .forms import BookForm, AestheticRegisterForm, AestheticLoginForm


LITERARY_QUOTES = [
    {
        "quote": "I have always imagined that Paradise will be a kind of library.",
        "author": "Jorge Luis Borges",
        "work": "Selected Poems"
    },
    {
        "quote": "A room without books is like a body without a soul.",
        "author": "Marcus Tullius Cicero",
        "work": "Letters to Atticus"
    },
    {
        "quote": "There is no friend as loyal as a book.",
        "author": "Ernest Hemingway",
        "work": "On Writing"
    },
    {
        "quote": "She read books as one would breathe air, to fill up and live.",
        "author": "Annie Dillard",
        "work": "The Living"
    },
    {
        "quote": "We read to know we're not alone.",
        "author": "William Nicholson",
        "work": "Shadowlands"
    }
]


def landing_page(request):
    """Aesthetic Front Page / Landing Page."""
    featured_books = Book.objects.filter(is_featured=True)[:4]
    if not featured_books.exists():
        featured_books = Book.objects.all()[:4]

    latest_books = Book.objects.all()[:6]

    # Metrics
    total_books = Book.objects.count()
    completed_books = Book.objects.filter(reading_status='COMPLETED').count()
    reading_books = Book.objects.filter(reading_status='READING').count()
    genres_count = Book.objects.values('genre').distinct().count()

    context = {
        'featured_books': featured_books,
        'latest_books': latest_books,
        'total_books': total_books,
        'completed_books': completed_books,
        'reading_books': reading_books,
        'genres_count': genres_count,
        'quote_of_the_day': LITERARY_QUOTES[0],
    }
    return render(request, 'books/landing.html', context)


def library_view(request):
    """Aesthetic Library Catalogue with multi-factor search & filter."""
    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', 'ALL')
    genre_filter = request.GET.get('genre', 'ALL')
    sort_by = request.GET.get('sort', '-created_at')

    # If logged in, prioritize user books and public demo books
    if request.user.is_authenticated:
        books = Book.objects.filter(Q(user=request.user) | Q(user__isnull=True))
    else:
        books = Book.objects.all()

    # Search
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query) |
            Q(aesthetic_tag__icontains=query) |
            Q(favorite_quote__icontains=query)
        )

    # Status filter
    if status_filter and status_filter != 'ALL':
        books = books.filter(reading_status=status_filter)

    # Genre filter
    if genre_filter and genre_filter != 'ALL':
        books = books.filter(genre=genre_filter)

    # Sorting
    valid_sorts = {
        'newest': '-created_at',
        'oldest': 'created_at',
        'title': 'title',
        'author': 'author',
        'rating': '-rating',
        'pages': '-pages',
    }
    books = books.order_by(valid_sorts.get(sort_by, '-created_at'))

    # Counts for status pills
    base_qs = Book.objects.filter(Q(user=request.user) | Q(user__isnull=True)) if request.user.is_authenticated else Book.objects.all()
    status_counts = {
        'ALL': base_qs.count(),
        'READING': base_qs.filter(reading_status='READING').count(),
        'COMPLETED': base_qs.filter(reading_status='COMPLETED').count(),
        'WANT_TO_READ': base_qs.filter(reading_status='WANT_TO_READ').count(),
        'ON_HOLD': base_qs.filter(reading_status='ON_HOLD').count(),
    }

    all_genres = Book.GENRE_CHOICES

    context = {
        'books': books,
        'query': query,
        'current_status': status_filter,
        'current_genre': genre_filter,
        'current_sort': sort_by,
        'status_counts': status_counts,
        'all_genres': all_genres,
    }
    return render(request, 'books/library.html', context)


def book_detail(request, pk):
    """Magazine-style Aesthetic Book Detail View."""
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(genre=book.genre).exclude(pk=book.pk)[:3]
    return render(request, 'books/book_detail.html', {
        'book': book,
        'related_books': related_books,
    })


@login_required
def book_create(request):
    """Add a new tome to the sanctuary."""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, f'“{book.title}” has been gracefully cataloged in your library.')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {
        'form': form,
        'page_title': 'Inscribe a New Tome',
        'button_text': 'Add to Sanctuary',
        'action': 'create'
    })


@login_required
def book_update(request, pk):
    """Update details of an existing book."""
    book = get_object_or_404(Book, pk=pk)
    
    # Ownership guard (allows staff or original creator)
    if book.user and book.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to alter this tome.')
        return redirect('book_detail', pk=book.pk)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'“{book.title}” records have been successfully refined.')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'books/book_form.html', {
        'form': form,
        'book': book,
        'page_title': f'Refine “{book.title}”',
        'button_text': 'Save Enhancements',
        'action': 'edit'
    })


@login_required
def book_delete(request, pk):
    """Aesthetic deletion view."""
    book = get_object_or_404(Book, pk=pk)

    if book.user and book.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to remove this tome.')
        return redirect('book_detail', pk=book.pk)

    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.info(request, f'“{title}” has been respectfully removed from your library.')
        return redirect('library')

    return render(request, 'books/book_confirm_delete.html', {'book': book})


def register_view(request):
    """Aesthetic User Registration."""
    if request.user.is_authenticated:
        return redirect('library')

    if request.method == 'POST':
        form = AestheticRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to AuraFolio, {user.first_name or user.username}. Your sanctuary awaits.')
            return redirect('library')
        else:
            messages.error(request, 'Please correct the highlighted errors.')
    else:
        form = AestheticRegisterForm()

    return render(request, 'books/auth/register.html', {'form': form})


def login_view(request):
    """Aesthetic Split-Screen Login."""
    if request.user.is_authenticated:
        return redirect('library')

    if request.method == 'POST':
        form = AestheticLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}.')
            next_url = request.GET.get('next', 'library')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or passphrase. Please try again.')
    else:
        form = AestheticLoginForm()

    return render(request, 'books/auth/login.html', {'form': form})


def logout_view(request):
    """Graceful Logout."""
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been safely logged out. Until next time, gentle reader.')
    return redirect('landing')
