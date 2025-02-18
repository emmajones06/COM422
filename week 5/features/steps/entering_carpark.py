from behave import *
from vehicle import vehicle
from carpark import carpark

@given(u'an empty car park')
def step_impl(context):
    cp = carpark(15)
    context.carpark = cp


@when(u'a car with a reg number of "abc" enters the car park')
def step_impl(context):
    car = vehicle("abc", "Car")
    context.carpark.add_car(car)



@then(u'a car with a reg number of "abc" should occupy a space in the car park')
def step_impl(context):
    assert context.carpark.spaces[0].reg == "abc"


@given(u'a carpark that holds a car with the reg number "abc"')
def step_impl(context):
    cp = carpark(15)
    cp.add_car( vehicle("abc", "Car") )
    context.carpark = cp


@when(u'a second car with the reg number "abc" tries to enter the carpark')
def step_impl(context):
    context.carpark.add_car( vehicle("abc", "Car") )

@then(u'only one car with the reg number "abc" should occupy a space in the car park')
def step_impl(context):
    count = 0
    for car in context.carpark.spaces:
        if car.reg == "abc":
            count += 1

    assert count == 1