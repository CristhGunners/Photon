<img src="https://scontent-dfw.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/10636088_982456151772019_2909611528891555934_n.png?oh=92f85dcd4f97ed817f3ea431d9c823f9&oe=5574DE2F" alt="Photon" height="100" width="100" style="margin:0 auto;display:block;" />

<h1 style="text-align:center;">Photon</h1>
Photon es una plataforma de codigo libre, la cual representa un banco de imagenes con multiples caracteristicas.

## Caracteristicas

- Registro y autentificacion de usuarios
- Perfiles de usuarios
- Subir imagenes
- Paginación
- Descargar y ver imagenes
- Editar perfil
- Diseño responsivo

## Stack de desarrollo

- HTML5
- Css
- Javascript
- Python 3.4.1
- Django 1.7.5
- Stylus 0.49.1
- Jquery 2.1.3

## Capturas

### Inicio

![Photon Home](https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-xfp1/t31.0-8/10945801_982429378441363_3671053479032921923_o.png)

### Perfil

![Photon Profile](https://scontent-dfw.xx.fbcdn.net/hphotos-xpf1/t31.0-8/10991632_982453825105585_5929319544336237377_o.png)

### Subir Imagen

![Photon Upload](https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-xpa1/t31.0-8/11082421_982453921772242_1177705383124456223_o.png)

### Tags

![Photon Tags](https://scontent-dfw.xx.fbcdn.net/hphotos-xpa1/t31.0-8/10269038_982453838438917_2937201247742264800_o.png)

### Iniciar Sesion

![Photon Login](https://scontent-dfw.xx.fbcdn.net/hphotos-xap1/t31.0-8/10896225_982453775105590_4383944557941284785_o.png)

### Registrarse

![Photon Register](https://scontent-dfw.xx.fbcdn.net/hphotos-xap1/t31.0-8/11050326_982453785105589_5935297192697308830_o.png)

## Pruebalo en tu equipo

Descargamos el repositorio y creamos nuestro entorno virtual, usare virtualenvwrapper:
    
    mkvirtualenv photon
    workon photon

Ahora nos ubicamos en el directorio del repositorio **photon** y ejecutamos:

    pip install -r requirements/local.txt

Con esto ya tendremos listo los paquetes necesarios para arrancar el proyecto. Ahora necesitamos agregar nuestros valores de configuración para el envio de email en el archivo **photon/settings/local.py** :
    
    # Ejemplo con Gmail

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'host@gmail.com'
    EMAIL_HOST_PASSWORD = '******'

Procedemos a migrar nuestros modelos:
    
    manage.py migrate --settings=photon.settings.local

Ahora necesitamos actualizar los valores al registro por defecto del modelo **SITE**, en este caso lo haremos por la shell de python:

    manage.py shell --settings=photon.settings.local
    >>> from django.contrib.sites.models import Site
    >>> Site.objects.filter(id=1).update(domain="http://127.0.0.1:8000",name="Photon")

Ya podremos arrancar el proyecto y comenzar a probar **Photon**:

    manage.py runserver --settings=photon.settings.local

## Contactame

Espero tu opinion :D

<a href="https://twitter.com/CristhGunners" target="_blank">
    <img src="http://img3.wikia.nocookie.net/__cb20140610122352/divergente/es/images/f/f7/Twitter.png" alt="CristhGunners" height="50" width="50" style="margin:5px auto;display:block;" />
</a>


