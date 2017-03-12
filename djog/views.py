from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Tag, Page

class PostIndex(generic.ListView):
    queryset = Post.objects.published()
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(generic.DetailView):
    queryset = Post.objects.published()
    template_name = 'post.html'

class TagIndex(generic.ListView):
    template_name = 'index.html'
    paginated_by = 6

    def get_queryset(self):
        slugs = self.kwargs['slug'].split('+')
        matched = []
        for slug in slugs:
            tag = Tag.objects.get(slug=slug)
            matched.extend(list(Post.objects.filter(tags=tag)))

        rematched = []
        for post in matched:
            if matched.count(post) == len(slugs) and post not in rematched:
                rematched.append(post)


        return rematched

    #def get_queryset(self):
    #    slug = self.kwargs['slug']
    #    tag = Tag.objects.get(slug=slug)
    #    results = Post.objects.filter(tags=tag)
    #    return results

class PageDetail(generic.DetailView):
    queryset = Page.objects.published()
    template_name = 'page.html'

class PageIndex(generic.ListView):
    queryset = Page.objects.published()
    template_name = 'index.html'
    paginate_by = 6
