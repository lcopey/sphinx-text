# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx

sys.path.append("../")

project = "sphinx-test"
copyright = "2023, Laurent Copey"
author = "Laurent Copey"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.napoleon", "myst_parser", "sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

from sphinx.util.logging import getLogger


def processor(app, what, name, obj, options, lines):
    logging = getLogger(__name__)
    logging.info(
        f"Processing {what} {name}",
    )
    logging.info(f"{options}")
    return False


def setup(app: Sphinx):
    # app.add_event('test')
    app.connect("autodoc-process-docstring", processor)
