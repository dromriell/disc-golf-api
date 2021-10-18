from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(username, email, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    STATE_CHOICES = [ 
        ('AL', 'Alabama'), 
        ('AK', 'Alaska'), 
        ('AZ', 'Arizona'), 
        ('AR', 'Arkansas'),  
        ('CA', 'California'), 
        ('CO', 'Colorado'), 
        ('CT', 'Connecticut'), 
        ('DE', 'Delaware'), 
        ('DC', 'District of Columbia'), 
        ('FL', 'Florida'), 
        ('GA', 'Georgia'), 
        ('HI', 'Hawaii'), 
        ('ID', 'Idaho'), 
        ('IL', 'Illinois'), 
        ('IN', 'Indiana'), 
        ('IA', 'Iowa'), 
        ('KS', 'Kansas'), 
        ('KY', 'Kentucky'), 
        ('LA', 'Louisiana'), 
        ('ME', 'Maine'), 
        ('MD', 'Maryland'), 
        ('MA', 'Massachusetts'), 
        ('MI', 'Michigan'), 
        ('MN', 'Minnesota'), 
        ('MS', 'Mississippi'), 
        ('MO', 'Missouri'), 
        ('MT', 'Montana'), 
        ('NE', 'Nebraska'), 
        ('NV', 'Nevada'), 
        ('NH', 'New Hampshire'), 
        ('NJ', 'New Jersey'), 
        ('NM', 'New Mexico'), 
        ('NY', 'New York'), 
        ('NC', 'North Carolina'), 
        ('ND', 'North Dakota'),  
        ('OH', 'Ohio'), 
        ('OK', 'Oklahoma'), 
        ('OR', 'Oregon'), 
        ('PA', 'Pennsylvania'), 
        ('RI', 'Rhode Island'), 
        ('SC', 'South Carolina'), 
        ('SD', 'South Dakota'), 
        ('TN', 'Tennessee'), 
        ('TX', 'Texas'), 
        ('UT', 'Utah'), 
        ('VT', 'Vermont'), 
        ('VA', 'Virginia'), 
        ('WA', 'Washington'), 
        ('WV', 'West Virginia'), 
        ('WI', 'Wisconsin'), 
        ('WY', 'Wyoming')
    ]
    username=models.CharField(unique=True, max_length=30)
    birth_day = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True)
    email = models.EmailField(unique=True)

    objects = UserManager()

    def __str__(self):
        return self.username