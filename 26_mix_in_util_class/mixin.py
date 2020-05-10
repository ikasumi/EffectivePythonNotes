
"""
多重継承は避けたほうが懸命
多重継承による簡便さとカプセル化が望ましい場合、代わりに mix-in を書く

mix-in はクラスが提供すべき一連の追加メソッドを定義するだけの小さなクラス
min-in はコードの繰り返しを最小化してシア利用を最大化するように組み合わせて層別に作ることができる

例：Python のオブジェクトをメモリ内の表現からシリアライズできる辞書表現に変換する機能
　　をすべてのクラスに使えるようなジェネリックな機能として実装
"""

class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse_dict(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

# この mix-in を使って二分木の辞書表現を作るクラスの例
class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
from pprint import pprint
pprint(tree.to_dict())
"""
{'left': {'left': None,
          'right': {'left': None, 'right': None, 'value': 9},
          'value': 7},
 'right': {'left': {'left': None, 'right': None, 'value': 11},
           'right': None,
           'value': 13},
 'value': 10}
"""

# mix-in の良いところ
# - ジェネリックな機能がプラグイン可能になり、必要なときに振る舞いをオーバーライド可能