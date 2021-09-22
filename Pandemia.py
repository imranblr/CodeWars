def infected(s):
  itotal, total, count0, count1 = 0, 0, 0, 0
  for i in s:
    if i is not 'X':
      if i is '0':
        count0 += 1
        total += 1
      elif i is '1':
        count1 += 1
        total += 1
    else:
      if count1 > 0:
        itotal += count1 + count0
      count0, count1 = 0, 0
  if count1 > 0:
    itotal += count1 + count0
  if itotal == 0 or total == 0:
    return 0
  else:
    return itotal * 100 / total



fixeds = [("01000000X000X011X0X",73.33333333333333), ("01X000X010X011XX", 72.72727272727273), ("XXXXX", 0), ("00000000X00X0000", 0), ("0000000010", 100), ("000001XXXX0010X1X00010", 100), ("X00X000000X10X0100",42.857142857142854)]
for inp,exp in fixeds:
  print(infected(inp), exp)




