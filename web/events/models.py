#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from django.db import models

# Create your models here.


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=150)
    title = models.CharField(max_length=220)
    start_date = models.DateField()

    def __str__(self):
        return self.title


class TicketType(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def num_sold_tickets(self):
        return self.tickets.all().count()

    @property
    def num_available_tickets(self):
        return self.stock - self.tickets.all().count()


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    ticket_type = models.ForeignKey(
        TicketType,
        on_delete=models.PROTECT,
        related_name='tickets',
        )
    number = models.PositiveIntegerField()
    keycode = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=72)
    email = models.CharField(max_length=260)
    phone = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return '{}/{} {}, {}'.format(
            self.number,
            self.ticket_type.event.title,
            self.surname,
            self.name,
            )