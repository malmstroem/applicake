"""Test workflows."""
import unittest
import sys
import os
import tempfile
import shutil

from appliapps.examples.cp import CpApp
from appliapps.examples.echowrapped import EchoWrapped
from appliapps.flow.branch import Branch
from appliapps.flow.collate import Collate
from appliapps.flow.merge import Merge
from appliapps.flow.split import Split
from appliapps.flow.jobid import Jobid

MY_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MY_PATH + '/../')


class Test(unittest.TestCase):
    """Test workflows."""
    @classmethod
    def setUpClass(cls):
        cls.tdir = tempfile.mkdtemp(dir=".")
        os.chdir(cls.tdir)
        with open("input.ini", "w") as out_fh:
            out_fh.write("""
COMMENT = comm,ent
LOG_STORAGE = memory
LOG_LEVEL = DEBUG
FILE = test.txt""")
        open("test.txt", "w").write("""TESTTEXT""")

    @classmethod
    def test1_jobid(cls):
        """Test jobid."""
        sys.argv = ['--INPUT', 'input.ini', '--OUTPUT', 'jobid.ini']
        Jobid.main()
        assert os.path.exists('jobid.ini')
        assert 'JOB_ID' in open('jobid.ini', 'r').read()

    @classmethod
    def test2_branch(cls):
        """Test brancing."""
        sys.argv = ['--INPUT', 'jobid.ini', '--BRANCH', 'forcp.ini', '--BRANCH', 'forecho.ini',]
        Branch.main()

        assert os.path.exists('forcp.ini')
        assert os.path.exists('forecho.ini')

    @classmethod
    def test3_cp(cls):
        """Test copy."""
        sys.argv = ['--INPUT', 'forcp.ini', '--OUTPUT', 'cp.ini']
        CpApp.main()
        assert os.path.exists('cp.ini')
        assert 'COPY' in open('cp.ini', 'r').read()

    @classmethod
    def test4_split(cls):
        """Test split."""
        sys.argv = ['--INPUT', 'forecho.ini', '--SPLIT', 'split.ini', '--SPLIT_KEY', 'COMMENT']
        Split.main()

        assert os.path.exists('split.ini_0')
        assert 'comm' in open('split.ini_0', 'r').read()
        assert not 'ent' in open('split.ini_0', 'r').read()

        assert os.path.exists('split.ini_1')
        assert not 'comm' in open('split.ini_1', 'r').read()
        assert 'ent' in open('split.ini_1', 'r').read()

    @classmethod
    def test5_echo(cls):
        """Test echoing."""
        sys.argv = ['--INPUT', 'split.ini_0', '--OUTPUT', 'echo.ini_0']
        EchoWrapped.main()

        assert os.path.exists('echo.ini_0')

        sys.argv = ['--INPUT', 'split.ini_1', '--OUTPUT', 'echo.ini_1']
        EchoWrapped.main()

        os.path.exists('echo.ini_1')

    @classmethod
    def test6_merge(cls):
        """Test merging."""
        sys.argv = ['--MERGE', 'echo.ini', '--MERGED', 'merged.ini']
        Merge.main()
        assert os.path.exists('merged.ini_0')

    @classmethod
    def test7_collate(cls):
        """Test collate."""
        sys.argv = ['--COLLATE', 'cp.ini', '--COLLATE', 'merged.ini_0', '--OUTPUT', 'collate.ini']
        Collate.main()
        assert os.path.exists('collate.ini')

        print(open('collate.ini', 'r').read())
        assert 'comm, ent' in open('collate.ini', 'r').read()
        assert 'COPY' in open('collate.ini', 'r').read()

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        shutil.rmtree(cls.tdir)
