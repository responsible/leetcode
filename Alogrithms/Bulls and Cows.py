__author__ = 'responsible'
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        for index, item in enumerate(guess):
            pos = secret.find(item)
            if pos != -1:
                if secret[index] == item:
                    bull += 1
                    secret = secret[:index] + "*" + secret[index + 1:]
                elif secret[pos] == guess[pos]:
                    bull += 1
                    secret = secret[:pos] + "*" + secret[pos + 1:]
                else:
                    cow += 1
                    secret = secret[:secret.find(item)] + "*" + secret[secret.find(item) + 1:]
        return "%sA%sB" % (bull, cow)