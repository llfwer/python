import pandas


class DataWriter:

    def __init__(self, file):
        """
        :param file:保存文件名
        """
        self.file_name = file
        self.data = pandas.DataFrame()

    def column(self, name):
        """
        :param name:列名
        """
        self.data[name] = None

    def set(self, index, name, value):
        """
        :param index:索引
        :param name:列名
        :param value:值
        """
        self.data.loc[index, name] = value

    def save(self):
        self.data.to_excel(self.file_name, sheet_name='Sheet1', index=False, header=True)


class DataReader:

    def __init__(self, file):
        """
        :param file:文件名
        """
        self.data = pandas.read_excel(file)
        self.columns = self.data.columns.values.tolist()
        self.length = self.data.shape[0]

    def titles(self):
        return self.columns

    def len(self):
        return self.length

    def loc(self, index):
        return self.data.loc[index]

    def avg(self, column):
        """
        :param column: 列名
        :return: 平均值
        """
        if self.length <= 0:
            return 0

        summary = 0

        for i in range(self.length):
            item = self.data.loc[i]

            value = item.loc[column]
            summary += value

        return summary / self.length
