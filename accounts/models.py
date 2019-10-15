from django.contrib.auth.models import AbstractUser

#this is a must do before making your fist migration or djnago will give you a defualt CustomUser
class CustomUser(AbstractUser):
    pass
