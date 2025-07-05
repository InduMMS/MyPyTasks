#Writing using Python sysntax
import math



def mathMethods01():
   n=3375
   result = math.cbrt(n)
   print(f'cubethroot of {n} ={result}')

   n=8
   result = math.comb(n,3)
   print(f'nCr --> {n}C{3} ={result}')
   print(f'nPr --> {n}P{3} ={math.perm(n,3)}')
## mathMethods01():


def mathMethods02():
   nums = [12, 18, 66]
   print(f'Numbers = {nums}   GCD={math.gcd(*nums)}  LCM={math.lcm(*nums)}')

   small = min(nums)
   gcdNums = []
   k = 0
   for n in nums:
      gcdNums.append([])
      for i in range(2, small+1):
         if n % i == 0 : 
            if (i not in gcdNums) : gcdNums[k].append(i)
            #print(f'   n={n}  mod={n%i}  i={i}')
         #print(gcdNums, f'Small={small} i={i}')
         i += 1
      print(gcdNums, f'for n={n}  Small={small} i={i}')
      k += 1
   print(gcdNums, '==Final')

   commonNums = set(gcdNums[0])
   for k in range(1, len(gcdNums)):
      commonNums = commonNums.intersection(set(gcdNums[k]));
   print(commonNums, '==Common Nums~~~ ', max(commonNums), '=my Calc HCF')

   uniqueNums = list(gcdNums[0])
   for k in range(1, len(gcdNums)):
      print(f'k={k}')
      uniqueNums.extend(gcdNums[k]);
   uqSet = set(uniqueNums)
   lcm = 1
   for k in uqSet:
      if (lcm % k) != 0: lcm = lcm * k
      #print('   k=',k, '  lcm=', lcm)

   print(uqSet, '==Unique Set~~~ ', lcm,  '=my Calc LCM')



## mathMethods02():




if __name__ == '__main__':
   mathMethods02();




'''
n = 5 
result = sum(i**3 for i in range(1, n+1))
print(f'sum={result}')

favs = ['Chess', 'Hockey', 'Soccer', 'Swimming', 'Cricket', 1001, 247.50,  0o127, 0xFB1]
for index, x in enumerate(favs[::1], start=1):
    print(x, index)
    print(id(x), type(id))
'''