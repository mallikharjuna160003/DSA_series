def checkAnagram(string1, string2):
    #your code goes here
    string1 = list(string1.lower())
    string2 = list(string2.lower())
    if( string1.sort() ==  string2.sort() ):
        return True
    return False

if __name__=='__main__':
    #you can run any test cases here
    print(checkAnagram("god","dog"))
    name = "doa"
  
