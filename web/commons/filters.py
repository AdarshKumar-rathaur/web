#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


_months = ['',
    'enero', 'febrero', 'marzo', 'abril',
    'mayo', 'junio', 'julio', 'agosto',
    'septiembre', 'octubre', 'noviembre', 'diciembre',
    ]


def as_month(f, num_letters=0):
    global _months
    n = getattr(f, 'month', f)
    if num_letters:
        return _months[n][0:num_letters]
    else:
        return _months[n]


def as_date(f):
    today = datetime.date.today()
    if f.year == today.year:
        return '{}/{}'.format(f.day, as_month(f, 3))
    else:
        return '{}/{}/{}'.format(f.day, as_month(f, 3), f.year)
