"""
Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewienciągnliter oraz
liczbę k i wypisuje najczęściej powtarzający się podciąg długościk(jeśli ciągówmogących stanowić rozwiązanie jest kilka,
algorytm zwraca dowolny z nich). Można założyć, żeciąg składa się wyłącznie z literaib.Na przykład dla ciągu ababaaaabborazk= 3
rozwiązaniem jest zarówno ciągaba, którypowtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność
"""
# translate to array where a is 0 and b is 1
# create array with all possible sub arrays of length k and then for each subarray of length k
# from original array add +1 to correct place in array of subs
# find biggest counter and transcribe from decimal (index) to a and b
