#! /usr/bin/python#! coding=UTF-8import jsonimport osimport sysimport unittestBASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))sys.path.append(BASE_DIR)from business.riskbell.test.unittest_flv4.case.interfacev4 import LoginAPI_v4class TestInactiveSub(unittest.TestCase):    @classmethod    def setUpClass(cls):        cls.LoginAPI_v4 = LoginAPI_v4()    # 默认入参：count:true;per_page:10;page:1;sort:-created_at    def test_inactive_subs1(self):        print 'test_inactive_subs1'        token = json.loads(self.LoginAPI_v4.login().content)['token']        per_page = 50        res_subsList = self.LoginAPI_v4.subs_list(per_page=per_page,token=token)        self.assertEqual(res_subsList.status_code, 200)        self.assertIsNotNone(res_subsList.content)        active_sub_id = []        for i in range(0,per_page):            sub_id = json.loads(res_subsList.content)[i]['sub_id']            status = json.loads(res_subsList.content)[i]['status']            if status == 'ACTIVE':                active_sub_id.append(sub_id)                break            else:                continue        res_inactive = self.LoginAPI_v4.inactive_subs(active_sub_id[0],token)        expect_keys = u'INACTIVE'        actual_res_keys = json.loads(res_inactive.content)['status']        self.assertEqual(actual_res_keys,expect_keys)        # self.assertItemsEqual(actual_res_keys,expect_keys)        # # 已暂停的订阅再次暂停，返回701        # res_inactive2 = self.LoginAPI_v4.inactive_subs(active_sub_id[0],token)        # self.assertEqual(res_inactive2.status_code,400)        # self.assertEqual(json.loads(res_inactive2.content)['code'],701)        # self.assertEqual(json.loads(res_inactive2.content)['message'],u'错误的请求数据')if __name__=='__main__':    unittest.main(verbosity=2)