from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a superuser for our own auth model MyUser'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating superuser...'))
        from app.models import MyUser

        phone = input("Enter phone number: ")

        if MyUser.objects.filter(phone=phone).exists():
            self.stdout.write(self.style.ERROR('User with this phone number already exists!'))
            return

        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        if password != confirm_password:
            self.stdout.write(self.style.ERROR('Passwords do not match!'))
            return

        MyUser(phone=phone, password=password, is_superuser=True, is_customer=False).save()
        self.stdout.write(self.style.SUCCESS('Superuser created successfully for own auth model MyUser!'))
