from posts import factory
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class PostsTestCase(APITestCase):

    def setUp(self):
        self.user = factory.UserFactory.create()
        self.client = APIClient()

        # post
        self.post = factory.PostFactory.create(
            title='Django REST',
            author=self.user,
        )

        # content
        self.content = factory.ContentFactory.create(
            type='h1',
            value='Django rest framework',
            post=self.post
        )

    def test_post_create(self):
        payload = {
            "title": "Framework",
            "author": self.user.id,
            "content": [
                {
                    "type": "h1",
                    "value": "Django models"
                },
                {
                    "type": "p",
                    "value": "Django views are ..."
                },
                {
                    "type": "p",
                    "value": "Django permissions are ..."
                }
            ]
        }

        response = self.client.post('/posts/', data=payload, format='json')
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get('title'), 'Framework')
        self.assertEqual(len(data.get('content')), 3)

    def test_post_list(self):
        response = self.client.get(path='/posts/', format='json')
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)

    def test_post_detail(self):
        response = self.client.get(path=f'/posts/{self.post.id}/', format='json')
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), 'Django REST')
        self.assertEqual(data.get('content')[0].get('type'), 'h1')
        self.assertEqual(data.get('content')[0].get('value'), 'Django rest framework')
