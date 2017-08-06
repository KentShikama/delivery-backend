import datetime

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.db import models


class Announcement(models.Model):
    message = models.CharField(max_length=1024)
    schools = models.ManyToManyField("School", blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    post_at = models.DateTimeField()

class Categories(models.Model):
    CATEGORY_TYPES = ((1, u'Food'),(2,u'Nonfood'))

    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='photos/')
    type = models.SmallIntegerField(choices=CATEGORY_TYPES)

class Profile(models.Model):
    user = models.OneToOneField(User)
    push_id = models.CharField(max_length=128)
    school = models.ForeignKey("School")
    name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars/')
    phone = models.CharField(max_length=128)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    last_login_date = models.DateTimeField(default=datetime.datetime.now)
    is_privacy = models.BooleanField(default=False)
    is_eula = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    referral = models.ForeignKey('self')
    orders = models.ManyToManyField("Order")
    is_driver = models.BooleanField(default=False)
    reviews = models.ManyToManyField("Review", blank=True)
    schedule = models.CharField(max_length=2048,validators=[validate_comma_separated_integer_list])

class Order(models.Model):
    ORDER_STATUS = ((1, u'pending acceptance'),(2, u'accepted'),(3, u'pending payment approval'),(4, u'completed'),(5, u'cancelled'))
    created_at = models.DateTimeField(default=datetime.datetime.now)
    status = models.SmallIntegerField(choices=ORDER_STATUS)
    store = models.ForeignKey("Store")
    review = models.ForeignKey("Review", null=True)
    gmv = models.FloatField()
    driver_cut = models.FloatField()
    management_cut = models.FloatField()
    tips = models.FloatField()
    total_cost = models.FloatField()
    driver_profit = models.FloatField() # drivers_cut + tips - 0.3 - 0.029*total_cost
    driver_payout = models.FloatField() # driver_profit + gmv
    promo_code = models.ForeignKey("Promo")
    item_quantities = models.ManyToManyField("ItemQuantity", blank=True)

class ItemQuantity(models.Model):
    amount = models.IntegerField()
    item = models.ForeignKey("Item")

class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    addons = models.ManyToManyField('self', null=True)
    store = models.ForeignKey("Store")

class Promo(models.Model):
    code = models.CharField(max_length=128)
    type = models.CharField(max_length=128)

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    comment = models.CharField(max_length=1024)
    created_at = models.DateTimeField(default=datetime.datetime.now)

class Store(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='store_images/')
    schools = models.ManyToManyField("School", blank=True)
    hours_of_operation = models.CharField(max_length=2048,validators=[validate_comma_separated_integer_list])
    is_partnered = models.BooleanField(default=False)

class Message(models.Model):
    sender = models.ForeignKey("Profile", related_name="message_sender")
    receiver = models.ForeignKey("Profile", related_name="message_receiver")
    content = models.CharField(max_length=512)

class School(models.Model):
    name = models.CharField(max_length=128)
    hours_of_operation = models.CharField(max_length=2048,validators=[validate_comma_separated_integer_list])
