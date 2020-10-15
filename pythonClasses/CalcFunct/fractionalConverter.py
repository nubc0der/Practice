class fractionalConverter:

    @staticmethod
    def initalStart(augend, addend = None):
        if isinstance(augend, list):
            return fractionalConverter.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(valueList):
        result = 0
        for value in valueList:
            result = fractionalConverter.sum(result, value)
        return result