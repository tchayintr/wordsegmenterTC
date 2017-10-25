import PyICU

SEPARATER = " "
class Segmenter:

    def isThai(self, chr):
        cVal = ord(chr)
        if (cVal >= 3584 and cVal <= 3711):
            return True
        return False

    def segment(self, text):
        bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
        bd.setText(text)
        lastPos = bd.first()
        retText = ""
        try:
            while(True):
                currentPos = next(bd)
                retText += text[lastPos:currentPos]
                if (self.isThai(text[currentPos - 1])):
                    if (currentPos < len(text)):
                        if (self.isThai(text[currentPos])):
                            # Separater
                            retText += SEPARATER
                lastPos = currentPos
        except StopIteration:
            pass
        return retText




