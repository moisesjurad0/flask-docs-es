import packaging.version
from pallets_sphinx_themes import ProjectLink, get_version

# Project --------------------------------------------------------------

project = "Flask"
copyright = "2010 Pallets"
author = "Pallets"
release, version = get_version("Flask")

# General --------------------------------------------------------------

master_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "pallets_sphinx_themes",
    "sphinx_issues",
    "sphinx_tabs.tabs",
]
autodoc_typehints = "description"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "werkzeug": ("https://werkzeug.palletsprojects.com/", None),
    "click": ("https://click.palletsprojects.com/", None),
    "jinja": ("https://jinja.palletsprojects.com/", None),
    "itsdangerous": ("https://itsdangerous.palletsprojects.com/", None),
    "sqlalchemy": ("https://docs.sqlalchemy.org/", None),
    "wtforms": ("https://wtforms.readthedocs.io/", None),
    "blinker": ("https://pythonhosted.org/blinker/", None),
}
issues_github_path = "pallets/flask"

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_theme_options = {"index_sidebar_logo": False}
html_context = {
    "project_links": [
        ProjectLink("Donar", "https://palletsprojects.com/donate"),
        ProjectLink("Publicaciones en PyPI",
                    "https://pypi.org/project/Flask/"),
        ProjectLink("Código fuente", "https://github.com/pallets/flask/"),
        ProjectLink(
            "Seguimiento de problemas", "https://github.com/pallets/flask/issues/"
        ),
        ProjectLink("Página web", "https://palletsprojects.com/p/flask/"),
        ProjectLink("Twitter", "https://twitter.com/PalletsTeam"),
        ProjectLink("Chat", "https://discord.gg/pallets"),
        ProjectLink(
            "Participar en la traducción", "https://github.com/Jalkhov/flask-docs-es"
        ),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
}
singlehtml_sidebars = {
    "index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_static_path = ["_static"]
html_favicon = "_static/flask-icon.png"
html_logo = "_static/flask-icon.png"
html_title = f"Documentación de Flask ({version})"
html_show_sourcelink = False

# LaTeX ----------------------------------------------------------------

latex_documents = [(master_doc, f"Flask-{version}.tex", html_title, author, "manual")]

# Local Extensions -----------------------------------------------------


def github_link(name, rawtext, text, lineno, inliner, options=None, content=None):
    app = inliner.document.settings.env.app
    release = app.config.release
    base_url = "https://github.com/pallets/flask/tree/"

    if text.endswith(">"):
        words, text = text[:-1].rsplit("<", 1)
        words = words.strip()
    else:
        words = None

    if packaging.version.parse(release).is_devrelease:
        url = f"{base_url}main/{text}"
    else:
        url = f"{base_url}{release}/{text}"

    if words is None:
        words = url

    from docutils.nodes import reference
    from docutils.parsers.rst.roles import set_classes

    options = options or {}
    set_classes(options)
    node = reference(rawtext, words, refuri=url, **options)
    return [node], []


def setup(app):
    app.add_role("gh", github_link)


# Translation ----------------------------------------------------------

locale_dirs = ["locales"]
gettext_compact = False
language = "es"
html_search_language = "es"
