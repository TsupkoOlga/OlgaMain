from django.db import models
from django.contrib.auth.models import User


#director = 'DI'
#admin = 'AD'
#cook = 'CO'
#cashier = 'CA'
#cleaner = 'CL'

#POSITIONS = [
   # (director, 'Директор'),
   # (admin, 'Администратор'),
    #(cook, 'Повар'),
    #(cashier, 'Кассир'),
    #(cleaner, 'Уборщик')
#]

class Author(models.Model):
    rating = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def update_rating(self):
        sum = 0

        sample = self.post_set.all()

        for i in sample:
            sum += i.rating

        sum *= 3



        sample = self.user.comment_set.all()

        for i in sample:
            sum += i.rating

        self.rating = sum
        self.save()






class Category(models.Model):
    name = models.CharField(max_length = 63, unique = True)


    #price = models.FloatField(default = 0.0)
    #composition = models.TextField(default="Состав не указан")


class Post(models.Model):
    is_article = models.BooleanField(default=False)
    title = models.CharField(max_length = 63)
    time_in = models.DateTimeField(auto_now_add = True)
    content = models.TextField(default = "Место для текста")
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.content) < 125:
            prw = self.content
        else:
            prw = self.content[:124] + '...'
        return prw

    #cost = models.FloatField(default = 0.0)
    #pickup = models.BooleanField(default = False)
    #complete = models.BooleanField(default = False)
    #staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    #products = models.ManyToManyField(Product, through='ProductOrder')

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    reply = models.CharField(max_length = 255)
    rating = models.IntegerField(default = 0)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

