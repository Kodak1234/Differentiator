"""
Python class for differentiating polynomials
form
    nvm + nvm ... + nvm

    n = coefficient
    v = variable
    m = exponent, m != 1, m > 0
    
"""
class DiffQ(object):
    def __init__(self,x):
        self.x = x

    def setX(self,x):
        self.x = x

    def solve(self,c = "x"):
        x = list(self.x)
        #print(self.resolveConst(x,c))
        sol = ""
        
        for k,v in enumerate(x):

            if(v.isalpha()):
                if(k < len(x) - 1):
                    if(x[k+1].isdigit()):
                        num = self.getNum(k+1,x)#exponent
                        f = self.getNumBack(k-1,x) if(k > 0 and x[k-1].isdigit()) else "1"
                        f = int(num) * int(f) #coefficient
                        e = str(int(num)-1) if(int(num)-1 > 1) else "" #new exponent
                        sol = sol + str(f) + c + e

                    #order of one
                    else:
                        sol += self.orderOne(k,x)
                        
                    #last variable
                elif(k == len(x) - 1):
                    sol += self.orderOne(k,x)

            elif(v.isdigit()):
                if(k+1 < len(x) and (x[k+1] == "-" or x[k+1] == "+") or k+1 == len(x)):
                    num = self.getNumBack(k,x)
                    if(k-(len(num)-1) > -1):
                        #make sure it is not an exponent
                        if(not x[k-len(num)].isalpha()):
                           sol += "0"

            else:
                sol += v

        return sol

    def orderOne(self,k,x):
        num = self.getNumBack(k-1,x);
        sol = num if(len(num) > 0) else "1"

        return sol             
                        
    def getNumBack(self,i,x):
        num = ""
        while(i >= 0):
            if(not x[i].isdigit()):
                break
            
            num += x[i]
            i -= 1;

        return num[::-1]

    def getNum(self,k,x):
        num = ""
        for i in range(k,len(x)):
            if(not x[i].isdigit()):
                break
            num += x[i]

        return num
        
    def __str__(self):
        return self.x


















    
    
