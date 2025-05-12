# Como se programa markdown

## headings
# theading1
## heading2
### heading3

## Formatos de texto
texto en **negrita** o *cursiva*

texto `remarcado` Para hacerlo, tenemos que usar las tildes francesas ( las que estan al lado de la tecla `P`)

## Cajas de código
Para abrir una caja de código tenemos que escribir seis veces la tilde francesa, en la tercera escribir el nombre del lenguaje de programación: `bash`, `python`, `html`, `sql`, `xml`, etc. y escribir el código dentro: 
```xml
<xml>
    <titulo/>
<xml>
```
## Imagenes
Para meter una imagen tendremos que hacerlo como en html, usando la etiqueta `img` con el atributo `src=""` ponemos la ruta relativa usando `./` y el nombre del archivo:
<img src="./C1 EOI.jpg" alt="imagen de titulo C1">

## Las listas:
- lista 1. ponemos simplemente un `-` espacio y escribimos el primer item
- lista 2. Si hacemos clic en `tabulador` antes de escribir ningun texto, tendremos una sub-lista dentro de la lista
  - lista 2.1
  - Lista 2.2

Los mismo ocurre para las listas ordenadas:
1. lista ordenada 1. Para crearla, pulsamos `1.` y luego espacio
2. lista ordenada 2. Para crear una sublista pulsamos `tab` después del `intro`
   1. sub-lista ordenada 2.1 
   2. sub-lista ordenada 2.2
   3. sub-lista ordenada 2.3
