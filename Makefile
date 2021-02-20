# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# If you want to use "make view", please edit them.
NGINXTEMPDIR  = /home/f_qilin/Nginx/dir/html/varcade/vabl-temp
NGINXTEMPHTTP = http://127.0.0.1/varcade/vabl-temp

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile view clean

# localhost
view:
	@make html
	@-rm -r "$(NGINXTEMPDIR)"
	@cp -r "$(BUILDDIR)/html" "$(NGINXTEMPDIR)"
	@echo "Complete! Please view <$(NGINXTEMPHTTP)>."

clean:
	@-rm -r "$(BUILDDIR)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
