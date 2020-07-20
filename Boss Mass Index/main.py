

class BMI(object):
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def __repr__(self):
        try:
            bmi = round(self.weight /(self.height**2), 2)
            if bmi <= 15.99:
                value = "Very UnderWeight"
            elif bmi >=16 and bmi<= 16.99:
                value = "Moderate InderWeight"
            elif bmi>=17 and bmi<=17.99:
                value = "Possible UnderWeight"
            elif bmi>=18.5 and bmi<=24.99:
                value = "Normal Weight"
            elif bmi>=25 and bmi <= 27.49:
                value = "Possible OverWeight"
            elif bmi>=27.5 and bmi<=29.99:
                value = "OverWeight"
            elif bmi>=30 and bmi<= 34.99:
                value = "Obesity class 1"
            elif bmi >=35 and bmi<=39.99:
                value = "Obesity Class 2"
            elif bmi>40:
                value ="Obesity class 3"
            return f"BODY MASS INDEX: {bmi}\t RANK: {value}"

        except:
            return" Need Weight and Height"

if __name__=="__main__":
    bmi = BMI(85, 1.75)
    print(bmi)