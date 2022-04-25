from turtle import right
import arithmetic_arranger as ari_arr

right_answer = '''   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
'''
operations_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
results = True


def get_result(operations,results):
    output = ari_arr.arithmetic_arranger(operations,results)
    return output

def test_output():
    assert get_result(operations_list,results) == right_answer