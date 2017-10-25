import PyICU
from postaggerTC import Tagger

SEPARATER = " "
def wordsegmeter(text):

    def isThai(chr):
        cVal = ord(chr)
        if (cVal >= 3584 and cVal <= 3711):
            return True
        return False

    def segmenter(text):
        bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
        bd.setText(text)
        lastPos = bd.first()
        retText = ""
        try:
            while(True):
                currentPos = next(bd)
                retText += text[lastPos:currentPos]
                if (isThai(text[currentPos - 1])):
                    if (currentPos < len(text)):
                        if (isThai(text[currentPos])):
                            # Separater
                            retText += SEPARATER
                lastPos = currentPos
        except StopIteration:
            pass
        return retText
    return segmenter(text)


print(wordsegmeter("ผมหิวข้าว"))