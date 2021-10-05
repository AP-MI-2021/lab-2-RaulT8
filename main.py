import datetime

def isPrime(x):
    if x<2:
        return False
    for i in range (2,x//2+1):
        if x%i==0:
            return False
    return True

def get_largest_prime_below(n):
  ok=True
  m=n-1
  while ok==True:
    if isPrime(m)==True:
      ok=False
    else:
      m=m-1
  return m

def test_get_largest_prime_below():
  assert get_largest_prime_below(12) is 11
  assert get_largest_prime_below(8) is 7
  assert get_largest_prime_below(6) is 5
  assert get_largest_prime_below(4) is 3

def get_age_in_days(birthday):
  from datetime import datetime 
  number_of_days_since_birthday = (datetime.utcnow() - birthday).days 
  return number_of_days_since_birthday  

def test_get_age_in_days():
  assert get_age_in_days(18/7/2002) is 7017
  assert get_age_in_days(12/12/2012) is 3217
  assert get_age_in_days(6/6/2006) is 5598
  assert get_age_in_days(1/1/2001) is 7580

def is_palindrome(n):
  ok=False
  cn=n
  m=0
  if n<10:
    return ok
  while cn>0:
    m= m*10 + (cn%10)
    cn//=10
  if m == n:
    ok=True
  return ok

def test_is_palindrome():
  assert is_palindrome(1221) is 1
  assert is_palindrome(232) is 1
   

def main():
  print("""
Meniu:
1. Ultimul numar prim mai mic decat un numar dat
2. Determinati varsta unei persoane dupa data nasterii introdusa sub forma:DD/MM/YYYY
3. Determinati daca un numar este palindrom sau nu
x. Inchideti programul
  """)
  option = input("Selectati o optiune: ")
  shouldRun=True

  while shouldRun==True:
    if option == "1":
      num = int(input("Introduceti un numar: "))
      prim=get_largest_prime_below(num)
      print(prim)
      shouldRun=True
      if shouldRun == True:
        option = input("Selectati o optiune: ")

    elif option == "2":
      from datetime import datetime
      datestr = input("Introduceti ziua de nastere sub formatul: (dd/mm/yyyy): ")
      birthday = datetime.strptime(datestr, "%d/%m/%Y")
      day=get_age_in_days(birthday)
      print(day,'zile')
      shouldRun=True
    elif option == "3":
      n=int(input("Introduceti un numar: "))
      m=is_palindrome(n)
      print(m)
      shouldRun=True
    if shouldRun == True:
      option = input("Selectati o optiune: ")

    if option=="x":
      shouldRun=False


    
  
if __name__ == '__main__':
  main()