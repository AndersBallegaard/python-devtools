#!/usr/bin/python3
import pydevtools
import unittest

class Test_get_calls(unittest.TestCase):
    
    def test_no_args_output(self):
        os = None
        def set_os(self,s):
            '''
            An output function to set the output string for analysis
            '''
            self.os = s

        @pydevtools.debug.get_calls(set_os)
        def fn_1(self):
            '''
            no args dummy function
            '''
            pass
            self.fn_1()
        
        self.assertEqual(os,"function: test_no_args_output args: () kwargs: {}")

if __name__ == '__main__':
    print("debug tests")
    unittest.main()