# Listas en Python

## Definición
- Una **lista** en Python es una estructura de datos que permite almacenar una colección ordenada de elementos.
- Cada elemento en la lista se denomina **ítem** y puede ser de cualquier tipo de dato: números, cadenas, o incluso otras listas.
- Las listas son **mutables**, lo que significa que pueden ser modificadas después de su creación.

## Creación de Listas
- Las listas se crean utilizando corchetes `[]`, y los elementos se separan por comas.
- Ejemplo: 
  ```python
  mi_lista = [1, 'dos', 3.0]
  ```

## Acceso a Elementos
- Los elementos de la lista se acceden mediante índices, empezando por el índice `0`.
- Ejemplo: `mi_lista[0]` devuelve `1`.
- Los índices negativos se pueden usar para acceder a los elementos desde el final de la lista (por ejemplo, `mi_lista[-1]` devuelve el último elemento).

## Mutabilidad
- Las listas pueden ser alteradas, permitiendo cambios como:
  - **Modificar elementos**: `mi_lista[1] = 'dos cambiado'`.
  - **Añadir elementos**: `mi_lista.append(4)`.
  - **Eliminar elementos**: `mi_lista.remove('dos')` o `del mi_lista[1]`.

## Métodos Comunes
- **`append(elemento)`**: Añade un elemento al final de la lista.
- **`remove(elemento)`**: Elimina la primera ocurrencia del elemento.
- **`pop([indice])`**: Elimina y devuelve el elemento en el índice dado. Si no se especifica índice