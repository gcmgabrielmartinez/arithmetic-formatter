def arithmetic_arranger(problems, result = False):
  if len(problems) > 5 :  
    return "Error: Too many problems."
  
  up = list()
  op = list()
  down = list()
  ans = list()
  
  #splitting components
  for problem in problems:
    args = problem.split()
    
    #validating equations
    flag = validate(*args)
    #print(flag)
    if flag == 1:
      return "Error: Operator must be '+' or '-'."
    elif flag == 2:
      return "Error: Numbers must only contain digits."
    elif flag == 3:
      return "Error: Numbers cannot be more than four digits."
    
    else:  
      up.append(args[0])
      op.append(args[1])
      down.append(args[2])
      ans.append(get_result(*args))
  
  #print(up)
  #return up, op, down, ans

  #printing problems
  arranged_problems = get_string(up, op, down, ans, result)

  return arranged_problems

def get_result(up, op, down):
  if op == "+" : 
    return str(int(up) + int(down))
  elif op == "-" : 
    return str(int(up) - int(down))

def validate(up, op, down):
  if op not in ["+", "-"]:
    return 1

  try:
    if int(up) > 9999 or int(up) < -9999 :
      return 3
    if int(down) > 9999 or int(down) < -9999:
      return 3
    
  except ValueError:
    return 2 
  
  else:
    return 0  

def get_string(up, op, down, ans, result):
  up_str = list()
  down_str = list()
  dashes_str = list()
  ans_str = list()
  spacer = " "*4
  
  line_up = ""
  line_down = ""
  dashes = ""
  line_ans = ""
  expression = ""
  
  for i in range(len(up)):
    #get the greater len() inbetween up and down
    digits = max(len(up[i]), len(down[i]))

    #then add 2 spaces for margin 
    up_str.append("  "+ " "*(digits-len(up[i])) + up[i])
    ans_str.append(" "*(digits-len(ans[i])+2) + ans[i])

    #join the symbol 
    down_str.append(op[i]+" "+ " "*(digits-len(down[i])) + down[i])
    dashes_str.append("-"*(digits + 2))
  
  #concat lines
  for i in range(len(up_str)-1):
    line_up += up_str[i] + spacer
    line_down += down_str[i] + spacer
    dashes += dashes_str[i] + spacer
    line_ans += ans_str[i] + spacer

  line_up += up_str[len(up_str)-1] + "\n"
  line_down += down_str[len(up_str)-1] + "\n"
  
  line_ans += ans_str[len(up_str)-1] 


  #concat all
  if result:
    dashes += dashes_str[len(up_str)-1] + "\n"
    expression += line_up + line_down + dashes + line_ans
  else:
    dashes += dashes_str[len(up_str)-1] 
    expression += line_up + line_down + dashes
    #print(expression)
  
  return expression