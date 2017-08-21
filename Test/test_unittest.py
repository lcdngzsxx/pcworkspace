import unittest
from demo.unittest_demo import get_formatted_name #引入方法

class NameTestCast(unittest.TestCase):
    def test_title_name(self):
        format_name = get_formatted_name('li','kui')
        self.assertEqual(format_name,'Li Kui')#assert断言是否相等

if __name__ == "__main__":#如果运行的是当前文件
    unittest.main()