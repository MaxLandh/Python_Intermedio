# Python_Intermedio
***Curso de introducción***

**El Zen de Python**
Para poder visualizar el Zen de Python debemos introducir el siguiente comando

```
import  this
```


**ENTORNOS VIRTUALES**

Un entorno virtual es un python separado con sus distintas versiones para cada proyecto
Los entornos virtuales son de mucha utilidad ya que nos ayudan a tener versiones especificas 
de librerías o módulos a un proyecto sin afectar a otros.
De esta forma en el mismo equipo pueden coexistir distintos proyectos con distintas versiones 
de la misma librería o modulo.

**CREACIÓN DE AMBIENTES VIRTUALES CON PYTHON**

Para poder crear ambientes virtuales en pyton usaremos el siguiente comando
> python3 -m venv [nombre_ambiente]

Notaremos que se ha creado una nueva carpeta llamada con el nombre del ambiente.
Para poder activar nuestro ambiente virtual usaremos el siguiente script desde donde se cuentra
la carpeta que contiene el ambiente virutal

> source [nombre_ambiente]/bin/activate

Nos daremos cuenta que hemos activado el ambiente virtual ya que nos aparecera en nuestra 
linea de comandos, entre parentesis, el ambiente en donde estamos.

Para desactivar el ambiente virtual usaremos lo siguiente:

> deactivate

**PIP- PACKAGE INSTALLER FOR PYTHON**

Cuando instalamos python hay modulos que vienen por defecto al instalarlo. Pero hay modulos que no 
vienen por defecto en python. Para eso necesitaremos un manejador de paquetes, el mas popular dentro
de python es PIP. Es un modulo que viene dentro de python que sirve para instalar otros modulos que
no estan dentro de python. 

Los modulos mas populares que no vienen dentro de python son:
-requests
-BeautifulSoup4
-Pandas
-Numpy
-Pytest

Para ver que modulos han sido instalados en nuestro ambiente virutal usaremos lo siguiente:

> pip3 freeze

Para instalar modulos usaremos el siguiente comando:

> pip3 install [nombre_modulo]

Imagina el caso en el que quieres compartir tu proyecto con alguien mas que esta al otro
lado del mundo. En ese caso necesitaremos compartir exactamente los modulos que estan en nuestro
ambiente. Para esto usaremos lo siguiente con el operador de control '>'

> pip3 freeze > requierments.txt

Ahora tenemos un archivo txt que contene todos los modulos necesarios para que el proyecto funcione
en otra computadora. Para que esto sea util usaremos el flag install -r.

> pip3 install -r requierments.txt

***LISTAS Y DICCIONARIOS ANIDADOS***

Como veremos podemos anidar listas en diccionarios (como si fueran tablas),
y diccionarios en listas como si fuera una coleccion de tablas en una lista.
Ver el archivo lists_and_dict.py

NOTAS: Para comentar en VSCode podemos usar la combinación de teclas
CTRL + K  y CTRL + C 

Para descomentar

CTRL + K  y CTRL + U

**LIST COMPREHENSIONS**

Syntaxis

> list_comprehension = [*expression* for *item* in  *iterable* if *condition == True* ]


**DICT COMPREHENSIONS**

Syntaxis

> dict_comprehesions = {*expressioon*: *expression_2* for *item* in *iterable* if *condition == True*}

NOTA: Siempre que compartamos un repositorio de Python nunca debemos incluir la carpeta del ambiente
virtual. En este caso lo omitiremos con .gitignore
 
**FUNCTION LAMBDA**

La funcion lambda es una funcion anonima que no necesita ser definida 
Syntexis

> lamda *argumentos*: *expresion*

En Python las funciones lambda solo deben tener una linea de codigo, no varias.

**FUNCIONES DE ORDEN SUPERIOR**

Es una funcion que recibe como parametro a otra funcion.
Hay tres funciones de orden superior que son sumamente importantes: *filter*, *map* y *reduce*
Todas estas funciones retornan un objeto **iterable**

Filter:

> filter(*funcion lambda*, lista)

Filtra valores de una lista, entonces la funcion lamda tiene que retornar un Bool por cada valor de la lista que cumpla
expresion de lambda

Por ejemplo, queremos obtener los numeros pares de una lista que contiene los numeros del 1 al 10:

>my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>pairs = list(filter(lambda x: x%2 == 0, my_list)) 

Map:

> map(*funcion lambda*, lista)

