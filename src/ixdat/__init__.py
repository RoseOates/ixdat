"""initialize ixdat, giving top-level access to a few of the important structures
"""
__version__ = "0.2.4"
__title__ = "ixdat"
__description__ = "The in-situ experimental data tool"
__url__ = "https://ixdat.readthedocs.io"
__author__ = "Soren B. Scott, Kenneth Nielsen, et al"
__email__ = "sbscott@ic.ac.uk"  # maybe we should get an organization email?
__license__ = "MIT"

from .measurements import Measurement
from .spectra import Spectrum
from . import db
from . import techniques
from . import plotters
from . import exporters
from . import config
from .config import plugins

# I like this to be sure I'm importing from where I think I am:
print(f"importing ixdat v{__version__} from {__file__}")
