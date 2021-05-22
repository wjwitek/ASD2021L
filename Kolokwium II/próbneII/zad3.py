"""
f(i, j, l) - minimalny czas czekania przy wybraniu l prac od i do j włącznie
"""


class Job:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end

    def __str__(self):
        return "( " + str(self.start) + " - " + str(self.end) + " )"


def impatientBobby(J,n,k):
    #tu umiesc implementacje
    pass


J = [Job(1,2),Job(2,3)]
k = 2
print(impatientBobby(J,len(J),k))

if __name__ == "__main__":
    from zad3testy import runtests
    runtests(impatientBobby)
