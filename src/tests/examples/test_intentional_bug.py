import unittest

from turing_machine_tutor.examples.intentional_bug import intentional_bug


class TestIntentionalBug(unittest.TestCase):
    def test_intentional_bug_on(self):
        passed = [False]

        @intentional_bug(activated=True)
        def this_bug_is_active():
            passed[0] = True

        self.assertTrue(passed[0])

    def test_intentional_bug_off(self):
        @intentional_bug(activated=False)
        def this_bug_is_inactive():
            self.fail()


if __name__ == '__main__':
    unittest.main()
