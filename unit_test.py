# -*- coding: utf-8 -*-
import os, sys, unittest
from ishibashi import Ishibashi
from logging import getLogger,StreamHandler
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(sys.flags.debug)
logger.setLevel(sys.flags.debug)
logger.addHandler(handler)

class ModuleTest(unittest.TestCase):
    """Module Test"""
    CLS_VAL = 'none'

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def setUpClass(cls):
        logger.debug('> setUpClass method is called.')
        # テストの準備するための重い処理のメソッドを実行
        cls.CLS_VAL = '> setUpClass : initialized!'
        logger.debug(cls.CLS_VAL)

    # テストクラスが解放される際に一度だけ呼ばれる (python2.7以上)
    @classmethod
    def tearDownClass(cls):
        logger.debug('> tearDownClass method is called.')
        # setUpClassで準備したオブジェクトを解放する
        cls.CLS_VAL = '> tearDownClass : released!'
        logger.debug(cls.CLS_VAL)

    # テストメソッドを実行するたびに呼ばれる
    def setUp(self):
        logger.debug(os.linesep + '> setUp method is called.')
        # テストの準備をするための軽い処理を実行
        self.ishibashi = Ishibashi("bcm")

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        logger.debug(os.linesep + '> tearDown method is called.')
        # setUpで準備したオブジェクトを解放する
        self.ishibashi.finish()

    #=============================================================================
    def test_signal_on(self):
        test = self.ishibashi.should_be_low(12)
        self.assertTrue(test)
        self.ishibashi.pin_on(20)
        test = self.ishibashi.should_be_high(12)
        self.assertTrue(test)


    # def test_single_pin_state_high(self):
    #     test = self.ishibashi.should_be_high(20)
    #     self.assertTrue(test)

    # def test_single_pin_state_low(self):
    #     test = self.ishibashi.should_be_low(21)
    #     self.assertTrue(test)

    # def test_all_pin_state_high(self):
    #     test = self.ishibashi.all_should_be_high(12, 20)
    #     self.assertTrue(test)

    # def test_all_pin_state_low(self):
    #     test = self.ishibashi.all_should_be_low(16,21)
    #     self.assertTrue(test)

    # def test_detect_high_edge(self):
    #     test = self.ishibashi.detect_high_edge(20, 1000)
    #     self.assertTrue(test)

    # def test_detect_low_edge(self):
    #     test = self.ishibashi.detect_low_edge(20, 1000)
    #     self.assertTrue(test)

    # def test_detect_high_or_low_edge(self):
    #     test = self.ishibashi.detect_high_or_low_edge(20, 1000)
    #     self.assertTrue(test)

if __name__ == '__main__':
    # unittestを実行
    unittest.main()
