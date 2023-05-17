from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Salad
from django.urls import reverse


SALADS_LIST_URL = 'salads-list'
SALADS_DETAIL_URL = 'salads-detail'
TEST_SALADS_NAME = 'Macaroni salad'
TEST_SALADS_BULK_CREATE_NAME = 'Macaroni salad bulk created'
TEST_SALADS_POST_REQUEST_NAME = 'Macaroni salad POST test'
TEST_SALADS_DESCRIPTION = 'Classic English salad'


class SaladTests(APITestCase):
    """Тесты Salads."""

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

    def test_post_salads(self):
        """Тест POST запроса к эндпоинту /salads."""

        response = self.client.post(
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

    def test_salads_list(self):
        """Тест GET запроса к эндпоинту /salads на получение 5 салатов."""

        response = self.client.get(reverse(SALADS_LIST_URL))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_salads_detail(self):
        """Тест GET запроса к эндпоинту /salads на получение одного салата."""

        response = self.client.get(reverse(
            SALADS_DETAIL_URL,
            kwargs={'pk': self.salad.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Salad.objects.get(pk=self.salad.pk).name,
            TEST_SALADS_NAME
        )

    def test_delete_salads(self):
        """Тест DELETE запроса к эндпоинту /salads."""

        salads_count = Salad.objects.count()
        self.client.delete(reverse(
            SALADS_DETAIL_URL,
            kwargs={'pk': self.salad.pk})
        )
        self.assertEqual(Salad.objects.count(), salads_count-1)
