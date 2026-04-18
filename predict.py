import joblib
import numpy as np

model = joblib.load("model.pkl")

sample = np.array([[650,35,5,50000,2,1,1,70000]])

result = model.predict(sample)

if result[0] == 1:
    print("Customer Will Churn")
else:
    print("Customer Will Stay")