import requests
import json

def GetAllProducts():
    url = 'https://fakestoreapi.com/products'
    respuesta = requests.get(url).json()
    print("Listado de productos ")
    print('---------------------')
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))


def GetProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Búsqueda de producto")
    
    product_id = input("Ingrese el ID del producto que desea consultar: ")

    try:
        url = f"{url_base}/{product_id}"
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
        
        if response.text:  # Verifica si la respuesta no está vacía
            producto = response.json()
            print("Detalles del producto solicitado: ")
            print("----------------------------------")
            print(json.dumps(producto, indent=4, ensure_ascii=False))
        else:
            print("Producto no encontrado.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Producto no encontrado.")
        else:
            print(f"Error HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    except json.JSONDecodeError:
        print("Producto no encontrado.")
    except Exception as err:
        print(f"Ha ocurrido un error inesperado: {err}")

    
def AddProduct():
    url = 'https://fakestoreapi.com/products'
    print("Agregar producto")
    print("----------------")
    title = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    description = input("Ingrese la descripción del producto: ")
    image = input("Ingrese la URL de la imagen del producto: ")
    category = input("Ingrese la categoría del producto: ")

    nuevo_producto = {
        "title": title,
        "price": price,
        "description": description,
        "image": image,
        "category": category
    }
    
    response = requests.post(url, json=nuevo_producto)
    
    if response.status_code == 200 or response.status_code == 201:
        print("Producto agregado correctamente :)")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("HUbo un error al agregar el producto", response.status_code)


def UpdateProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Modificar producto")
    print("------------------")
 
    product_id = input("Ingrese el ID del producto que desea modificar: ")
    
    title = input("Ingrese el nuevo nombre del producto: ")
    price = float(input("Ingrese el nuevo precio del producto: "))
    description = input("Ingrese la nueva descripción del producto: ")
    image = input("Ingrese la nueva URL de la imagen del producto: ")
    category = input("Ingrese la nueva categoría del producto: ")

    
    producto_actualizado = {
        "title": title,
        "price": price,
        "description" : description,
        "image": image,
        "category" : category
    }
    
    url = f"{url_base}/{product_id}"
    response = requests.put(url, json=producto_actualizado)
    
    if response.status_code == 200:
        print("Producto modificado correctamente")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("Hubo un error al modificar el producto", response.status_code)  


def DeleteProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Eliminación de producto")
    print("-----------------------")
    
    product_id = input("Ingrese el ID del producto que desea eliminar: ")
    url = f"{url_base}/{product_id}"

    try:
        # Obtener el producto primero para verificar su existencia
        check_response = requests.get(url)
        if check_response.status_code == 404:
            print("El producto no existe, no se puede eliminar.")
            return

        # Verificar si la respuesta no está vacía (producto existe)
        if check_response.text:
            # Intentar eliminar el producto
            response = requests.delete(url)
            if response.status_code == 200 or response.status_code == 204:
                print("Producto eliminado correctamente.")
            else:
                print("Hubo un error al eliminar el producto:", response.status_code)
        else:
            print("Producto no encontrado, no se puede eliminar.")
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    except Exception as err:
        print(f"Ha ocurrido un error inesperado: {err}")


def mostrar_menu():
    print("\nAdministración de Productos:")
    print("1. Consultar todos los productos")
    print("2. Consultar un producto en específico")
    print("3. Agregar un nuevo producto")
    print("4. Modificar producto en específico")
    print("5. Eliminar un producto")
    print("6. Salir")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == '1':
        GetAllProducts()
    elif opcion == '2':
        GetProduct()
    elif opcion == '3':
        AddProduct()
    elif opcion == '4':
        UpdateProduct()    
    elif opcion == '5':
        DeleteProduct()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")

