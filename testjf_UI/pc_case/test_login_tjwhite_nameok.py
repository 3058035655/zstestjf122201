#-*- coding:utf-8 -*-
import unittest
import time
import sys

from testjf_UI.common.blackwhiteuserpage import BlackWhitepage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf_UI.common.loginpage import LoginPage

class Test_Tjwhitename (unittest.TestCase):
    excel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page = BlackWhitepage ()
                driver = login_page.driver
                # Step3: 输入用户名
                login_page.set_admin ("yradmin")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                time.sleep (6)
                # Step5: 单击登录按钮
                login_page.click_login ()
                # time.sleep(1)
                login_page.click_xtgl ()
                time.sleep (0.5)
                login_page.click_yhgnmd ()
                time.sleep (0.5)
                driver.switch_to_frame ("contentIframe")
                login_page.click_tianjia()
                login_page.set_tel(int(d['login']))
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[2].click ();  #债券转让
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[4].click ();  # 新手标投资
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[5].click ();  # 销售
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[6].click ();  # 内部员工
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[8].click ();  # 充值
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[10].click ();  # 钱袋子内部员工推荐奖励
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[7].click ();  # 钱袋子转入转出
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[9].click ();  # 物业员工
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[12].click ();  # 物业现金缴费黑名单
                driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[13].click ();  # 用户投资

                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[14].click ();  # 提现放款白名单
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[15].click ();  # 用户提现黑名单
                # driver.find_element_by_id ("type").find_elements_by_tag_name ("option")[16].click ();  # 借款人查看合同白名单

                # <option value="1">积分转余额</option>
                # <option value="2">债权转让</option>
                # <option value="3">活动邀请投资1万元奖励88元</option>
                # <option value="4">新手标投资</option>
                # <option value="5">销售</option>
                # <option value="6">内部员工</option>
                # <option value="8">充值</option>
                # <option value="10">钱袋子内部员工推荐奖励</option>
                # <option value="7">钱袋子转入转出</option>
                # <option value="9">物业员工</option>
                # <option value="11">美分期发送红包</option>
                # <option value="12">物业现金缴费黑名单</option>
                # <option value="13">用户投资</option>
                # <option value="14">提现放款白名单</option>
                # <option value="15">用户提现黑名单</option>
                # <option value="16">借款人查看合同白名单</option>
                #driver.find_element_by_id ("isyn").find_elements_by_tag_name ("option")[0].click ();  # 黑名单
                driver.find_element_by_id ("isyn").find_elements_by_tag_name ("option")[1].click ();  # 白名单
                login_page.click_save()
                login_page.driver.close()
if __name__ == '__main__':
    unittest.main ()
