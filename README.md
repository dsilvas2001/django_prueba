Sistema de Clasificación de Imágenes - Resumen Ejecutivo
📌 Objetivo
Sistema automático que clasifica imágenes subidas por usuarios en categorías como "Documento", "Foto" o "Factura", almacenando los resultados en una base de datos mediante una arquitectura serverless en AWS.

🛠️ Componentes Clave
Backend Django (4 puntos)
Aplicación "catalogo" con modelo Imagen que incluye:

Nombre del archivo

Tipo detectado (Documento/Foto/Factura)

Descripción generada

Archivo almacenado

API REST completa con operaciones CRUD

Panel de administración Django integrado

Desplegado en AWS Lightsail/Elastic Beanstalk

Función Lambda (4 puntos)
Recibe imágenes desde S3 o en formato base64

Clasifica automáticamente usando:

Análisis de cabeceras de archivo

Modelo simple de detección

Devuelve:

Tipo detectado (ej: "Factura")

Descripción breve (ej: "Documento PDF de 2 páginas")

🔄 Flujo del Sistema
Usuario sube imagen → Bucket S3

Lambda se activa → Clasifica imagen

Resultados enviados → API Django

Datos almacenados → Base de datos

Disponibles en Admin y API REST

✅ Estado Actual
Backend Django completo con API funcional

Función Lambda básica implementada

Integración inicial S3-Lambda-Django
