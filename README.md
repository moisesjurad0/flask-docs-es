[![Documentation Status](https://readthedocs.org/projects/flask-es/badge/?version=main)](https://flask-es.readthedocs.io/?badge=main)

# Traducción al Español de la documentación de Flask

## Guía de contribución


### Instalación

- Haz clic en el botón "Fork" para bifurcar este repositorio en GitHub.
- Clona tu repositorio localmente (sustituye `{usuario}` por tu nombre de usuario):

```
$ git clone https://github.com/{usuario}/flask-docs-es
$ cd flask-docs-es
$ git remote add upstream https://github.com/Jalkhov/flask-docs-es
```

- Cree un entorno virtual e instale los requisitos:

Para Linux/macOS:

```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install --upgrade pip setuptools
$ pip install -r requirements/dev.txt
$ pip install -e .
$ pre-commit install
```

Para Windows:

```
> python -m venv env
> env\Scripts\activate
> python -m pip install --upgrade pip setuptools
> pip install -r .\requirements\dev.txt
> pip install -e .
> pre-commit install
```


### Autoasignación

- Abre tu repositorio fork en GitHub.
- Haz clic en el botón "Fetch upstream" para actualizar tu fork.
- Haz clic en el botón de edición (un icono de un lápiz en la esquina superior derecha del README)
para editar el README.
- Encuentra la sección "Lista de tareas de traducción", marca el capítulo que quieres
traducir en el siguiente formato:

```
- [ ] ejemplo @tu_usuario Tu nombre
```

Puedes vincular el nombre de usuario a tu perfil de GitHub:

```
- [ ] ejemplo [@tu_usuario](https://github.com/tu_usuario) Tu nombre
```

- Deje un commit (por ejemplo, "Asignar ejemplo a @tu_usuario"), luego seleccione
"Create a new branch for this commit and start a pull request" y haga clic en el botón
"Commit changes" para crear un PR.


### Traducción

- Cuando se fusione el PR de autoasignación, cree una nueva rama localmente
(asegúrese de actualizar el nombre de la rama de ejemplo, por ejemplo, `translate-cli`):

```
$ git fetch upstream
$ git checkout -b nombre-de-tu-rama upstream/main
```

- Traduzca el archivo `.po` en el directorio `docs/locales/es/LC_MESSAGES`.

A continuación se muestra un ejemplo de un archivo de este tipo, de docs/.../index.po.

```po
#: ../../index.rst:4
msgid "Welcome to Flask"
msgstr "Bienvenido a Flask"
```

En otro caso, msgid es un texto de varias líneas y contiene la sintaxis reStructuredText:

```po
#: ../../index.rst:11
msgid ""
"Welcome to Flask's documentation. Get started with :doc:`installation` "
"and then get an overview with the :doc:`quickstart`."
msgstr ""
"Bienvenido a la documentación de Flask. Empieza con :doc:`installation`"
"y luego obtén una visión general con el :doc:`quickstart`".
```

Tenga cuidado de no romper la notación reST. La mayoría de los
[editores po](https://www.gnu.org/software/trans-coord/manual/web-trans/html_node/PO-Editors.html) le ayudarán con eso.

- Marque el capítulo como finalizado (rellene la casilla con una "x"):

```
- [x] ejemplo @tu_usuario Tu nombre
```

- Actualice el campo `Last-Translator` en la parte superior del archivo `.po`.
- Confirme los cambios (commit):

```
$ git add docs/locales/es/LC_MESSAGES/ejemplo.po README.md
$ git commit -m "Traducir docs/ejemplo"
```

- Construya los documentos y previsualice los cambios:

Para Linux/macOS:

```
$ cd docs
$ make html
```

Para Windows:

```
> cd docs
> .\make.bat html
```

Abra `{ruta_del_proyecto}/docs/_build/html/index.html` en su navegador para ver los documentos.

- Si todo funciona como se espera, lleve los cambios a GitHub:

```
$ git push origin nombre-de-tu-rama
```

- Abra la página principal de su repositorio bifurcado, verá un aviso sobre
la nueva rama. Haga clic en el botón "Compare & pull request" para crear un PR.
- El coordinador de traducción revisará su PR muy pronto. Gracias.


## Lista de tareas de traducción

Asegúrese de marcar sólo un capítulo a la vez, marque otro cuando el anterior
PR sea creado. A menos que sea un capítulo largo, podemos reiniciar la tarea
si no terminas la traducción en diez días.


### docs/

- [x] advanced_foreword [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [ ] appcontext
- [ ] async-await
- [ ] becomingbig
- [ ] blueprints
- [ ] changes
- [ ] cli
- [ ] config
- [ ] contributing
- [ ] debugging
- [ ] design
- [ ] errorhandling
- [ ] extensiondev
- [ ] extensions
- [x] foreword [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [ ] htmlfaq
- [x] index [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [ ] installation [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [ ] logging
- [x] quickstart [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [ ] reqcontext
- [ ] security
- [ ] server
- [ ] shell
- [ ] signals
- [ ] templating
- [ ] testing
- [ ] views


### docs/tutorial/

- [ ] blog
- [ ] database
- [ ] deploy
- [ ] factory
- [ ] index
- [ ] install
- [ ] layout
- [ ] next
- [ ] static
- [ ] templates
- [ ] tests
- [ ] views


### docs/deploying/

- [ ] asgi
- [ ] cgi
- [ ] fastcgi
- [ ] index
- [ ] mod_wsgi
- [ ] uwsgi
- [ ] wsgi-standalone


### docs/patterns/

- [ ] appdispatch
- [ ] appfactories
- [ ] caching
- [ ] celery
- [ ] deferredcallbacks
- [ ] distribute
- [ ] fabric
- [ ] favicon
- [ ] fileuploads
- [ ] flashing
- [ ] index
- [ ] jquery
- [ ] lazyloading
- [ ] methodoverrides
- [ ] mongoengine
- [ ] packages
- [ ] requestchecksum
- [ ] singlepageapplications
- [ ] sqlalchemy
- [ ] sqlite3
- [ ] streaming
- [ ] subclassing
- [ ] templateinheritance
- [ ] urlprocessors
- [ ] viewdecorators
- [ ] wtforms


## docs/api

- [x] L0~L1000 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L1000~L1500 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L1500~L2000 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L2000~L2500 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L2500~L3000 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L3000~L3500 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L3500~L4000 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L4000~L4500 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L4500~L5000 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L5000~L5500 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L5500~L6000 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
- [x] L6000~L6500 [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt
