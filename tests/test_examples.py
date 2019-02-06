"""Test examples."""
import unittest
import sys
from sys import platform as _platform
import os
import tempfile
import shutil


from appliapps.examples.echobasic import EchoBasic
from appliapps.examples.echowrapped import EchoWrapped
from appliapps.examples.cp import CpApp
from appliapps.examples.template import TemplateApp


class Test(unittest.TestCase):
    """Test examples."""

    @classmethod
    def setUpClass(cls):
        cls.tdir = tempfile.mkdtemp(dir=".")
        os.chdir(cls.tdir)
        with open("testfile", "w") as out_fh:
            out_fh.write("testcontent")

    @classmethod
    def test1_pyecho(cls):
        """Test pyecho."""
        sys.argv = ['--COMMENT', 'comment']
        EchoBasic.main()

    @classmethod
    def test2_extecho(cls):
        """Test wrapped app."""
        sys.argv = ['--COMMENT', 'comment']
        EchoWrapped.main()

    def test3_cp(self):
        """Test cp."""
        sys.argv = ["--FILE", "testfile"]
        if _platform == "linux":
            CpApp.main()
            os.chmod("testfile", 000)
            self.assertRaises(SystemExit, CpApp.main)
            os.chmod("testfile", 644)

    @classmethod
    def test4_tpl(cls):
        """Test templates."""
        sys.argv = ['--COMMENT', 'comment', '--WORKDIR', '.']
        TemplateApp.main()
        assert os.path.exists("template_out.tpl")

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        shutil.rmtree(cls.tdir)
