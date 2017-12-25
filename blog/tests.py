import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from .models import Post


class PostModelTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() returns False for posts whose date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(date=time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        """
        was_published_recently() returns False for posts whose date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_post = Post(date=time)
        self.assertIs(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
        was_published_recently() returns True for posts whose date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(house=23, minutes=59, seconds=59)
        recent_post = Post(date=time)
        self.assertIs(recent_post.was_published_recently(), True)


def create_post(title, days):
    """
    Create a post with the given 'title' and published the given number of 'days' offset to now (negative for posts published in the past, positive for posts that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(title=title, date=time)


class PostIndexViewTests(TestCase):
    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assetContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_post_list'], [])
    
    def test_past_post(self):
        """
        Posts with a date in the past are displayed on the index page.
        """
        create_post(title="Past post.", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<Post: Past post.>']
        )

    def test_future_post(self):
        """
        Posts with a date in the future aren't displayed on the index page.
        """
        create_post(title="Future post.", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_future_post_and_past_post(self):
        """
        Even if both past and future posts exist, only past posts are displayed.
        """
        create_post(title="Past post.", days=-30)
        create_post(title="Future post.", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response(context.['latest_post_list'],
            ['<Post: Past post.>']
        )

    def test_two_past_posts(self):
        """
        The posts index page may display multiple posts.
        """
        create_post(title="Past post 1.", days=-30)
        create_post(title="Past post 2.", days=-5)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<Post: Past post 2.>', '<Post: Past post 1.>']
        )


class PostDetailViewTests(TestCase):
    def test_future_post(self):
        """
        The detail view of a post with a date in the future returns a 404 not found.
        """
        future_post = create_post(title='Future post.', days=5)
        url = reverse('blog:detail', args=future_post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_post(self):
        """
        The detail view of a post with a date in the past displays the post's title.
        """
        post_post = create_post(title='Past Post.', days=-5)
        url = reverse('blog:detail', args=(past_post.id,))
        response = self.client.get(url)
        self.assertContains(response, past_post, title)

