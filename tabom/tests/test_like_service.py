from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_유저는_게시글을_좋아요_할_수_있다(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)
