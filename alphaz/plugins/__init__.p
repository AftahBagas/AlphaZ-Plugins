# alfareza

__all__ = ['ROOT', 'get_all_plugins']

import sys
from os.path import dirname
from typing import List

from alphaz import logging
from alphaz.utils import get_import_path

_LOG = logging.getLogger(__name__)
ROOT = dirname(__file__)


def get_all_plugins() -> List[str]:
    """ list all plugins """
    plugins = get_import_path(
        ROOT, "/dev/" if len(sys.argv) == 2 and sys.argv[1] == 'dev' else "/**/")
    _LOG.debug("All Available Plugins: %s", plugins)
    return list(plugins)
