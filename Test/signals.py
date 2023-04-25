from django.db.models.signals import m2m_changed
from Test.models import User
from django.db.models import F




def like_add_remove(sender, instance, reverse, model, *args, **kwargs):
    # print(kwargs)
    _id, = kwargs['pk_set'] if kwargs['pk_set'] else (0,)
    print("in action", kwargs["action"], kwargs['pk_set'])

    if kwargs["action"] == "post_add" and _id:
        model.objects.filter(id=_id).update(total_like=F('total_like')+1)
        
    elif kwargs["action"] == "post_remove" and _id:
        model.objects.filter(id=_id).update(total_like=F('total_like')-1)

    else:
        print("error")

m2m_changed.connect(
    like_add_remove, sender=User.like.through,) 