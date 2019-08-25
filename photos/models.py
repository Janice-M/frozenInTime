from django.db import models

# Create your models here bruvaaah

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads')
    description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(pic=value)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def get_image_by_cat(cls,cat):
        images = cls.objects.filter(image_category__cat__contains=cat)
        return images

    @classmethod
    def get_image_by_location(cls,loc):
        images = cls.objects.filter(image_location__loc__contains=loc).all()
        return images

    def __str__(self):
        return self.name
