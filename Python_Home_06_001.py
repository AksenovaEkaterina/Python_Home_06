# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

def find (str_eq):
    list_opr = ['+','-','*','/','(',')']
    list_var = []
    str_var =''
    for el in str_eq:
        if el not in list_opr:
            str_var += el
        else:
            list_var.append(int(str_var))
            str_var=''
            list_var.append(el)
    list_var.append(int(str_var))
    return(list_var)


def rec (list_var): #возвращаем массив в скобках
    new_r = []
    for i in range(0,len(list_var)):
        if list_var[i] == "(":
          while list_var[i+1]!=')':
           new_r.append (list_var[i+1])
           i+=1
    return(new_r)
def rec2(list_var, new_r):  # массив в скобках заменяем на результат после его вычисления
   new_r2 = []
   for i in range(0,len(list_var)):
      new_r2.append(list_var[i])
      if list_var[i] == "(":
        new_r2.append(new_r)
        break
      return (new_r2)

def make_arif_solution (list_var):
    i=0
    result_equ = 0
    while ('*'in list_var)or('/'in list_var):
        if list_var[i]=='*':
             result_equ += list_var[i+1]*list_var[i-1]
             list_var[i+1] = result_equ
             del list_var[i-1:i+1]
             i = 0
             result_equ = 0
        elif list_var[i]=='/':
             result_equ += list_var[i+1]/list_var[i-1]
             list_var[i+1] = result_equ
             del list_var[i-1:i+1]
             i = 0
             result_equ = 0
        else: i+=1
    while ('+'in list_var)or('-'in list_var):
        if list_var[i]=='+':
             result_equ += list_var[i+1]*list_var[i-1]
             list_var[i+1] = result_equ
             del list_var[i-1:i+1]
             i = 0
             result_equ = 0
        elif list_var[i]=='-':
             result_equ += list_var[i+1]/list_var[i-1]
             list_var[i+1] = result_equ
             del list_var[i-1:i+1]
             i = 0
             result_equ = 0
        else: i+=1
    result_equ=list_var
    return result_equ


str_eq= 3+2(4*5)

print (rec(find(str_eq)))
print (make_arif_solution(rec(find(str_eq))))
print (rec2(find (str_eq),(make_arif_solution(rec(find(str_eq))))))
print (make_arif_solution(rec2(find (str_eq),(make_arif_solution(rec(find(str_eq)))))))