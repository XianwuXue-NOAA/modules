# -*- coding: utf-8 -*-
#
# Modules documentation build configuration file, created by
# sphinx-quickstart on Mon Oct  2 06:17:09 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Modules'
copyright = '1996-1999 John L. Furlani & Peter W. Osel, 1998-2017 R.K.Owen, 2002-2004 Mark Lakata, 2004-2017 Kent Mein, 2016-2021 Xavier Delaruelle'
author = ''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

from subprocess import Popen, PIPE
def get_version_release_from_git():
    """
    Returns project version and release as string from 'git' repository data.
    """
    DEVNULL = open(os.devnull, 'w')
    pipe = Popen('git describe --tags --abbrev=0', stdout=PIPE, stderr=DEVNULL, shell=True)
    git_current_tag = pipe.stdout.read()
    pipe = Popen('git describe --tags', stdout=PIPE, stderr=DEVNULL, shell=True)
    git_current_desc = pipe.stdout.read()
    pipe = Popen('git rev-parse --abbrev-ref HEAD', stdout=PIPE, stderr=DEVNULL, shell=True)
    git_current_branch = pipe.stdout.read()

    if git_current_desc:
        version = git_current_tag.lstrip('v').rstrip()
        if git_current_tag == git_current_desc:
            return version, ''
        else:
            branch = git_current_branch.rstrip()
            tags = git_current_desc.lstrip(git_current_tag + '-').rstrip()
            # workaround for RTD, where master branch is not detected
            if branch == 'master' or os.environ.get('READTHEDOCS', None) == 'True':
                return version, version + '+' + tags
            else:
                return version, version + '+' + branch + '-' + tags
    else:
        return '5.0.1', ''

# The short X.Y version.
# The full version, including alpha/beta/rc tags.
if os.access('version.py', os.R_OK):
    # get version and release information from version.py file
    exec(open('version.py').read())
else:
    # or fetch them from git repository data
    version, release = get_version_release_from_git()

today_fmt = '%Y-%m-%d'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
os_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if os_rtd:
    html_theme = 'sphinx_rtd_theme'
    # override wide tables in RTD theme
    # colorize terminal output
    html_context = {
        'css_files': [
            '_static/rtd_theme_overrides.css',
            '_static/rtd_literal_block.css',
            '_static/terminal_output.css',
            ],
         }
else:
    html_theme = 'bizstyle'
    # colorize terminal output
    html_context = {
        'css_files': [
            '_static/literal_block.css',
            '_static/terminal_output.css',
            ],
         }

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
if os_rtd:
    html_theme_options = { 'logo_only' : True }

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
if os_rtd:
    html_logo = '../img/modules_white.svg'
else:
    html_logo = '../img/modules_red.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '../img/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# ensure quotes and dashes are preserved and not converted to lang-specific
# entities (fix issue#250). done by disabling `html_use_smartypants` on Sphinx
# version older than 1.6 and by disabling `smartquotes` on newer versions.
from sphinx import __version__ as sphinx_version
sphinx_version_parts = [int(i) for i in sphinx_version.split('.')]
if sphinx_version_parts[0] <= 1 and sphinx_version_parts[1] < 6:
    html_use_smartypants = False
else:
    smartquotes = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Modulesdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
]


# replace locations by pattern to pre-generate pages in dist
if 'pathsubs' in tags:
    prefix = '@prefix@'
    bindir = '@bindir@'
    libexecdir = '@libexecdir@'
    etcdir = '@etcdir@'
    initdir = '@initdir@'
    modulefilesdir = '@modulefilesdir@'
# or set default distributions location
else:
    prefix = '/usr/share/Modules'
    bindir = prefix + '/bin'
    libexecdir = prefix + '/libexec'
    etcdir = '/etc/environment-modules'
    initdir = prefix + '/init'
    modulefilesdir = prefix + '/modulefiles'

