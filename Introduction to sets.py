# TC : O(n)
# SC : O(n)

def average(array):
    # your code goes here
    res = set(array)
    avg = sum(res)/len(res)
    final_avg = round(avg,3)
    return final_avg