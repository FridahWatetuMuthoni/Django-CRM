from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


"""class LeadManger(models.Manager):
    # returns all leads created by the user
    def agent_leads(self, user):
        return super(LeadManger, self).get_queryset().filter(agent__user=user)
"""


class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_organiser = models.BooleanField(default=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    """@receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
"""


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        'Agent', blank=True, null=True, on_delete=models.SET_NULL)
    # best way to name a related name is to base it on the model
    category = models.ForeignKey(
        'Category', related_name='leads', on_delete=models.SET_NULL, blank=True, null=True)

    #user_leads = LeadManger()
    objects = models.Manager()

    def __str__(self):
        return self.first_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# The receiver
def create_profile(sender, instance, created, **kwargs):
    # What you want to happen after a new user is created
    print('Creating a new user profile when a new user is created')
    print(created)

    if created:
        profile = UserProfile.objects.create(user=instance)
        profile.save()
        print('user created')


# The signal
post_save.connect(create_profile, sender=User)
