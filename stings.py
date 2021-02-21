from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter_thing = Counter(ar)
    dicty = dict(counter_thing)
    valuelist = list(dicty.values())
    count = 0
    for item in valuelist:
        count += item//2
    print(count)
    #Idea in these types of problems is to get the 
    # number of values in the form of 
    # the dictionary and iterate it over and over again
    
if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    sockMerchant(n, ar)

