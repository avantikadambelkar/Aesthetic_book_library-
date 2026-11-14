from django.core.management.base import BaseCommand
from books.models import Book


SEEDED_BOOKS = [
    {
        "title": "The Secret History",
        "author": "Donna Tartt",
        "genre": "Dark Academia",
        "reading_status": "COMPLETED",
        "rating": 5,
        "publication_year": 1992,
        "pages": 559,
        "language": "English",
        "isbn": "978-1400031702",
        "aesthetic_tag": "Autumn Academia • Greek Tragedy",
        "cover_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=700&q=80",
        "description": "Under the influence of an eccentric classics professor, a group of clever, eccentric misfits at an elite New England college discover a way of thinking and living that is a world away from the humdrum existence of their contemporaries.",
        "favorite_quote": "Beauty is terror. Whatever we call beautiful, we quiver before it.",
        "is_featured": True,
    },
    {
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "genre": "Philosophy",
        "reading_status": "READING",
        "rating": 5,
        "publication_year": 180,
        "pages": 256,
        "language": "English / Ancient Greek",
        "isbn": "978-0140449334",
        "aesthetic_tag": "Stoic Wisdom • Timeless Reflections",
        "cover_url": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80",
        "description": "The private journal of the Roman emperor Marcus Aurelius, offering enduring personal insights into virtue, resilience, inner peace, and human nature amidst duty and adversity.",
        "favorite_quote": "You have power over your mind - not outside events. Realize this, and you will find strength.",
        "is_featured": True,
    },
    {
        "title": "Kafka on the Shore",
        "author": "Haruki Murakami",
        "genre": "Fiction",
        "reading_status": "COMPLETED",
        "rating": 4,
        "publication_year": 2002,
        "pages": 505,
        "language": "English / Japanese",
        "isbn": "978-1400079278",
        "aesthetic_tag": "Magical Realism • Nostalgia & Rain",
        "cover_url": "https://images.unsplash.com/photo-1532012164546-f432f2e3777f?auto=format&fit=crop&w=700&q=80",
        "description": "A metaphysical journey intertwining two characters: Kafka Tamura, a teenage runaway haunted by a dark prophecy, and Nakata, an aging tracker of lost cats.",
        "favorite_quote": "Memories warm you up from the inside. But they also tear you apart.",
        "is_featured": True,
    },
    {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": "Classics",
        "reading_status": "COMPLETED",
        "rating": 5,
        "publication_year": 1890,
        "pages": 272,
        "language": "English",
        "isbn": "978-0141439570",
        "aesthetic_tag": "Victorian Gothic • Aestheticism",
        "cover_url": "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=700&q=80",
        "description": "A story of aestheticism, moral decay, and beauty's dark temptation, as Dorian Gray trades his soul for eternal youth while his hidden portrait bears the marks of his sins.",
        "favorite_quote": "Behind every exquisite thing that existed, there was something tragic.",
        "is_featured": True,
    },
    {
        "title": "Letters to a Young Poet",
        "author": "Rainer Maria Rilke",
        "genre": "Poetry",
        "reading_status": "WANT_TO_READ",
        "rating": 4,
        "publication_year": 1929,
        "pages": 128,
        "language": "English / German",
        "isbn": "978-0393343167",
        "aesthetic_tag": "Solitude & Creation • Intimate Prose",
        "cover_url": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=700&q=80",
        "description": "Ten intimate letters offering profound guidance on solitude, love, creative struggle, and the delicate art of living authentically.",
        "favorite_quote": "Be patient toward all that is unsolved in your heart and try to love the questions themselves.",
        "is_featured": False,
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Sci-Fi & Fantasy",
        "reading_status": "READING",
        "rating": 5,
        "publication_year": 1965,
        "pages": 688,
        "language": "English",
        "isbn": "978-0441172719",
        "aesthetic_tag": "Desert Epic • Ecology & Myth",
        "cover_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=700&q=80",
        "description": "Set on the desert planet Arrakis, Dune is the story of Paul Atreides as he navigates political betrayal, prophetic visions, and the rare planetary resource known as the spice melange.",
        "favorite_quote": "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration.",
        "is_featured": False,
    },
    {
        "title": "The Design of Everyday Things",
        "author": "Don Norman",
        "genre": "Art & Design",
        "reading_status": "COMPLETED",
        "rating": 4,
        "publication_year": 2013,
        "pages": 368,
        "language": "English",
        "isbn": "978-0465050659",
        "aesthetic_tag": "Cognitive Elegance • Design Theory",
        "cover_url": "https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&w=700&q=80",
        "description": "A foundational masterwork on human-centered design, cognitive ergonomics, and the quiet psychology behind everyday interactions.",
        "favorite_quote": "Good design is actually a lot harder to notice than poor design, in part because good designs fit our needs so well that the design is invisible.",
        "is_featured": False,
    },
    {
        "title": "Quiet: The Power of Introverts",
        "author": "Susan Cain",
        "genre": "Psychology",
        "reading_status": "ON_HOLD",
        "rating": 4,
        "publication_year": 2012,
        "pages": 352,
        "language": "English",
        "isbn": "978-0307352156",
        "aesthetic_tag": "Introspection • Quiet Strength",
        "cover_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=700&q=80",
        "description": "An evocative examination of how modern society undervalues introverts, and how quiet contemplation fuels deep creativity, leadership, and empathy.",
        "favorite_quote": "There's zero correlation between being the best talker and having the best ideas.",
        "is_featured": False,
    }
]


class Command(BaseCommand):
    help = 'Seeds the database with curated aesthetic books.'

    def handle(self, *args, **options):
        created_count = 0
        for data in SEEDED_BOOKS:
            book, created = Book.objects.get_or_create(
                title=data['title'],
                author=data['author'],
                defaults=data
            )
            if created:
                created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {created_count} aesthetic books!"))

