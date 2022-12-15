# Just-Django-Tutorial

## SIGNALS

Signals consists of a sender and receiver
Used to listen for events
post_save and pre_save are used to send signals before or after data is saved in the database
post_save => Add logic after saving something to the database
pre_save=>Add logic before saving something to the database

## CRUD

CRUD stands for create-read-update-delete
all websites can be categorized under  CRUD
django.views.generic has the following  CRUD operation classes

1. TemplateView => Displaying a template
2. CreateView =>Creating a new object with a form
3. DeleteView=>Deleting
4. ListView=>showing a list
5. UpdateView=>updating

context passed thru a class view is reffered to as object_list
But we can customise it by this : context_object_name="leads"

## EMAIL CONTEXT that is passed to the email template

for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }
