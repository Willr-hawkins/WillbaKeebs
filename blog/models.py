from django.db import models

class Category(models.Model):
    """ Allows blog posts to be categorised into what the post is about. """

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Post(models.Model):
    """ Hold a blog post entry. """

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

