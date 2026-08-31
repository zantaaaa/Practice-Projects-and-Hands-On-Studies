"""
def doors (ChekDoors):
    for door in ChekDoors:
        if door == "50":
            return "Door 50 is open."
    else : 
        return "Door 50 is closed."
"""

#creación de lista del 1 al 100, supuestas puertas 
def check_doors(): #inicio de funcion 
    lista = list(range(0, 101)) #Creación de lista del 1 al 100
    return lista # salida de la función

def busqueda_door(door_number): 
    def bin_searh ():
        lista = check_doors() #llamado a la función check_doors
        low = 0 #inicio de la búsqueda
        high = len(lista) - 1 #fin de la búsqueda
        while low <= high: #bucle para buscar el número de puerta
            mid = (low + high) // 2 #cálculo del punto medio
            guess = lista[mid] #adivinanza del número de puerta
            if guess == door_number: #si la adivinanza es correcta
                return f"Door {door_number} is open." #retorna que la puerta está abierta
            if guess > door_number: #si la adivinanza es mayor que el número de puerta
                high = mid - 1 #ajusta el límite superior
            else: 
                low = mid + 1 #ajusta el límite inferior
        return f"Door {door_number} is closed." #retorna que la puerta está cerrada
# este sistema de busqueda binaria es eficiente hasta que te topas con busquedas de de numeros enormes donde tengamos que hacerla mas eficiente 
def Efficient_Binary_Search():
    search_number = int(input("Enter the door number to search: ")) #entrada del número de puerta a buscar
    search_lst = check_doors() #llamado a la función check_doors
    lst_start_number = 1 #inicio de la lista
    lst_end_number = len(search_lst) - 1 #fin de la lista
    def create_even_list():
        search_number_between = list(range(lst_start_number, lst_end_number + 1)) #creación de lista de búsqueda
        search_number_betweem = [num for num in search_number_between if num % 2 == 0] #filtrado de números pares
        return search_number_betweem #retorna la lista de búsqueda
    filtered_range = create_even_list() #llamado a la función create_even_list
    while True: #bucle infinito para la búsqueda
        if  search_number in search_lst: #si el número de búsqueda es mayor que el número de búsqueda complejo
            closet = min(filtered_range, key=lambda x: abs(x - search_number)) #busca el número más cercano
            diference = abs(closet - search_number) #calcula la diferencia
            return f"Door {search_number-diference} Open  "
        if search_number in search_lst: #si el número de búsqueda es menor que el número de búsqueda complejo
            closet = min(filtered_range, key=lambda x: abs(x - search_number)) #busca el número más cercano
            diference = abs(closet - search_number) #calcula la diferencia
            return f"Door {search_number+diference} Open  "
        if search_number in search_lst: #si el número de búsqueda es igual al número de búsqueda complejo
            return f"Door {search_number} is open." #retorna que la puerta está abierta
            break #rompe el bucle
        else :
            return f"Door {search_number} not found." #retorna que la puerta no se encontró
print(Efficient_Binary_Search()) #llamado a la función Efficient_Binary_Search