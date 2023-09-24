from django.test import TestCase


# Create your tests here.
class Test(TestCase):
    def setUp(self) -> None:
        print('setup')

    def test_func(self):
        print(123)
