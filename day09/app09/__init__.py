from django.db.models.signals import pre_save,post_save
from .mysingal import action

def pre_save_func(sender,**kwargs):
    print(sender)
    print(kwargs)
    print(kwargs.get("instance"))

# pre_save.connect(pre_save_func)
post_save.connect(pre_save_func)



def my_action_func(sender,**kwargs):
    print(sender)
    print(kwargs)

action.connect(my_action_func)