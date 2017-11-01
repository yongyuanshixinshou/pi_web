#  -*- coding: utf-8 -*-

from flask import render_template, Response, redirect, url_for

from app import redis
from app.car import car
from app.main import main


@car.route('/car/')
def index():
    return render_template('car/index.html')


@car.route('/car/control/<string:direction>/')
def control(direction):
    redis.publish("direction", direction)
    return ""
