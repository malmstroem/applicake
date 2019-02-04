import unittest
import sys
import os
import tempfile
import shutil
from sys import platform as _platform

from appliapps.examples.echobasic import EchoBasic
from appliapps.examples.echowrapped import EchoWrapped
from appliapps.examples.cp import CpApp
from appliapps.examples.template import TemplateApp


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tdir = tempfile.mkdtemp(dir=".")
        os.chdir(cls.tdir)
        with open("testfile", "w") as f:
            f.write("testcontent")

    def test1_pyecho(self):
        sys.argv = ['--COMMENT', 'comment']
        EchoBasic.main()

    def test2_extecho(self):
        sys.argv = ['--COMMENT', 'comment']
        EchoWrapped.main()

    def test3_cp(self):
        sys.argv = ["--FILE", "testfile"]
        if _platform == "linux":
            CpApp.main()
            os.chmod("testfile", 000)
            self.assertRaises(SystemExit, CpApp.main)
            os.chmod("testfile", 644)

    def test4_tpl(self):
        sys.argv = ['--COMMENT', 'comment', '--WORKDIR', '.']
        TemplateApp.main()
        assert os.path.exists("template_out.tpl")

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        shutil.rmtree(cls.tdir)
