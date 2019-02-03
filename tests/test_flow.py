import unittest
import sys
import os
import tempfile
import shutil
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from applicake.apps.flow.branch import Branch
from applicake.apps.flow.collate import Collate
from applicake.apps.flow.merge import Merge
from applicake.apps.flow.split import Split


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tdir = tempfile.mkdtemp(dir=".")
        os.chdir(cls.tdir)
        with open("input.ini", "w") as f:
            f.write("""COMMENT = comm,ent
SOMEKEY = some, key
LOG_LEVEL = INFO
LOG_STORAGE = memory""")

    def test1_branch(self):
        sys.argv = ['--INPUT', 'input.ini', '--BRANCH', 'tandem.ini', 'omssa.ini', '--COMMENT', 'kommentar']
        Branch.main()
        assert os.path.exists('tandem.ini')
        assert os.path.exists('omssa.ini')

    def test2_collate(self):
        sys.argv = ['--COLLATE', 'tandem.ini', 'omssa.ini', '--OUTPUT', 'collate.ini']
        Collate.main()
        assert os.path.exists('collate.ini')

    def test3_split(self):
        sys.argv = ['--INPUT', 'input.ini', '--SPLIT', 'split.ini', '--SPLIT_KEY', 'SOMEKEY']
        Split.main()

        assert os.path.exists('split.ini_0')
        assert os.path.exists('split.ini_1')

    def test4_merge(self):
        sys.argv = ['--MERGE', 'split.ini', '--MERGED', 'merged.ini']
        Merge.main()
        assert os.path.exists('merged.ini_0')

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        shutil.rmtree(cls.tdir)
