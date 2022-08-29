from modules.pizza import tamanos_pizza, tipos_borde, ingredientes, tipos_masa, tipos_salsa
from utils.input_utils import get_input_pizza
from modules.file_handler import write_file, read_file

from concurrent.futures import process

def pizza_menu():

    process = {
        '1': tamanos_pizza,
        '2': tipos_borde,
        '3': ingredientes,
        '4': tipos_masa,
        '5': tipos_salsa,
        '-1': write_file
    }
    content = read_file()
    continue_loop = True

    while continue_loop:
        user_input = get_input_pizza()
        continue_loop, content = process[user_input](content)