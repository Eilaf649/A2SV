class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans=[]
        kalvin= celsius+273.15
        ans.append(kalvin)
        Fahrenheit= celsius*1.80 +32.00
        ans.append(Fahrenheit)
        return ans
