from django.db import models
from django.utils import timezone
from docutils.core import publish_parts

from django.core.urlresolvers import reverse


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Tag(models.Model):
    tag = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.slug


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    text = models.TextField()
    html = models.TextField(editable=False, blank=True, null=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now())
    modified = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

    def save(self):
        self.html = publish_parts(self.text, writer_name='html4css1',
                                  settings_overrides={'initial_header_level': 3, 'file_insertion_enabled': 0,})['body']
        super(Post, self).save()

    class Meta:
        ordering = ["-created"]


class Page(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    text = models.TextField()
    html = models.TextField(editable=False, blank=True, null=True)
    publish = models.BooleanField(default=False)

    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})

    def save(self):
        self.html = publish_parts(self.text, writer_name='html4css1',
                                  settings_overrides={'initial_header_level': 3, 'file_insertion_enabled': 0,})['body']
        super(Page, self).save()

    def __str__(self):
        return self.slug
