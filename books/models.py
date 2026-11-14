from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    GENRE_CHOICES = [
        ('Classics', 'Classics & Antiquity'),
        ('Dark Academia', 'Dark Academia & Mystery'),
        ('Philosophy', 'Philosophy & Thought'),
        ('Poetry', 'Poetry & Prose'),
        ('Fiction', 'Literary Fiction'),
        ('Sci-Fi & Fantasy', 'Sci-Fi & Speculative Fiction'),
        ('Art & Design', 'Art, Architecture & Aesthetics'),
        ('Psychology', 'Psychology & Human Nature'),
        ('Memoir', 'Memoir & Biography'),
        ('Non-Fiction', 'Essays & Non-Fiction'),
    ]

    STATUS_CHOICES = [
        ('WANT_TO_READ', 'Want to Read'),
        ('READING', 'Currently Reading'),
        ('COMPLETED', 'Finished Reading'),
        ('ON_HOLD', 'On Hold'),
    ]

    RATING_CHOICES = [
        (1, '★ 1 - Modest'),
        (2, '★★ 2 - Fair'),
        (3, '★★★ 3 - Captivating'),
        (4, '★★★★ 4 - Splendid'),
        (5, '★★★★★ 5 - Masterpiece'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='Fiction')
    description = models.TextField(
        blank=True,
        help_text="A brief reflection, synopsis, or your personal thoughts."
    )
    favorite_quote = models.TextField(
        blank=True,
        help_text="An inspiring or evocative quote from this tome."
    )
    isbn = models.CharField(max_length=20, blank=True, verbose_name="ISBN")
    publication_year = models.PositiveIntegerField(null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True, verbose_name="Total Pages")
    language = models.CharField(max_length=50, default="English")
    
    cover_image = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True,
        help_text="Upload a local cover image."
    )
    cover_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Or paste a high-resolution web image URL."
    )
    
    reading_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='WANT_TO_READ'
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        null=True,
        blank=True
    )
    aesthetic_tag = models.CharField(
        max_length=100,
        blank=True,
        help_text="E.g., 'Rainy Autumn Reads', 'Mindful Awakening', 'Midnight Musings'"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Feature this title on the front landing showcase."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.author}"

    @property
    def cover(self):
        if self.cover_image:
            return self.cover_image.url
        if self.cover_url:
            return self.cover_url
        # Fallback aesthetic unplash placeholder
        return "https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&w=600&q=80"

    @property
    def filled_stars(self):
        return range(self.rating) if self.rating else range(0)

    @property
    def empty_stars(self):
        return range(5 - self.rating) if self.rating else range(5)

    @property
    def status_badge_class(self):
        mapping = {
            'WANT_TO_READ': 'badge-want',
            'READING': 'badge-reading',
            'COMPLETED': 'badge-completed',
            'ON_HOLD': 'badge-hold',
        }
        return mapping.get(self.reading_status, 'badge-want')
