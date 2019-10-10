import pytest
from takeaway import Takeaway

"""
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes

As a customer
So that I can verify that my order is correct
I would like to check that the total I have been given matches the sum of the various dishes in my order

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered
"""


def test_menu():
    """Returns the menu"""
    takeaway = Takeaway()
    assert takeaway.menu == {
                "Pizza": 1.0,
                "Falafel": 1.0
        }


def test_list_menu_items():
    """Returns a list of menu items"""
    takeaway = Takeaway()
    assert takeaway.list_menu_items() == "Pizza: 1.0, Falafel: 1.0, "


def test_orders_are_empty_by_default():
    """Returns the orders"""
    takeaway = Takeaway()
    assert takeaway.orders == []


def test_add_item_to_order():
    """Returns an order with one added item"""
    takeaway = Takeaway()
    takeaway.add("Pizza")
    assert takeaway.orders == [{"Pizza": 1.0}]


def test_add_different_items_to_order():
    """Returns an order with different items"""
    takeaway = Takeaway()
    takeaway.add("Pizza")
    takeaway.add("Falafel")
    assert takeaway.orders == [{"Pizza": 1.0}, {"Falafel": 1.0}]


def test_add_multiple_items_to_order():
    """Returns an order with multiple items"""
    takeaway = Takeaway()
    takeaway.add("Pizza", 2)
    assert takeaway.orders == [{"Pizza": 2.0}]
