import unittest
from oop.Coder import Coder


class CoderTestCase(unittest.TestCase):
    '''初始化数据,重写setUp'''

    def setUp(self):
        self.c = Coder('Tom')
        self.c.skills = ['java' , 'python' , 'axure']

    def test_skill_in(self):
        # c = Coder ( 'Tom' )
        # c.mastering_skill ( 'java' )
        # c.mastering_skill ( 'python' )
        # c.skills.append ( 'axure' )
        # self.assertIn ( 'java' , c.skills )
        self.assert_in = self.assertIn('axure' , self.c.skills)


'''如果运行的文件是当前文件:注释用三引号'''
if __name__ == '__main__':
    unittest.main()
