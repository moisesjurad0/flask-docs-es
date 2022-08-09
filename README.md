[![Estado de la documentación](https://readthedocs.org/projects/flask-es/badge/?version=main)](https://flask-es.readthedocs.io/?badge=main)
![Progreso de traducción](https://jalkhov.github.io/docspro/badge/es_progress.svg)
![Última sincronización con Flask](https://img.shields.io/static/v1?label=Última%20sincronización%20con%20Flask&message=11-07-2022&color=cyan)

[Ver commits en Flask desde la última sincronización](https://github.com/pallets/flask/search?o=desc&q=author-date%3A%3E2022-07-11&s=committer-date&type=Commits)

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

### Software de traducción recomendado

Como se explica a continuación, las traducciones se realizan mediante archivos `.po`. Un buen editor es [POEdit](https://poedit.net/) (no confundir con POEditor)


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

## docs/

| Finished | File              | Assigned                                             |
| -------- | ----------------- | ---------------------------------------------------- |
| &#9745;  | advanced_foreword | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | api               | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | appcontext        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | async-await       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | becomingbig       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | blueprints        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | changes           | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | cli               | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | config            | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | contributing      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | debugging         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | design            | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | errorhandling     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
|          | extensiondev      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | extensions        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | foreword          | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | htmlfaq           | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | index             | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | installation      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | license           | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | logging           | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | quickstart        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | reqcontext        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | security          | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | server            | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | shell             | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | signals           | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | templating        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | testing           | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | views             | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |


## deploying/

| Finished |       File      |                       Assigned                       |
|----------|-----------------|------------------------------------------------------|
| &#9745;  |   apache-httpd  | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |       asgi      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |       cgi       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     eventlet    | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     fastcgi     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      gevent     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     gunicorn    | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      index      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     mod_wsgi    | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      nginx      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |    proxy_fix    | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      uwsgi      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     waitress    | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | wsgi-standalone | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |


## patterns/

| Finished |          File          |                       Assigned                       |
|----------|------------------------|------------------------------------------------------|
| &#9745;  |      appdispatch       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      appfactories      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |        caching         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |         celery         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   deferredcallbacks    | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |       distribute       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |         fabric         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |        favicon         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      fileuploads       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |        flashing        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |         index          | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |       javascript       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |         jquery         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      lazyloading       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |    methodoverrides     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      mongoengine       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |        packages        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |    requestchecksum     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | singlepageapplications | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |       sqlalchemy       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |        sqlite3         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |       streaming        | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |      subclassing       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |  templateinheritance   | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     urlprocessors      | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |     viewdecorators     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |        wtforms         | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |


## tutorial/

| Finished |    File   |                       Assigned                       |
|----------|-----------|------------------------------------------------------|
| &#9745;  |    blog   | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |  database | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   deploy  | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |  factory  | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   index   | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |  install  | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   layout  | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |    next   | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   static  | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | templates | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   tests   | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  |   views   | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |


## docs/api


| Finished | Strings range | Assigned                                             |
| -------- | ------------- | ---------------------------------------------------- |
| &#9745;  | 001~123       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 123~246       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 246~369       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 369~492       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 492~615       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 615~738       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 738~861       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 861~984       | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
| &#9745;  | 984~1.107     | [@Jalkhov](https://github.com/jalkhov) Pedro Torcatt |
