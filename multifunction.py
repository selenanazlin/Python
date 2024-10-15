class multiplefunctions():
    
    def Subfields_in_AI():
        subfields = ["Machine Learning", "Neural Network", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("The Subfields of AI are:")
        for subfield in subfields:
            print(subfield)
            
    def OddEven():
        num = int(input("enter a number:"))
        if((num%2)==0):
            print("Even")    
        else:
            print("odd")
            
    def Elegible():
        gender = input("Enter the gender:")
        age = int(input("Enter age:"))
        if (gender == "male"):
            if age >= 21:
                print("Eligible for marriage")
            else:
                print("Not Eligible")
        elif (gender == "female"):
            if age >= 18:
                print("Eligible for marriage")
            else:
                print("Not Eligible")
        else:
            print("invalid")
            
    def percentage():
        sub1 = int(input("Subject 1:"))
        sub2 = int(input("Subject 2:"))
        sub3 = int(input("Subject 3:"))
        sub4 = int(input("Subject 4:"))
        sub5 = int(input("Subject 5:"))
        total_mark = sub1+sub2+sub3+sub4+sub5
        max_mark = 500
        percentage = (total_mark/max_mark)*100
        #return percentage
        print(percentage)
        
    def triangle_area():
        height = int(input("Height: "))
        breath = int(input("Breath: "))
        print("Area formula = (height*breath)/2")
        area = (height*breath)/2
        print(area)

    def triangle_perimeter():
        height1 = int(input("Height1: "))
        height2 = int(input("Height2: "))
        breath = int(input("Breath: "))
        print("Perimeter formula = height1 + height2 + breath")
        perimeter = height1 + height2 + breath
        print(perimeter)