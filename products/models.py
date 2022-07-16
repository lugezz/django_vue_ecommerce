from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def get_image(self):
        if self.image:
            # TODO: Make it more dinamic
            return 'http://localhost:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        # TODO: Change it, it's making unpload/upload
        if self.thumbnail:
            return 'http://localhost:8000' + self.thumbnail.url
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return 'http://localhost' + self.thumbnail.url
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumbs_io = BytesIO()
        img.save(thumbs_io, format='JPEG', quality=85)

        thumbnail = File(thumbs_io, name=image.name)

        return thumbnail
