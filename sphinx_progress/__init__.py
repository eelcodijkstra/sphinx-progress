from pathlib import Path

from sphinx.util import logging
from sphinx.util.fileutil import copy_asset

logger = logging.getLogger(__name__)


def copy_asset_files(app, exc):
    """ Copies required assets for formating in HTML """

    static_path_css = (
        Path(__file__).parent.joinpath("assets", "css", "assessment.css").absolute()
    )
    static_path_js = (
        Path(__file__).parent.joinpath("assets", "js", "assessment.js").absolute()
    )
    asset_files = [str(static_path_css), str(static_path_js)]

    if exc is None:
        for path in asset_files:
            logger.info("copy: " + str(path))
            logger.info("..to: " + str(Path(app.outdir).joinpath("_static").absolute()))
            copy_asset(path, str(Path(app.outdir).joinpath("_static").absolute()))


def setup(app):

    app.connect("build-finished", copy_asset_files)  # event order - 16

    app.add_css_file("progress.css")
    app.add_js_file("progress.js")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

