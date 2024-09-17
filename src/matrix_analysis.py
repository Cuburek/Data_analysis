class MatrixAnalysis:
    @staticmethod
    def min(matrix: list[list[int]]) -> int:
        min_number = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < min_number:
                    min_number = matrix[i][j]
        return min_number

    @staticmethod
    def max(matrix: list[list[int]]) -> int:
        max_number = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > max_number:
                    max_number = matrix[i][j]
        return max_number

    # @staticmethod
    # def sum (matrix: list[list[int]]):
    #     matrix_sum = 0
    #     for i in matrix:
    #         for element in i:
    #             matrix_sum += element
    #     return matrix_sum

    @staticmethod
    def sum(matrix: list[list[int]]) -> int:
        matrix_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix_sum += matrix[i][j]
        return matrix_sum

    @staticmethod
    def mod(matrix: list[list[int]]):
        numbers_count = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                numbers_count[matrix[i][j]] = numbers_count.get(matrix[i][j], 0) + 1
        frequent_number = matrix[0][0]
        max_count = 0
        for number, count in numbers_count.items():
            if count > max_count:
                frequent_number = number
                max_count = count

        return frequent_number

