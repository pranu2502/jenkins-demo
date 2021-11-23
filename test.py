from prog import add,div

def test():
  res = add(12,23)
  expected = 35
  assert res == expected
  print("1. add(12,23)")
  print("pass")

  res = div(12,2)
  expected = 6
  assert res == expected
  print("2. add(12,2)")
  print("pass")

  res = div(12,3)
  expected = "Inf"
  assert res == expected
  print("3. div(12,0)")
  print("pass")



if __name__ == "__main__":
  try:
    test()
  except Exception as e:
    print("An error ocured: " + e)
