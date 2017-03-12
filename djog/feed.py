from django.contrib.syndication.views import Feed
from djog.models import Post

class PostsFeed(Feed):
    title = 'Sometimes I Write About Code'
    link = '/feed/'
    description = 'Sometimes I write about code. When I do, it usually ends up here.'

    def items(self):
        return Post.objects.published()

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_updatedate(self, item):
        return item.modified


