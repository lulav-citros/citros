from unittest import TestCase

from tests.test_parse_makefile import *


class Test(TestCase):
    def test_test_px4_makefile(self):
        test_px4_makefile()

    def test_test_parse_makefile_no_install(self):
        test_parse_makefile_no_install()

    def test_test_micro_ros_agent_makefile(self):
        test_micro_ros_agent_makefile()
