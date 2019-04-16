from django.test import TestCase
from django.test import Client
from django.shortcuts import reverse

class HelloTest(TestCase):
    def test_index_get(self):
        c = Client()
        response = c.get(reverse('hello_index'))
        self.assertContains(response, 'form')

    def test_hello_with_name(self):
        c = Client()
        response = c.post(reverse('hello_index'),
            dict(name='budi', pilihan='hello'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('Location', ''),
                '{}?name={}'.format(reverse('hello_hello'), 'budi'))

        response = c.get('{}?name={}'.format(reverse('hello_hello'), 'budi'))
        self.assertContains(response, 'Hello budi')

    def test_hello_with_empty_name(self):
        c = Client()
        response = c.post(reverse('hello_index'),
            dict(name='', pilihan='hello'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('Location', ''),
                '{}?name={}'.format(reverse('hello_hello'), ''))

        response = c.get('{}?name={}'.format(reverse('hello_hello'), ''))
        self.assertContains(response, 'Hello World')

    def test_hello_without_name(self):
        c = Client()
        response = c.post(reverse('hello_index'),
            dict(pilihan='hello'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('Location', ''),
                '{}?name={}'.format(reverse('hello_hello'), ''))

        response = c.get('{}'.format(reverse('hello_hello')))
        self.assertContains(response, 'Hello World')

    def test_bye_with_name(self):
        pass

    def test_bye_with_empty_name(self):
        pass

    def test_bye_without_name(self):
        pass
