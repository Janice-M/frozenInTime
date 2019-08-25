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
class Location(models.Model):
    locations = (
        ('Nairobi','Nairobi'),
        ('Mombasa','Mombasa'),
        ('Naivasha','Naivasha'),
        ('Lagos','Lagos'),
        ('Maldives','Maldives'),
        ('Paris','Paris'),
        ('Cape Town','Cape Town'),
        ('London','London'),
        ('Alexandria','Alexandria')
    )

    loc = models.CharField(max_length=255, choices=locations)


    class Meta:
        verbose_name_plural = 'Location'

    def __str__(self):
        return f"{self.loc}"




    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_loc(cls, id, new_loc):
        cls.objects.filter(id=id).update(loc=new_loc)


class Category(models.Model):
    categories = (
        ('Food','Food'),
        ('Cars','Cars'),
        ('Shoes','Shoes'),
        ('Quotes','Quotes')
    )

    cat = models.CharField(max_length = 255, choices = categories)


    class Meta:
        verbose_name_plural = 'Category'


    def __str__(self):
        return f"{self.cat}"




    def save_category(self):
        self.save()


    def delete_category(self):
        self.delete()

    @classmethod
    def update_cat(cls, id, new_cat):
        cls.objects.filter(id=id).update(cat=new_cat)