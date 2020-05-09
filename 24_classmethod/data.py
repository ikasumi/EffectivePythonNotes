# 共通クラス
class InputData(object):
    def read(self):
        raise NotImprementedError

# 具体的なサブクラス
class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


# 共通クラス
class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImprementedError

    def reduce(self):
        raise NotImprementedError

# 具体的なサブクラス
class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result