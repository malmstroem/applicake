"""Test flow apps."""
import unittest
import sys
import os
import tempfile
import shutil

from appliapps.flow.branch import Branch
from appliapps.flow.collate import Collate
from appliapps.flow.merge import Merge
from appliapps.flow.split import Split

MY_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MY_PATH + '/../')


class Test(unittest.TestCase):
    """Test flow apps."""
    @classmethod
    def setUpClass(cls):
        cls.tdir = tempfile.mkdtemp(dir=".")
        os.chdir(cls.tdir)
        with open("input.ini", "w") as out_fh:
            out_fh.write("""COMMENT = comm,ent
SOMEKEY = some, key
LOG_LEVEL = INFO
LOG_STORAGE = memory""")

    @classmethod
    def test1_branch(cls):
        """Test branching."""
        sys.argv = ['--INPUT', 'input.ini', '--BRANCH',
                    'tandem.ini', 'omssa.ini', '--COMMENT', 'kommentar']
        Branch.main()
        assert os.path.exists('tandem.ini')
        assert os.path.exists('omssa.ini')

    @classmethod
    def test2_collate(cls):
        """Test collate."""
        sys.argv = ['--COLLATE', 'tandem.ini', 'omssa.ini', '--OUTPUT', 'collate.ini']
        Collate.main()
        assert os.path.exists('collate.ini')

    @classmethod
    def test3_split(cls):
        """Test split."""
        sys.argv = ['--INPUT', 'input.ini', '--SPLIT', 'split.ini', '--SPLIT_KEY', 'SOMEKEY']
        Split.main()

        assert os.path.exists('split.ini_0')
        assert os.path.exists('split.ini_1')

    @classmethod
    def test4_merge(cls):
        """Test merge."""
        sys.argv = ['--MERGE', 'split.ini', '--MERGED', 'merged.ini']
        Merge.main()
        assert os.path.exists('merged.ini_0')

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        shutil.rmtree(cls.tdir)
