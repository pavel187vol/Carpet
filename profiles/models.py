from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class AbstractProfile(models.Model):
    user = models.ForeignKey(User,
                             related_name='%(class)s_related',
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = PhoneNumberField(blank=True, unique=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    # feedback = models.ForeignKey('FeedBack',
    #                              related_name='%(class)s_related',
    #                              on_delete=models.SET_NULL,
    #                              blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}. {}".format(self.first_name,
                               self.last_name)

class Customer(AbstractProfile):
    order = models.ForeignKey('Order',
                              related_name='customers',
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)

class Executer(AbstractProfile):
    description = models.ForeignKey('DescriptionExecuter',
                                    related_name='executer',
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True)
    work = models.ForeignKey('Order',
                             related_name='executers',
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)

class Order(models.Model):
    description_order = models.ForeignKey('DescriptionOrder',
                                          related_name='orders',
                                          on_delete=models.SET_NULL,
                                          blank=True,
                                          null=True)
    customer = models.ForeignKey('Customer',
                                 related_name='customers',
                                 on_delete=models.CASCADE)
    executor = models.ForeignKey('Executer',
                                 related_name='executors',
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    condition = models.BooleanField(default=False)
    condition_success = models.BooleanField(default=False)
    moderation = models.BooleanField(default=False)

class DescriptionOrder(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='orders/%Y/%m/%d',
                              blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type_work = models.ForeignKey('TypeWork',
                                  related_name='descriptionss',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)
    order = models.ForeignKey('Order',
                              related_name='orders',
                              on_delete=models.CASCADE)

class TypeWork(models.Model):
    title = models.CharField(max_length=200)

class FeedBack(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.title

class DescriptionExecuter(models.Model):
    pass
