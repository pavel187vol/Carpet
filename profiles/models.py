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
    feedback = models.ForeignKey(FeedBack,
                                 related_name='%(class)s_related',
                                 on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}. {}".format(self.first_name,
        self.last_name)

class Customer(AbstractProfile):
    order = models.ForeignKey(Order,
                              related_name='customer',
                              on_delete=models.SET_NULL)

class Executer(AbstractProfile):
    description = models.ForeignKey(DescriptionExecuter,
                                    related_name='executer',
                                    on_delete=models.SET_NULL)
    work = models.ForeignKey(Order,
                             related_name='executer',
                             on_delete=models.SET_NULL)

class Order(models.Model):
    description_order = models.ForeignKey(DescriptionOrder,
                                          related_name='order',
                                          on_delete=models.SET_NULL)
    
