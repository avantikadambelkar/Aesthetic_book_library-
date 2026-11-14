from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Book


class AuraFolioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testcurator',
            password='testpassword123',
            email='test@curator.com',
            first_name='Clara'
        )
        self.book = Book.objects.create(
            title='The Secret History',
            author='Donna Tartt',
            genre='Dark Academia',
            reading_status='COMPLETED',
            rating=5,
            publication_year=1992,
            pages=559,
            user=self.user,
            is_featured=True,
            favorite_quote='Beauty is terror.'
        )

    def test_landing_page(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AuraFolio')
        self.assertContains(response, 'The Secret History')

    def test_library_page(self):
        response = self.client.get(reverse('library'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Sanctuary Library')
        self.assertContains(response, 'Donna Tartt')

    def test_library_search_and_filter(self):
        # Search match
        res_search = self.client.get(reverse('library') + '?q=Donna')
        self.assertEqual(res_search.status_code, 200)
        self.assertContains(res_search, 'The Secret History')

        # Search no match
        res_empty = self.client.get(reverse('library') + '?q=NonExistentTome123')
        self.assertEqual(res_empty.status_code, 200)
        self.assertContains(res_empty, 'No tomes found')

        # Status filter
        res_status = self.client.get(reverse('library') + '?status=COMPLETED')
        self.assertEqual(res_status.status_code, 200)
        self.assertContains(res_status, 'The Secret History')

    def test_book_detail_page(self):
        response = self.client.get(reverse('book_detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Secret History')
        self.assertContains(response, 'Donna Tartt')
        self.assertContains(response, 'Beauty is terror.')

    def test_auth_login_and_logout(self):
        # Test login view GET
        login_page = self.client.get(reverse('login'))
        self.assertEqual(login_page.status_code, 200)

        # Test login POST
        login_post = self.client.post(reverse('login'), {
            'username': 'testcurator',
            'password': 'testpassword123'
        }, follow=True)
        self.assertEqual(login_post.status_code, 200)
        self.assertTrue(login_post.context['user'].is_authenticated)

        # Test logout
        logout_res = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(logout_res.status_code, 200)
        self.assertFalse(logout_res.context['user'].is_authenticated)

    def test_book_crud_lifecycle(self):
        # Must be logged in to create
        self.client.login(username='testcurator', password='testpassword123')

        # Create book
        create_res = self.client.post(reverse('book_create'), {
            'title': 'The Picture of Dorian Gray',
            'author': 'Oscar Wilde',
            'genre': 'Classics',
            'reading_status': 'READING',
            'rating': 5,
            'pages': 272,
            'language': 'English'
        }, follow=True)
        self.assertEqual(create_res.status_code, 200)
        new_book = Book.objects.get(title='The Picture of Dorian Gray')
        self.assertEqual(new_book.author, 'Oscar Wilde')
        self.assertEqual(new_book.user, self.user)

        # Update book
        update_res = self.client.post(reverse('book_update', kwargs={'pk': new_book.pk}), {
            'title': 'The Picture of Dorian Gray (Illustrated)',
            'author': 'Oscar Wilde',
            'genre': 'Classics',
            'reading_status': 'COMPLETED',
            'rating': 5,
            'pages': 300,
            'language': 'English'
        }, follow=True)
        self.assertEqual(update_res.status_code, 200)
        new_book.refresh_from_db()
        self.assertEqual(new_book.title, 'The Picture of Dorian Gray (Illustrated)')
        self.assertEqual(new_book.reading_status, 'COMPLETED')

        # Delete book
        delete_res = self.client.post(reverse('book_delete', kwargs={'pk': new_book.pk}), follow=True)
        self.assertEqual(delete_res.status_code, 200)
        self.assertFalse(Book.objects.filter(pk=new_book.pk).exists())
