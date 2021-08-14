import answer
import sys


def agent():
    wantsTOTalk = True
    while(wantsTOTalk):
        answer.answerMaker()
        if answer.isRunning==False:
            # wantsTOTalk = False
            break
            sys.exit()