rst_epilog = '\n'
rst_epilog += '.. |prefix| replace:: %s\n' % prefix
rst_epilog += '.. |emph prefix| replace:: *%s*\n' % prefix
rst_epilog += '.. |bold prefix| replace:: **%s**\n' % prefix
rst_epilog += '.. |file prefix| replace:: :file:`%s`\n' % prefix
rst_epilog += '.. |bindir| replace:: %s\n' % bindir
rst_epilog += '.. |emph bindir| replace:: *%s*\n' % bindir
rst_epilog += '.. |bold bindir| replace:: **%s**\n' % bindir
rst_epilog += '.. |libexecdir| replace:: %s\n' % libexecdir
rst_epilog += '.. |emph libexecdir| replace:: *%s*\n' % libexecdir
rst_epilog += '.. |bold libexecdir| replace:: **%s**\n' % libexecdir
rst_epilog += '.. |file libexecdir| replace:: :file:`%s`\n' % libexecdir
rst_epilog += '.. |file libexecdir_modulecmd| replace:: :file:`%s/modulecmd.tcl`\n' % libexecdir
rst_epilog += '.. |etcdir| replace:: %s\n' % etcdir
rst_epilog += '.. |emph etcdir| replace:: *%s*\n' % etcdir
rst_epilog += '.. |bold etcdir| replace:: **%s**\n' % etcdir
rst_epilog += '.. |file etcdir| replace:: :file:`%s`\n' % etcdir
rst_epilog += '.. |file etcdir_rc| replace:: :file:`%s/rc`\n' % etcdir
rst_epilog += '.. |file etcdir_siteconfig| replace:: :file:`%s/siteconfig.tcl`\n' % etcdir
rst_epilog += '.. |file etcdir_initrc| replace:: :file:`%s/initrc`\n' % etcdir
rst_epilog += '.. |file etcdir_modulespath| replace:: :file:`%s/modulespath`\n' % etcdir
rst_epilog += '.. |initdir| replace:: %s\n' % initdir
rst_epilog += '.. |emph initdir| replace:: *%s*\n' % initdir
rst_epilog += '.. |bold initdir| replace:: **%s**\n' % initdir
rst_epilog += '.. |file initdir_shell| replace:: :file:`%s/<shell>`\n' % initdir
rst_epilog += '.. |file initdir_csh| replace:: :file:`%s/csh`\n' % initdir
rst_epilog += '.. |modulefilesdir| replace:: %s\n' % modulefilesdir
rst_epilog += '.. |emph modulefilesdir| replace:: *%s*\n' % modulefilesdir
rst_epilog += '.. |bold modulefilesdir| replace:: **%s**\n' % modulefilesdir
rst_epilog += '.. |file modulefilesdir| replace:: :file:`%s`\n' % modulefilesdir
rst_epilog += '.. |code version| replace:: ``%s``\n' % version
rst_epilog += '.. |gh_tgz_dl_url| replace:: https://github.com/cea-hpc/modules/releases/download/v%s/modules-%s.tar.gz\n' % (version, version)

# define roles used to color text in parsed-literal to render output like in terminal
rst_epilog += """.. role:: noparse
.. role:: ps
.. role:: sgrhi
.. role:: sgrer
.. role:: sgrwa
.. role:: sgrin
.. role:: sgrtr
.. role:: sgrse
.. role:: sgrcm
.. role:: sgrme
.. role:: sgrmp
.. role:: sgrdi
.. role:: sgrali
.. role:: sgrva
.. role:: sgrsy
.. role:: sgrde
.. role:: sgrh
.. role:: sgral
.. role:: sgrl
.. role:: sgrf
.. role:: sgrnf
.. role:: sgrs
.. role:: sgrss"""


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('module', 'module', u'command interface to the Modules package', [], 1),
    ('ml', 'ml', u'handy command interface to the Modules package', [], 1),
    ('modulefile', 'modulefile', u'files containing Tcl code for the Modules package', [], 4)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
]


# -- Extension interface --------------------------------------------------

from sphinx import addnodes
def parse_cmd_args_node(env, sig, signode):
    try:
        cmd, args = sig.strip().split(' ', 1)
    except ValueError:
        cmd, args = sig, None
    # distinguish cmd from its args
    signode += addnodes.desc_name(cmd, cmd)
    if args:
        args = ' ' + args
        signode += addnodes.desc_addname(args, args)
    return cmd

def parse_opt_args_node(env, sig, signode):
    if (sig.strip().find('=') != -1):
        sep = '='
    else:
        sep = ', '
    try:
        opt, args = sig.strip().split(sep, 1)
    except ValueError:
        opt, args = sig, None
    # distinguish opt from its args
    signode += addnodes.desc_name(opt, opt)
    if args:
        args = sep + args
        signode += addnodes.desc_addname(args, args)
    return opt

# define new directive/role that can be used as .. subcmd::/:subcmd:,
# .. mfcmd::/:mfcmd: and .. mfvar::/:mfvar:
def setup(app):
    app.add_object_type('subcmd', 'subcmd',
                        objname='module sub-command',
                        indextemplate='pair: %s; module sub-command',
                        parse_node=parse_cmd_args_node)
    app.add_object_type(directivename='mfcmd', rolename='mfcmd',
                        objname='modulefile command',
                        indextemplate='pair: %s; modulefile command',
                        parse_node=parse_cmd_args_node)
    app.add_object_type(directivename='mfvar', rolename='mfvar',
                        objname='modulefile variable',
                        indextemplate='pair: %s; modulefile variable',
                        parse_node=parse_cmd_args_node)
    app.add_object_type('instopt', 'instopt',
                        objname='installation option',
                        indextemplate='pair: %s; installation option',
                        parse_node=parse_opt_args_node)
    app.add_object_type('mconfig', 'mconfig',
                        objname='module configuration option',
                        indextemplate='pair: %s; module configuration option')

