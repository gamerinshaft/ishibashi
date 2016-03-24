# -*- coding: utf-8 -*-
import os, sys, unittest
from ishibashi import Ishibashi

class SampleTest(unittest.TestCase):
    """あるクラスをテストするテストクラス"""
    CLS_VAL = 'none'

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        if sys.flags.debug: print('> setUpClass method is called.')
        # テストの準備するための重い処理のメソッドを実行
        cls.CLS_VAL = '> setUpClass : initialized!'
        if sys.flags.debug: print(cls.CLS_VAL)

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        if sys.flags.debug: print('> tearDownClass method is called.')
        # setUpClassで準備したオブジェクトを解放する
        cls.CLS_VAL = '> tearDownClass : released!'
        if sys.flags.debug: print(cls.CLS_VAL)

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        if sys.flags.debug: print(os.linesep + '> setUp method is called.')
        # テストの準備をするための軽い処理を実行
        self.smpl = Ishibashi("bcm")

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        if sys.flags.debug: print(os.linesep + '> tearDown method is called.')
        # setUpで準備したオブジェクトを解放する
        self.smpl.finish()

    def test_hoge(self):
        test = self.smpl.should_be_high(20)
        self.assertTrue(test)

    def test_poyo(self):
        test = self.smpl.should_be_low(20)
        self.assertTrue(test)

if __name__ == '__main__':
    # unittestを実行
    unittest.main()
