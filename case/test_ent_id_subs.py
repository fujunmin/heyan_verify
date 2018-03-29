#! /usr/bin/python#! coding=UTF-8import sysfrom gevent import sleepreload(sys)import osBASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))sys.path.append(BASE_DIR)# print 'ffffmmmmm:',BASE_DIRimport requestsimport unittestimport jsonfrom business.riskbell.test.unittest_flv4.case.interfacev4 import LoginAPI_v4# from interfacev4 import LoginAPI_v4# subs_import_interface = LoginAPI_v4(configuration.env)class TestEntIdSubs(unittest.TestCase):    @classmethod    def setUpClass(cls):        cls.LoginAPI_v4 = LoginAPI_v4()    def test_ent_id_subs(self):        token = json.loads(self.LoginAPI_v4.login().content)['token']        entId = '150000\u000117c9a2cb-0146-1000-e147-19f77f000001\u00011949100100000011813619'        ent_type = "2"        res_ent_id_subs = self.LoginAPI_v4.ent_id_subs(entId,ent_type,token)        expect_keys = ['created', 'not_found', 'exists']        expect_inside_keys = ['keyword', 'sub_id', 'ent_name']        self.assertEqual(res_ent_id_subs.status_code,200)        actual_res_keys = json.loads(res_ent_id_subs.content).keys()        self.assertItemsEqual(actual_res_keys,expect_keys)        if json.loads(res_ent_id_subs.content)['created']:            created_keys = json.loads(res_ent_id_subs.content)['created'][0].keys()            self.assertItemsEqual(created_keys, expect_inside_keys)        elif json.loads(res_ent_id_subs.content)['exists']:            sub_id = json.loads(res_ent_id_subs.content)['exists'][0]['sub_id']            res_remove = self.LoginAPI_v4.remove_subs(sub_id,token)            sleep(3)            self.assertEqual(res_remove.status_code,200)            res_ent_id_subs2 = self.LoginAPI_v4.ent_id_subs(entId,ent_type,token)            actual_inside_keys = json.loads(res_ent_id_subs2.content)['created'][0].keys()            self.assertItemsEqual(actual_inside_keys, expect_inside_keys)            self.assertEqual(json.loads(res_ent_id_subs2.content)['created'][0]['keyword'],entId)if __name__=='__main__':    unittest.main(verbosity=2)    # test_suit = unittest.TestSuite()    # test_suit.addTest(Login('test_login'))