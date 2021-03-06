from easyprocess import EasyProcess
from easyprocess import extract_version
from PIL import Image
import tempfile
from pyscreenshot.iplugin import IPlugin


PROGRAM = 'scrot'
URL = None
PACKAGE = 'scrot'


class ScrotWrapper(IPlugin):
    name = 'scrot'
    childprocess = True

    def __init__(self):
        EasyProcess([PROGRAM, '-version'], url=URL,
                    ubuntu_package=PACKAGE).check_installed()

    def grab(self, bbox=None):
        f = tempfile.NamedTemporaryFile(
            suffix='.png', prefix='pyscreenshot_scrot_')
        filename = f.name
        self.grab_to_file(filename)
        im = Image.open(filename)
        if bbox:
            im = im.crop(bbox)
        return im

    def grab_to_file(self, filename):
        EasyProcess([PROGRAM, filename]).call()

    def backend_version(self):
        return extract_version(EasyProcess([PROGRAM, '-version']).call().stdout)
