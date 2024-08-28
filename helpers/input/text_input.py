from helpers.print.red import print_in_red

def text_input(msg:str, v_type:str, length, range):
  i = input(msg)
  if v_type=='string':
    if len(i)>=length:
      return i
    else:
      print_in_red(f"Min Input length {length}")
      text_input(msg,v_type,length,range)
  elif v_type=='number':
    i = int(i)
    if i>=range[0] and i<=range[1]:
      return i
    else:
      print_in_red("Number out of range")
      text_input(msg,v_type,length,range)
  return

    