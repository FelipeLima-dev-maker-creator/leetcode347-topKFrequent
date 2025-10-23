class Solution(object):
    def topKFrequent(self, nums, k):
        contador = {}
        for n in nums:
            if n not in contador:
                contador[n] = 0
            contador[n] += 1
        pares = []
        for chave in contador:
            pares.append((chave, contador[chave]))

        for i in range(len(pares)):
            for j in range(i + 1, len(pares)):
                if pares[j][1] > pares[i][1]:
                    pares[j], pares[i] = pares[i], pares[j]

        resultado = []
        for i in range(k):
            resultado.append(pares[i][0])
        return resultado


s = Solution()
print(s.topKFrequent([4,5,1,65,4,2,2,2,2,1], 3))
