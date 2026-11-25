# Glosario de Selectores y Propiedades CSS

Documentación de las reglas **CSS** utilizadas dentro de la etiqueta `<style>` para el diseño de la vista **Mensajes Recibidos** (`Zona Administración`).

---

## 1. Selectores (Cómo se eligen los elementos)

| Selector | Ejemplo | Descripción y Función |
| :--- | :--- | :--- |
| **Universal (`*`)** | `* { ... }` | Selecciona **absolutamente todos** los elementos de la página para aplicarles reglas base (reseteo de márgenes y rellenos). |
| **Etiqueta + Clase** | `body.admin-body` | Apunta únicamente a la etiqueta `<body>` que tenga asignada la clase `admin-body`. |
| **Clase (`.`)** | `.admin-card` | El punto indica que el estilo se aplicará a cualquier etiqueta HTML con el atributo `class="admin-card"`. |
| **Descendiente** | `.admin-header h1` | Selecciona todas las etiquetas `<h1>` que estén **dentro** de un elemento con la clase `.admin-header`. |
| **Pseudoclase (`:hover`)** | `.btn-action:hover` | Aplica estilos especiales únicamente en el instante en que el usuario pasa el cursor del mouse por encima del elemento. |

---

## 2. Modelo de Caja y Espaciado (Box Model)

| Propiedad | Descripción y Función |
| :--- | :--- |
| `box-sizing: border-box;` | Hace que el ancho (`width`) y alto (`height`) de un elemento incluyan su relleno (`padding`) y borde (`border`), evitando que las cajas crezcan de más. |
| `margin` | Espacio exterior que separa un elemento de sus vecinos (`margin: 0` elimina márgenes por defecto; `margin-top: auto` empuja el footer al fondo). |
| `padding` | Espacio interior entre el borde del elemento y su contenido (ej. `padding: 30px 15px` aplica 30px arriba/abajo y 15px a los lados). |
| `border-bottom` | Dibuja una línea en el borde inferior de un elemento (ej. `1px solid #e2e8f0`). |
| `border-radius` | Redondea las esquinas de un contenedor (`8px` en la tarjeta principal). |

---

## 3. Posicionamiento y Flexbox (Distribución)

| Propiedad | Descripción y Función |
| :--- | :--- |
| `display: flex;` | Convierte el contenedor en una caja flexible (**Flexbox**) para alinear y distribuir fácilmente los elementos hijos. |
| `flex-direction: column;` | Apila los elementos hijos uno debajo del otro en forma de columna (`header` arriba, `main` en medio, `footer` abajo). |
| `flex: 1;` | Hace que el contenedor principal (`.admin-container`) crezca para ocupar todo el espacio sobrante, empujando el pie de página hacia abajo. |
| `justify-content: center;` | Centra los elementos hijos horizontalmente dentro de un contenedor Flex. |
| `align-items` | Alinea los elementos verticalmente (`center` los centra; `flex-start` los alinea en la parte superior). |
| `width` / `max-width` / `min-height` | Controlan las dimensiones:<br>• `width: 100%`: Ocupa todo el ancho disponible.<br>• `max-width: 750px`: Evita que la tarjeta crezca más allá de 750px en pantallas grandes.<br>• `min-height: 100vh`: Asegura que el cuerpo mida al menos el 100% de la altura visible de la pantalla. |
| `overflow-x: auto;` | Si la tabla es más ancha que la pantalla (ej. en dispositivos móviles), activa una barra de desplazamiento horizontal solo para la tabla sin romper el diseño. |

---

## 4. Colores, Sombras y Tipografía

| Propiedad | Descripción y Función |
| :--- | :--- |
| `background-color` | Define el color de fondo usando códigos hexadecimales (ej. `#0f172a` azul oscuro, `#ffffff` blanco). |
| `color` | Define el color del texto o de los íconos vectoriales. |
| `font-family` | Define la fuente tipográfica (usa fuentes nativas del sistema operativo para mayor velocidad y apariencia moderna). |
| `font-size` | Tamaño de la letra usando `rem` (unidad relativa al tamaño base del navegador; `1rem` equivale por defecto a `16px`). |
| `font-weight` | Grosor de la letra (`600` semi-negrita, `700` negrita). |
| `font-style: italic;` | Muestra el texto en cursiva. |
| `text-align` | Alineación horizontal del texto (`left`, `center`). |
| `text-decoration: none;` | Elimina el subrayado azul que traen por defecto los hipervínculos (`<a>`). |
| `white-space: nowrap;` | Evita que los íconos de acción (editar y borrar) salten a una segunda línea si la pantalla se estrecha. |
| `box-shadow` | Agrega una sombra difuminada detrás de la tarjeta (`.admin-card`) para darle efecto de elevación. |

---

## 5. Tablas y Animaciones

| Propiedad | Descripción y Función |
| :--- | :--- |
| `border-collapse: collapse;` | Fusiona los bordes de las celdas de la tabla para que no se vean líneas dobles separadas entre sí. |
| `transition` | Suaviza los cambios de estilo (color o escala al pasar el mouse) durante `0.2s` (0.2 segundos) para evitar saltos bruscos. |
| `transform: scale(1.1);` | Aumenta ligeramente (un 10%) el tamaño del ícono de inicio cuando pasas el cursor encima. |