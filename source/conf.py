# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

from time import strftime

project = 'Varcade_BL'
author = 'F_Qilin'
copyright = f'2020-{strftime("%Y")}, {author}'

with open('../tags', 'r', encoding='utf-8') as f:
    release, ver_date = f.read().split('\n')[0:2]

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
    'sphinx_markdown_tables'
]

# templates_path = ['_templates']
exclude_patterns = ['_build']

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------

# import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_favicon = 'images/logo/va-colored.ico'
html_last_updated_fmt = '%Y-%m-%d %H:%M (%Z)'

# -- App Setup Hook ----------------------------------------------------------

from recommonmark.transform import AutoStructify

def setup(app):
    app.add_config_value('recommonmark_config', {
        # 'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
        'enable_math': False,
        'enable_inline_math': False,
        'enable_eval_rst': True,
        'enable_auto_doc_ref': False
    }, True)
    app.add_transform(AutoStructify)

# -- Other Settings ----------------------------------------------------------

rst_prolog = f"""
.. |ver| replace::         {release}
.. |ver_date| replace::    {ver_date}
"""
