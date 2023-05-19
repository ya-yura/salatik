import os

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from dotenv import load_dotenv

from core.models import Salad
from django.urls import reverse


load_dotenv()

SALADS_LIST_URL = 'salads-list'
SALADS_DETAIL_URL = 'salads-detail'
TEST_SALADS_NAME = 'Macaroni salad'
TEST_SALADS_BULK_CREATE_NAME = 'Macaroni salad bulk created'
TEST_SALADS_POST_REQUEST_NAME = 'Macaroni salad POST test'
TEST_SALADS_DESCRIPTION = 'Classic English salad'
TEST_SALADS_PATCH_NAME = 'Macaroni salad PATCH test'
TEST_SALADS_PATCH_DESCRIPTION = 'Classic English salad edited'
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')


class SaladTests(APITestCase):
    """Тесты эндпоинта /salads."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.salad = Salad.objects.create(
            name=TEST_SALADS_NAME,
            description=TEST_SALADS_DESCRIPTION,
        )
        Salad.objects.bulk_create([
            Salad(
                name=TEST_SALADS_BULK_CREATE_NAME,
                description=TEST_SALADS_DESCRIPTION,
            ) for i in range(4)
        ])

    def setUp(self):
        self.guest_client = APIClient()
        self.admin_client = APIClient()
        self.admin_client.login(
            username=ADMIN_USERNAME,
            password=ADMIN_PASSWORD
        )

    def test_admin_post_salads(self):
        """Тест POST запроса от админа к эндпоинту /salads."""

        response = self.admin_client.post(
            reverse(SALADS_LIST_URL),
            {
                'name': TEST_SALADS_POST_REQUEST_NAME,
                'description': TEST_SALADS_DESCRIPTION
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Salad.objects.count(), 6)
        self.assertEqual(Salad.objects.get(
            name=TEST_SALADS_POST_REQUEST_NAME,
            description=TEST_SALADS_DESCRIPTION).name,
            TEST_SALADS_POST_REQUEST_NAME
        )

    # def test_guest_cant_post_salads(self):  # пока нет пермишенов
    #     """Тест POST запроса от анонимного пользователя
    #     к эндпоинту /salads."""

    #     response = self.guest_client.post(
    #         reverse(SALADS_LIST_URL),
    #         {
    #             'name': TEST_SALADS_POST_REQUEST_NAME,
    #             'description': TEST_SALADS_DESCRIPTION
    #         },
    #         format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertEqual(Salad.objects.count(), 5)

    def test_salads_list(self):
        """Тест GET запроса от гостя к эндпоинту /salads
        на получение всех салатов."""

        response = self.guest_client.get(reverse(SALADS_LIST_URL))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_salads_detail(self):
        """Тест GET запроса от гостя к эндпоинту /salads
        на получение одного салата."""

        response = self.guest_client.get(
            reverse(SALADS_DETAIL_URL, kwargs={'pk': self.salad.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Salad.objects.get(pk=self.salad.pk).name,
            TEST_SALADS_NAME
        )

    def test_admin_can_delete_salads(self):
        """Тест DELETE запроса от админа к эндпоинту /salads."""

        salads_count = Salad.objects.count()
        response = self.admin_client.delete(
            reverse(SALADS_DETAIL_URL, kwargs={'pk': self.salad.pk})
        )
        self.assertEqual(Salad.objects.count(), salads_count-1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_guest_cant_delete_salads(self): # пока нет пермишенов
    #     """Тест DELETE запроса от анонимного пользователя
    #     к эндпоинту /salads."""

    #     salads_count = Salad.objects.count()
    #     response = self.guest_client.delete(
    #         reverse(SALADS_DETAIL_URL, kwargs={'pk': self.salad.pk})
    #     )
    #     self.assertEqual(Salad.objects.count(), salads_count)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_patch_salads(self):
        """Тест PATCH запроса от админа к эндпоинту /salads."""

        data = {
                'name': TEST_SALADS_PATCH_NAME,
                'description': TEST_SALADS_PATCH_DESCRIPTION
        }
        response = self.admin_client.patch(
            reverse(SALADS_DETAIL_URL, kwargs={'pk': self.salad.pk}),
            data=data,
            format='json'
        )
        self.assertTrue(Salad.objects.filter(
            name=TEST_SALADS_PATCH_NAME,
            description=TEST_SALADS_PATCH_DESCRIPTION).exists()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_guest_cant_patch_salads(self):  # пока нет пермишенов
    #     """Тест PATCH запроса от анонимного пользователя
    #     к эндпоинту /salads."""

    #     data = {
    #             'name': TEST_SALADS_PATCH_NAME,
    #             'description': TEST_SALADS_PATCH_DESCRIPTION
    #     }
    #     response = self.guest_client.patch(
    #         reverse(SALADS_DETAIL_URL, kwargs={'pk': self.salad.pk}),
    #         data=data,
    #         format='json'
    #     )
    #     self.assertFalse(Salad.objects.filter(
    #         name=TEST_SALADS_PATCH_NAME,
    #         description=TEST_SALADS_PATCH_DESCRIPTION).exists()
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
