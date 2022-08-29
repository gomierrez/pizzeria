from modules.pizza_gestion import pizza_menu
#from modules.order_gestion import order_menu
from utils.input_utils import get_input_principal

def main():
    user_input=get_input_principal()
    if user_input=='1':
        pizza_menu()
    if user_input=='2':
        order_menu()



if __name__ == "__main__":
    main()