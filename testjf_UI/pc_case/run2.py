import os
import unittest

import self as self

from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger


class AllTest:

    def set_case_list(self):
        """
        set pc_case list
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(hhh):
        """
        set pc_case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                resultPath = logger.get_report_path ()
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                logger.info("Have no pc_case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")

            # send test report by email



if __name__ == '__main__':
    obj = AllTest()
    obj.run()
