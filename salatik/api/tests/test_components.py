import os

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from dotenv import load_dotenv

from core.models import Component, Ingredient, Salad, IngredientType
from django.urls import reverse


load_dotenv()

COMPONENTS_LIST_URL = 'components-list'
COMPONENTS_DETAIL_URL = 'components-detail'
TEST_SALADS_NAME = 'Macaroni salad'
TEST_SALADS_BULK_CREATE_NAME = 'Macaroni salad bulk created'
TEST_SALADS_DESCRIPTION = 'Classic English salad'
TEST_INGREDIENT_NAME = 'tomatoes'
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
TEST_TYPE_NAME = 'vegetable'
TEST_NUMBER = 1234
TEST_SALADS_PATCH_NAME = 'Macaroni salad PATCH test'
TEST_SALADS_DESCRIPTION = 'Classic English salad'


class CompontentsTests(APITestCase):
    """Тесты эндпоинта /components."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.component = Component.objects.create(
            salad=Salad.objects.create(
                name=TEST_SALADS_NAME,
                description=TEST_SALADS_DESCRIPTION),
            weight=TEST_NUMBER,
            order=TEST_NUMBER,
            ingredient=Ingredient.objects.create(
                name=TEST_INGREDIENT_NAME,
                type=IngredientType.objects.create(name=TEST_TYPE_NAME),
                protein=TEST_NUMBER,
                fat=TEST_NUMBER,
                carbohydrates=TEST_NUMBER,
                energy=TEST_NUMBER,
                price_per_unit=TEST_NUMBER),
        )
        Component.objects.bulk_create([
            Component(
                salad=Salad.objects.create(
                    name=TEST_SALADS_BULK_CREATE_NAME,
                    description=TEST_SALADS_DESCRIPTION),
                weight=TEST_NUMBER,
                order=TEST_NUMBER,
                ingredient=Ingredient.objects.create(
                    name=TEST_INGREDIENT_NAME,
                    type=IngredientType.objects.create(name=TEST_TYPE_NAME),
                    protein=TEST_NUMBER,
                    fat=TEST_NUMBER,
                    carbohydrates=TEST_NUMBER,
                    energy=TEST_NUMBER,
                    price_per_unit=TEST_NUMBER),
            ) for i in range(4)
        ])

    def setUp(self):
        self.guest_client = APIClient()
        self.admin_client = APIClient()
        self.admin_client.login(
            username=ADMIN_USERNAME,
            password=ADMIN_PASSWORD
        )

    def test_components_list(self):
        """Тест GET запроса от гостя к эндпоинту /components
        на получение всех компонентов салатов."""

        response = self.guest_client.get(reverse(COMPONENTS_LIST_URL))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_components_detail(self):
        """Тест GET запроса от гостя к эндпоинту /components
        на получение одного компонента."""

        response = self.guest_client.get(
            reverse(COMPONENTS_DETAIL_URL, kwargs={'pk': self.component.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Component.objects.get(pk=self.component.pk).ingredient.name,
            TEST_INGREDIENT_NAME
        )

    def test_admin_can_delete_components(self):
        """Тест DELETE запроса от админа к эндпоинту /components."""

        components_count = Component.objects.count()
        response = self.admin_client.delete(
            reverse(COMPONENTS_DETAIL_URL, kwargs={'pk': self.component.pk})
        )
        self.assertEqual(Component.objects.count(), components_count-1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_guest_cant_delete_components(self):  # пока нет пермишенов
    #     """Тест DELETE запроса от анонимного пользователя
    #     к эндпоинту /components."""

    #     components_count = Component.objects.count()
    #     response = self.guest_client.delete(
    #         reverse(COMPONENTS_DETAIL_URL, kwargs={'pk': self.salad.pk})
    #     )
    #     self.assertEqual(Component.objects.count(), components_count)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_admin_post_components(self):
    #     """Тест POST запроса от админа к эндпоинту /components."""
