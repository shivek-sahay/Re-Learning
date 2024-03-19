str_arr = []
def main(str_arr):
    n = len(str_arr)
    common = str_arr[0]
    for i in range(n):
        common = findCommon(common, str_arr[i])
    
    return common

def findCommon(str1, str2):
    n = len(str1)
    m = len(str2)
    common_str = ''
    for i in range(min(n,m)):
        if str1[i] == str2[i]:
            common_str += str1[i]
        else:
            break
    return common_str
print(main(str_arr))