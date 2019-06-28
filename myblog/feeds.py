from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post

class LatestEntriesFeed(Feed):
    title = "Latest posts"
    link = "/latest/feed"
    description = "The most recent posts on your blog"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text