class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero.")
        
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio: float):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El nuevo precio debe ser un número mayor o igual a cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad: int):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La nueva cantidad debe ser un número entero mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto al inventario.")
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El término de búsqueda no es válido.")
        
        nombre_buscar = nombre.strip().lower()
        for p in self.productos:
            if p.nombre.lower() == nombre_buscar:
                return p
        return None

    def calcular_valor_inventario(self) -> float:
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


def menu_principal():
    inventario = Inventario()
    
    while True:
        print("\n" + "="*30)
        print("--- Sistema de Inventario ---")
        print("="*30)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            try:
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio: "))
                cantidad = int(input("Ingrese la cantidad: "))
                
                nuevo_producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
                print(f"\n Producto '{nombre}' agregado exitosamente.")
            except ValueError as e:
                print(f"\n Error de valor: {e}")
            except TypeError as e:
                print(f"\n Error de tipo: {e}")
            except Exception as e:
                print(f"\n Error inesperado al agregar el producto: {e}")
                
        elif opcion == '2':
            try:
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print("\n Producto encontrado:")
                    print("-" * 20)
                    print(producto)
                else:
                    print(f"\n No se encontró ningún producto con el nombre '{nombre}'.")
            except Exception as e:
                print(f"\n Error en la búsqueda: {e}")
                
        elif opcion == '3':
            print("\n--- Lista de Productos ---")
            inventario.listar_productos()
            
        elif opcion == '4':
            total = inventario.calcular_valor_inventario()
            print(f"\n Valor total del inventario: ${total:.2f}")
            
        elif opcion == '5':
            print("\n¡Gracias por utilizar el sistema de inventario! Hasta pronto.")
            break
            
        else:
            print("\n Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == '__main__':
    menu_principal()
