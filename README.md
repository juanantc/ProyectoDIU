##### Instalar Phyton:
```sudo apt-get install python3.5```

```alias python=python3```

##### Instalar pip:
```sudo apt-get install python3-pip```

##### Instalar virtualenv:
```sudo pip install virtualenv```

##### Crear entorno:
```virtualenv proyecto```

```virtualenv -p python3 proyecto/```

##### Activar entorno:
```cd proyecto/```

```source bin/activate```

##### Instalar django:
```pip install django```

##### Crear nueva aplicación:
```django-admin.py startproject sitio```

```python manage.py startapp aplicacion```

##### Migrar:
```cd sitio/```

```python manage.py migrate```

##### Crear superusuario:

```python manage.py createsuperuser```

###### Introducir nombre de usuario deseado:

```Username: admin```

###### Introducir dirección de correo electrónico:

```Email address: admin@example.com```

###### Introducir contraseña:
```
Password: **********
Password (again): *********
Superuser created successfully.
```
