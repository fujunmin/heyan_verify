#! /usr/bin/python
#! coding=UTF-8
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)
print 'fffffmmmmmmmm:',BASE_DIR
reload(sys)
import unittest

# test_cases = (TestLogin, TestSubsList)
# def load_tests(loader, tests, pattern):
#     suite = unittest.TestSuite()
#     for test_class in test_cases:
#         tests = loader.loadTestsFromTestCase(test_class)
#         suite.addTests(tests)
#     return suite

# 用例路径 
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report/report.txt",)
print case_path
print report_path

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover


if __name__=='__main__':
    # 测试2
    # 此用法可以同时测试多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSubsList)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # report = '%s%s'%(report_path,'report.txt')
    # print report

    with open(report_path,'w+') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(all_case())
