from django.db import models
from django.db.models import *
from django.core.validators import MinLengthValidator




class StatusOptions(TextChoices):
    # Used by User, Inventory and Booking
    DENIED = "0", "Denied"
    PENDING = "1", "Pending"
    APPROVED = "2", "Approved"


class Person(Model):
    first_name = CharField(max_length=32)
    
    surname = CharField(max_length=32)
    email = CharField(max_length=32)
    phone = IntegerField()
    address = CharField(max_length=32)

    username = CharField(max_length=12)
    password = CharField(
        max_length=12,
        validators=[MinLengthValidator(6)]
    )
    
    class AccountLevel(TextChoices):
        ADMIN = "0", "Admin"
        STAFF = "1", "Staff"
        STUDENT = "2", "Student"

    account_level = TextField(
        max_length=7,
        choices=AccountLevel.choices,
        default=AccountLevel.STUDENT
    )
    
    # Primary Key
    person_id = BigAutoField(primary_key=True)


class User(Model):
    person_id = OneToOneField(Person, on_delete=CASCADE)


    # see here for ref: 
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    verification_status = CharField(
        max_length=8,
        choices=StatusOptions.choices,
        default=StatusOptions.PENDING
    )

    # NOTE(Gohar): As I am making the database, I do not think we need to add
    # a ref to the booking number inside User table
    # Rather we query Booking table with person_id to find all bookings
    # the user has
    # booking = OneToManyField(Booking)


class Admin(Model):
    person_id = OneToOneField(Person, on_delete=CASCADE)

    # All the bookings the Admin has approved or denied.
    list_of_booking = ManyToManyField("Booking")

    # NOTE(Gohar): not sure if we need a ref to inventory id here
    # inventory = OneToOneField(Inventory)

    # NOTE(Gohar): Same case as User, please read above for explanation
    # as to why we do not need a ref to a booking id here
    # booking = OneToManyField(Booking)


class Booking(Model):
    booking_num = BigAutoField(primary_key=True)

    # Please see https://stackoverflow.com/a/38389488 
    # for any questions about on_delete

    # NOTE(Gohar): look into OneToOneField or OneToManyField for both ids

    user_id = ForeignKey(
        User,
        on_delete=PROTECT
    )


    admin_id = ForeignKey(
        Admin,
        on_delete=PROTECT
        
    )
    
    # see here for ref: 
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    equipment_approvel_status = CharField(
        max_length=8,
        choices=StatusOptions.choices,
        default=StatusOptions.PENDING
    )

    # NOTE(Gohar): Using a ManyToManyField 
    # to hold past equipments 
    # see here: 
    # https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/#many-to-many-relationships
    equipment_list = ManyToManyField("Equipment")

    # booking created date
    booking_date = DateField(auto_now_add=True)
    # stores the dates the booking will be used for
    usage_date = TextField(null=True)
    # the date the equipment must be returned by
    return_date = DateField()
    # the date the equipment was returned
    delivered_date = DateField()

    # has the current date
    # exceeded the return date
    overdue = BooleanField(default=False)
    # comment user/admin can make
    note = CharField(max_length=255)


class Inventory(Model):
    inventory_id = BigAutoField(primary_key=True)

    equipment_list = ManyToManyField("Equipment")

    audit_date = DateField()
    location = TextField(max_length=200)

    # see here for ref: 
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
    status = CharField(
        max_length=8,
        choices=StatusOptions.choices,
        default=StatusOptions.PENDING
    )

    comments = TextField(max_length=255)

    # IMPORATNT NOTE(Gohar): no knowledge of why this is needed
    # please add a comment as to why and what type this should be
    history = TextField(max_length=255)

class Equipment(Model):
    equipment_id = BigAutoField(primary_key=True)

    equip_name = CharField(max_length=32)
    quantity = PositiveIntegerField(default=0)
    equip_type = CharField(max_length=32)

    # the equipment can be used
    # only on site
    on_site = BooleanField()
    # can it be borrowed
    borrowable = BooleanField()

    past_booking_nums = ManyToManyField("Booking")

    warranty = DateField()
    date_added = DateField(auto_now_add=True)
   




class Report(Model):
    report_num = BigAutoField(primary_key=True)

    # infinite possibilities thus TextField is used
    report_type = TextField(max_length=255)
    generation_date = DateField(auto_now_add=True)

    # NOTE(Gohar): look at relationship between the tables
    # again
    inventory = OneToOneField(Inventory, on_delete=CASCADE)
    admin = OneToOneField(Admin, on_delete=CASCADE)