Mapea toda la lista y las itera en la funcion lamda y retorna el valor de la expression que esta en la funcion. Tiene que ser 
cualquier operación.

Por ejemplo, queremos el cuadrado de los valores de la lista que contiene del 1 al 10:

>my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>squeres = list(map(lambda x: x**2, my_list))

Reduce

> from functools import reduce

> reduce(*funcion lambda*, list)

Reduce la lista en un solo valor de la expresion de lambda.
Por ejemplo, queremos el valor final de multiplicar los valores de una lista:

>from functools import reduce
>my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>result = reduce(lambda a, b: a*b, my_list)

**NOTA: Para concatener diccionarios usaremos el operador pipe |

### Manejador de errores

En Python existen dos tipos de errores: SyntaxisError y Exception.
**Syntaxis Error** son los errores en los que hay un error de sintaxis al momento de escribir codigo
Por ejemplo, en lugar de escribir for escribimos far, se le conoce como un error typo. Estos errores hacen que
python no corra el codigo. Lee linea por linea y si detecta este tipo de errores cancelara su ejecución.

**Exception** son los errores en los que a lo largo del codigo resulto un error en una linea especifica. Y todas las
lineas arriba si lograron ejecutarse

**Elevar una excepcion**: cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo
exception que se va moviendo a traves de los bloques de código hasta llegar al bloque principal si es que no se maneja
dicha excepción en algun bloque intermedio el programa se interrumpe y genera el traceback

### Debugging

En VS code podemos correr linea por linea nuestro codigo para ver en que punto hay un error.
En la barra lateral izquierda damos click en ***degugging*** y le damos click en run and debugging. Donde correra 
el archivo que estamos tratando de ejecutar paso a paso. Nos aparecera un menu superior donde podremos detener, ir al isguiente paso, entrar en una funcion y salir. Tambien del lado izquierdo empezaran a salir las variables que se van creando en el programa.

### try.. except
try:
	..codigo..
except **nombre_error**:
	..codigo..
	
**try**: En el bloque de codigo de try pondremos el código que se va ejecutar
**except** : En caso de que ocurra un error en el bloque ***try*** se pasara a este bloque de codigo, pero con tendra unparametro, el parametro es el nombre de la excepción.

### raise

try:
    if **condicion**:
        raise **nombre_error**'mensaje'

except **nombre_error** :
    ..codigo..

**raise** raise es un metodo por el cual si no se cumple una condición que damos elevara el error que le dimos a un bloque superior, en estecaso al que esta dentro de ***try*** (raise esta en el bloque if) donde evaluara el error y lo mandara a except.

### finally

try:

except:

finally:

**finally** se ejecuta SIEMPRE, haya sido lanzada la excepcion o no haya sido lanzada. Es utiizado normalmente para cerrar archivos, cerrar una conexión a unabase de datos, por ejemplo.

### Assert statements

Los assert statements es un manejador de errores que se compone como sigue

> assert ..condition..  ..mensaje..

En palabras seria: Afirmo que la siguiente condición es verdadera, si no, cortar el programa  y mandar el mensaje.

### else

El bloque de sentencias **try.. except** tiene una clausula extra llamada *else*. **Else** nos permite continuar con la ejecución de nuestro codigo si en el bloque try no ocurrio ningun error

try:

except:

else:

finally:

Es muy util para englobar mas sentencias try y tener mas limpio el código.

### Manejo de archivos externos

Para poder abrir archivos de texto plano en Python existen tres modos de apertura

**r** Lectura
**w** Escritura (sobree escribir)
**a** Escritura (agregar al final)

Es sencillo realizar este proceso en Python con la siguiente linea de código:

> **with** ***open***('..ruta_archivo..' , '..modo(r,w,a)..') as ..alias..:

Donde el metodo **with** es un manejador contextual, el cual controla el flujo de nuestro archivo que estemos manipulanod. ***open*** es la función que nos permitira abrir el archivo. 
Le pasamos dos parametros (puede tener mas parametros ) la ruta del archivo y el modo en que lo queremos abrir. Otros modos son los siguientes:

**x** Crea un archivo, lanza un error si ya existe.
**b** Modo binario
**t** Modo de texto

La función **open** tiene el metodo ***write()*** en el cual podemos escribir una linea en nuestro archivo.

### NOTAS

> os.systems('clear') : limpia la consola en python

> Modulos string:  el atributo  string.ascii_lowercase es un modulo que contiene el alfabeto en minusculas


