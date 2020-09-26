#importing libraries
from sklearn.externals import joblib
import Inputscript

#load the pickle file
classifier = joblib.load('rf_final.pkl')


#input url
print("\n\n\n\nWelcome to the phishing website detection software !\n")   
url = input("Enter the Website URL: ")

#checking and predicting
checkprediction = Inputscript.main(url) 
prediction = classifier.predict(checkprediction)

#Printing the result
if(prediction == 1):
    print("The site is a phishing site")
else:
    print("The site is not a phishing site")