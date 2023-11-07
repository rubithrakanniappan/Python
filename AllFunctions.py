class AllConcept():
    def Subfields():
        print("Sub-fields in AI are:")
        AIConcept = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfield in AIConcept:
            print(subfield)
            
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
           print(num, "is EvenNumber") 
           oddeven = num, "is Even Number"
        else:
           print(num, "is Odd Number") 
           oddeven = num, "is Odd Number"
            
    def Eligible():
        Gender=input("Your Gender:") 
        Age=int(input("Your Age:"))
        if(Gender.lower()=='male' and Age >= 21):
            print("ELIGIBLE") 
            Marriage = "ELIGIBLE"
        elif(Gender.lower()=='female' and Age >=18):
            print("ELIGIBLE") 
            Marriage = "ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            Marriage = "NOT ELIGIBLE"        
       
    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        AddSubMark = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total : " , AddSubMark)
        print("Percentage : " ,float(AddSubMark)*(100/500))   
 
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breath)/2")
        print("Area of Triangle: ", (Height*Breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", Height1+Height2+Breadth)    