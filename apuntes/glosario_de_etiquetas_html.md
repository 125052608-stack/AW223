# Glosario de Etiquetas HTML

Documentación de las etiquetas utilizadas en la vista de **Mensajes Recibidos** (`Zona Administración`), agrupadas según su función estructural.

---

## 1. Estructura Base y Metadatos

| Etiqueta | Descripción y Función |
| :--- | :--- |
| `<!DOCTYPE html>` | Indica al navegador que el documento está escrito bajo el estándar **HTML5**. |
| `<html lang="es">` | Etiqueta raíz que envuelve todo el código de la página. El atributo `lang="es"` especifica que el idioma principal es español. |
| `<head>` | Contiene información de configuración, metadatos y enlaces a recursos externos que no son visibles directamente en la pantalla. |
| `<meta>` | Define metadatos del documento:<br>• `charset="UTF-8"`: Permite mostrar correctamente acentos, la letra "ñ" y símbolos especiales.<br>• `name="viewport"`: Ajusta el ancho de la página al tamaño de la pantalla del dispositivo (diseño responsivo). |
| `<title>` | Define el título que aparece en la pestaña del navegador (*"Mensajes Recibidos"*). |
| `<link>` | Vincula archivos externos al documento HTML, como tu hoja de estilos local (`estilos.css`) y la librería de íconos **FontAwesome**. |
| `<style>` | Permite escribir código **CSS** directamente dentro del documento para darle diseño, colores y distribución a los elementos. |
| `<body>` | Contiene todo el contenido visible de la página web (textos, tablas, botones, íconos, etc.). |

---

## 2. Estructura Semántica (Maquetación)

| Etiqueta | Descripción y Función |
| :--- | :--- |
| `<header>` | Representa la cabecera o parte superior de la página, donde se ubica el título principal de la *Zona Administración*. |
| `<nav>` | Define una sección destinada a enlaces de navegación (contiene el botón de inicio para regresar a `index.html`). |
| `<main>` | Envuelve el contenido principal y único del documento (la tarjeta con la tabla de mensajes). |
| `<footer>` | Define el pie de página en la parte inferior, usado para los derechos de autor y el nombre de la práctica. |
| `<div>` | Contenedor genérico en bloque sin significado semántico propio. Se usa para agrupar elementos y aplicarles estilos CSS (como `.admin-card` o `.table-responsive`). |

---

## 3. Textos, Enlaces e Íconos

| Etiqueta | Descripción y Función |
| :--- | :--- |
| `<h1>` | Encabezado de nivel 1 (el título de mayor jerarquía e importancia en la página). |
| `<h2>` | Encabezado de nivel 2 (subtítulo de sección, usado dentro de la tarjeta blanca). |
| `<p>` | Define un párrafo de texto estándar. |
| `<a>` | Crea un hipervínculo o enlace:<br>• `href`: Indica la ruta o URL de destino (`index.html`, `editar.php?id=1`).<br>• `title`: Muestra un texto descriptivo flotante al pasar el cursor por encima. |
| `<i>` | Utilizada junto con las clases de **FontAwesome** (ej. `fa-solid fa-house`) para renderizar íconos vectoriales. |

---

## 4. Estructura de Tablas

| Etiqueta | Descripción y Función |
| :--- | :--- |
| `<table>` | Define el contenedor principal de una tabla de datos. |
| `<thead>` | Agrupa las filas que funcionan como encabezado de las columnas de la tabla. |
| `<tbody>` | Agrupa el cuerpo principal de la tabla, es decir, todas las filas que contienen los registros o mensajes. |
| `<tr>` | *(Table Row)* Define una fila horizontal dentro de la tabla. |
| `<th>` | *(Table Header)* Define una celda de encabezado dentro de un `<tr>`. Por defecto se muestra en negrita. |
| `<td>` | *(Table Data)* Define una celda estándar que contiene los datos de cada registro. |