import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
import joblib

# Step1: Loading the dataset
df = pd.read_csv("dataset.csv")

# Step2: Splitting train and test data
x = df.drop(["Label"], axis=1)
y = df["Label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=650)

# Step3: Building model
model = RandomForestClassifier(n_estimators=100, max_depth=5, max_features="sqrt")
model.fit(x_train, y_train)

joblib.dump(model, "rf_malaraia_100_5")   # saving the model for future real-time use

# Step4: Making predictions
predictions = model.predict(x_test)
i = 0
print(x_test)
# print(metrics.classification_report(predictions, y_test))
