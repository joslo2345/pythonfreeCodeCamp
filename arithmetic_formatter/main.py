import arithmetic_arranger as ari_arr

if __name__ == '__main__':
    result1 = ari_arr.arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
    #result1 = ari_arr.arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    print(result1)

    result2 = ari_arr.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)
    #result2 = ari_arr.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
    print(result2)