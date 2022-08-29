from utils import *


def _check_input_principal(input_str):
    """
    Check if input is valid.
    """
    if input_str in ['1', '2']:
        return input_str
    return '-1'

def get_input_principal():
    """
    Get input from user and return it.
    """
    user_action = input(MENU_PRINCIPAL)
    return _check_input_principal(user_action)

def _check_input_pizza(input_str):
    """
    Check if input is valid.
    """
    if input_str in ['1', '2', '3', '4', '5']:
        return input_str
    return '-1'

def get_input_pizza():
    """
    Get input from user and return it.
    """
    user_action = input(MENU_PIZZA)
    return _check_input_pizza(user_action)

def _check_input_order(input_str):
    """
    Check if input is valid.
    """
    if input_str in ['1', '2']:
        return input_str
    return '-1'

def get_input_order():
    """
    Get input from user and return it.
    """
    user_action = input(MENU_ORDER)
    return _check_input_order(user_action)
