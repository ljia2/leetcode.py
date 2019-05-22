class Solution(object):
    def isNumber(self, s):
        """
        Validate if a given string can be interpreted as a decimal number.

        Some examples:
        "0" => true
        " 0.1 " => true
        "abc" => false
        "1 a" => false
        "2e10" => true
        " -90e3   " => true
        " 1e" => false
        "e3" => false
        " 6e-1" => true
        " 99e2.5 " => false
        "53.5e93" => true
        " --6 " => false
        "-+3" => false
        "95a54e53" => false

        Note: It is intended for the problem statement to be ambiguous.
        You should gather all requirements up front before implementing one.
        However, here is a list of characters that can be in a valid decimal number:

        Numbers 0-9
        Exponent - "e"
        Positive/negative sign - "+"/"-"
        Decimal point - "."
        Of course, the context of these characters also matters in the input.

        Update (2015-02-10):
        The signature of the C++ function had been updated.
        If you still see your function signature accepts a const char * argument,
        please click the reload button to reset your code definition.
        
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        numbersSeen = False
        pointSeen = False
        eSeen = False
        # set numberAfterE is initialized to True
        # When E is encourtered, set numberAfterE = False
        # when numbers are encourtered after "e", reset numberAfterE = True
        numberAfterE = True
        n = len(s)
        for i in range(n):
            if '0' <= s[i] <= '9':
                numbersSeen = True
                numberAfterE = True
            elif s[i] == '.':
                # there must be only one point and before "e" if any
                # if there are e before or multiple point, return False invalid.
                if eSeen or pointSeen:
                    return False
                else:
                    pointSeen = True
            elif s[i] == 'e':
                # there must be only one "e"
                # if there are multiple "e" or no numbers before e, return False (invalid)
                if eSeen or not numbersSeen:
                    return False
                # set this false, and reset to True when a number after E is encourtered.
                numberAfterE = False
                eSeen = True
            elif s[i] == '+' or s[i] == '-':
                # must be sign or sign after "e"
                if i != 0 or s[i-1] != 'e':
                    return False
            else:
                return False

        return numbersSeen and numberAfterE



