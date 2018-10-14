text = "We choose to go to the Moon. " \
       "We choose to go to the Moon in this decade and do the other things. " \
       "Not because they are easy, but because they are hard. " \
       "Because that goal will serve to organize and measure the best of our energies and skills. " \
       "Because that challenge is one that we are willing to accept. " \
       "One we are unwilling to postpone. And one we intend to win"

# test=zdanie.split(".")
# test1=len(test)
# print(test1)

ile_zdan = 0
ile_slow = 0
ile_znakow = 0
wynik = list()

for zdanie in text.split("."):
    ile_znakow = len(zdanie)
    print(zdanie)
    slowa_w_zdaniu = zdanie.split(' ')
    print(slowa_w_zdaniu)
    ile_slow=len(slowa_w_zdaniu)
    print(ile_slow)
    # len(zdanie)
    # print(ile_wyrazow)
    wynik.append({zdanie: ile_slow})
    # DICT = [zdanie, ile_wyrazow]

    ile_zdan += 1
    ile_slow += ile_slow
    ile_znakow += ile_znakow

print(wynik)
print(f"Zdan w sumie bylo: {ile_zdan}")
print(f"Slow w sumie bylo: {ile_slow}")
print(f"Znakow w sumie bylo: {ile_znakow}")

# rozwiazanie
# TEXT = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'
#
# wynik = list()
#
# for sentence in TEXT.split('.'):
#     sentence = sentence.strip()
#     words = sentence.split(' ')
#     count = len(words)
#     wynik.append({sentence: count})
#
# from pprint import pprint
#
# pprint(wynik)
