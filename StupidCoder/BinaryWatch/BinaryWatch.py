class Solution:

    HH = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': '10',
        '1011': '11'
    }

    MM = {
        '000000': '00',
        '000001': '01',
        '000010': '02',
        '000011': '03',
        '000100': '04',
        '000101': '05',
        '000110': '06',
        '000111': '07',
        '001000': '08',
        '001001': '09',
        '001010': '10',
        '001011': '11',
        '001100': '12',
        '001101': '13',
        '001110': '14',
        '001111': '15',
        '010000': '16',
        '010001': '17',
        '010010': '18',
        '010011': '19',
        '010100': '20',
        '010101': '21',
        '010110': '22',
        '010111': '23',
        '011000': '24',
        '011001': '25',
        '011010': '26',
        '011011': '27',
        '011100': '28',
        '011101': '29',
        '011110': '30',
        '011111': '31',
        '100000': '32',
        '100001': '33',
        '100010': '34',
        '100011': '35',
        '100100': '36',
        '100101': '37',
        '100110': '38',
        '100111': '39',
        '101000': '40',
        '101001': '41',
        '101010': '42',
        '101011': '43',
        '101100': '44',
        '101101': '45',
        '101110': '46',
        '101111': '47',
        '110000': '48',
        '110001': '49',
        '110010': '50',
        '110011': '51',
        '110100': '52',
        '110101': '53',
        '110110': '54',
        '110111': '55',
        '111000': '56',
        '111001': '57',
        '111010': '58',
        '111011': '59',
    }

    result = list()

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8:
            return []
        self.result = list()
        self.findConfig(num, 0, ['0']*10)
        return self.result


    def findConfig(self, n, i, A):
        """

        configure A[i:] for n candidates

        :type n: int
        :type i: int
        :type A: List
        """

        if len(A) - i == n:
            for index in range(i, len(A), 1):
                A[index] = '1'
            self.validateConfig(A)
            for index in range(i, len(A), 1):
                A[index] = '0'
            return

        if n == 1:
            for index in range(i, len(A), 1):
                A[index] = '1'
                self.validateConfig(A)
                A[index] = '0'
            return

        self.findConfig(n, i+1, A)
        A[i] = '1'
        self.findConfig(n-1, i+1, A)
        A[i] = '0'


    def validateConfig(self, A):
        HH = A[:4]
        MM = A[4:]
        if ''.join(HH) in self.HH:
            oneresult = self.HH[''.join(HH)]
            if ''.join(MM) in self.MM:
                oneresult = oneresult + ':' + self.MM[''.join(MM)]
                self.result.append(oneresult)


s = Solution()
print(s.readBinaryWatch(8))
