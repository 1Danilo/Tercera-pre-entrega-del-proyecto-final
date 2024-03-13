# Página de Iluminación
## Descripción del Proyecto
Este proyecto se centra en el desarrollo de una página web de iluminación, con la implementación de tres clases fundamentales: Producto, Cliente y Superadministrador. Cada una de estas clases desempeña un papel específico en la plataforma.
## Clases Definidas
1. **Producto:** Representa los productos de iluminación disponibles en la tienda.
1. **Cliente:** Representa a los usuarios que pueden explorar y realizar compras en la página.
1. **Superadministrador:** Posee privilegios elevados para gestionar y administrar la plataforma en su totalidad.
## Carga de Formularios
Se ha implementado un sistema de carga de formularios para facilitar la incorporación de nuevos productos y la gestión de clientes por parte del superadministrador.
## Iniciar el Proyecto
Para ejecutar el proyecto, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
1. Abre una terminal y navega hasta el directorio del proyecto.
1. Ejecuta el siguiente comando:
   ~~~ bash
   python manage.py runserver
   Esto iniciará el servidor de desarrollo de Django y podrás acceder a la aplicación desde tu navegador.

   Accesos de Administrador de Django
   Utiliza las siguientes credenciales para acceder a la interfaz de administrador de Django:

   Usuario: super_admin
   Contraseña: Administrador.1234!
   A partir de aquí, podrás gestionar productos, clientes y realizar otras tareas administrativas necesarias para el buen funcionamiento de la página de iluminación.

   ¡Esperamos que disfrutes explorando la plataforma de iluminación!

   Estructura del Proyecto
   plaintext
   Copy code
   └── 📁ProyectoCoder
   └── 📁.idea
        └── .gitignore
        └── dbnavigator.xml
        └── 📁inspectionProfiles
            └── profiles_settings.xml
            └── Project_Default.xml
        └── misc.xml
        └── modules.xml
        └── ProyectoCoder.iml
        └── workspace.xml
   └── 📁AppCoder
        └── admin.py
        └── apps.py
        └── forms.py
        └── 📁migrations
            └── 0001_initial.py
            └── 0002_entregable_estudiante_profesor.py
            └── 0003_cliente_producto_superadmin.py
            └── 0004_alter_producto_id.py
            └── 0005_delete_estudiante_delete_profesor.py
            └── 0006_delete_curso_producto_sku.py
            └── 0007_alter_producto_sku.py
            └── 0008_remove_producto_sku.py
            └── 0009_producto_serie.py
            └── 0010_remove_producto_precio.py
            └── 0011_alter_producto_serie.py
            └── __init__.py
            └── 📁__pycache__
                └── 0001_initial.cpython-312.pyc
                └── 0002_entregable_estudiante_profesor.cpython-312.pyc
                └── 0003_cliente_producto_superadmin.cpython-312.pyc
                └── 0004_alter_producto_id.cpython-312.pyc
                └── 0005_delete_estudiante_delete_profesor.cpython-312.pyc
                └── 0006_delete_curso_producto_sku.cpython-312.pyc
                └── 0007_alter_producto_sku.cpython-312.pyc
                └── 0008_remove_producto_sku.cpython-312.pyc
                └── 0009_producto_serie.cpython-312.pyc
                └── 0010_remove_producto_precio.cpython-312.pyc
                └── 0011_alter_producto_serie.cpython-312.pyc
                └── __init__.cpython-312.pyc
        └── models.py
        └── 📁static
            └── 📁AppCoder
                └── 📁assets
                    └── favicon.ico
                    └── 📁img
                        └── bg-masthead.jpg
                        └── 📁portfolio
                            └── 📁fullsize
                                └── 1.jpg
                                └── 2.jpg
                                └── 3.jpg
                                └── 4.jpg
                                └── 5.jpg
                                └── 6.jpg
                            └── 📁thumbnails
                                └── 1.jpg
                                └── 2.jpg
                                └── 3.jpg
                                └── 4.jpg
                                └── 5.jpg
                                └── 6.jpg
                └── 📁css
                    └── styles.css
                └── index.html
                └── 📁js
                    └── scripts.js
        └── 📁templates
            └── 📁AppCoder
                └── busquedaProductos.html
                └── cliente.html
                └── entregables.html
                └── inicio.html
                └── padre.html
                └── producto.html
                └── productoFormulario.html
                └── resultados.html
                └── superadmin.html
        └── tests.py
        └── urls.py
        └── views.py
        └── __init__.py
        └── 📁__pycache__
            └── admin.cpython-312.pyc
            └── apps.cpython-312.pyc
            └── forms.cpython-312.pyc
            └── models.cpython-312.pyc
            └── urls.cpython-312.pyc
            └── views.cpython-312.pyc
            └── __init__.cpython-312.pyc
   └── db.sqlite3
   └── manage.py
   └── 📁ProyectoCoder
        └── asgi.py
        └── settings.py
        └── urls.py
        └── wsgi.py
        └── __init__.py
        └── 📁__pycache__
            └── settings.cpython-312.pyc
            └── urls.cpython-312.pyc
            └── wsgi.cpython-312.pyc
            └── __init__.cpython-312.pyc
   ~~~
