**A progress extension for Sphinx (and Jupyter Book).**

This package contains a Sphinx extension for keeping the progress of a student in a Jupyter Book,
to be combined with (e.d.) de Sphinx assessments extension.

After the user logs in, the use of the assessment questions is logged (in a CouchDB database).

**This is an alpha-version, use at your own risk; interfaces may change**

## Get started

To get started with *sphinx_progress*, first install it through pip:

```
pip install git+https://github.com/eelcodijkstra/sphinx-progress.git
```

### Use in Jupyter Book

Add *sphinx_assessment* to the sphinx extensions in `_config.yml`:

```
sphinx:
  extra_extensions:
    - sphinx_progress
```

### Use in Sphinx

Add *sphinx_progress* to your sphinx extensions in `conf.py`

```
extensions = ["sphinx_progress"]
```

## Documentation

TBD.

The function `progress_log(obj)` stores the `obj` in de log-database, with extra data: datetime, user, book-title, page-title. (Chapter???)
