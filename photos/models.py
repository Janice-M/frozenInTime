from django.db import models

# Create your models here bruvaaah

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads')
    description = models.TextField()
    image_location = models.ForeignKey('Location', default="image_location",on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey('Category',on_delete=models.DO_NOTHING)

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
    def get_image_by_categ(cls,categ):
        images = cls.objects.filter(image_category__categ__contains=categ)
        return images

    @classmethod
    def get_image_by_location(cls,pahali):
        images = cls.objects.filter(image_location__pahali__contains=pahali).all()
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

    pahali = models.CharField(max_length=255, choices=locations)


    class Meta:
        verbose_name_plural = 'Location'

    def __str__(self):
        return f"{self.pahali}"




    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_pahali(cls, id, new_pahali):
        cls.objects.filter(id=id).update(pahali=new_pahali)


class Category(models.Model):
    categories = (
        ('Fandom Stuff','Fandom stuff'),
        ('Pets','Pets'),
        ('Outfits','Outfits'),
        ('Memories','Memories')
    )

    categ = models.CharField(max_length = 255, choices = categories)


    class Meta:
        verbose_name_plural = 'Category'


    def __str__(self):
        return f"{self.categ}"




    def save_category(self):
        self.save()


    def delete_category(self):
        self.delete()

    @classmethod
    def update_categ(cls, id, new_categ):
        cls.objects.filter(id=id).update(categ=new_categ)