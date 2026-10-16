from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User

#runs after save:
@receiver(post_save,sender=User)
def User_saved(sender,instance,created,**kwargs):
    if created:
        print("New User Created: ",instance.name)
    else:
        print("Student Updated: ",instance.name)

#runs before save:
@receiver(pre_save,sender=User)
def User_before_save(sender,instance,**kwargs):
    print(f"saving: {instance.name}")

    instance.name = instance.name.title()
