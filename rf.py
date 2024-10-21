import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv('whole2.csv',low_memory=False)




# # Drop rows containing any zero values
# data.dropna(inplace=True)
# data = data[(data != 0).all(axis=1)]

# # Replace NaN values with the mena of the  columns
# for col in df:
#     df[col].fillna(df[col].mean(), inplace=True)

# # Replace 0 values
# for column in df:
#     mean_val = df[(df[column] != 0) & (df[column].notna())][column].mean()
#     df[column] = df[column].replace(0, mean_val)


X = data.drop('Y', axis=1)
X = X.drop('part_id', axis=1)
X = X.drop(X.columns[0], axis=1)

print(X)
y = data['Y']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(random_state=42)

param_grid = {
    'n_estimators': [10],
    'max_features': ['sqrt'],
    'max_depth': [None, 10],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'bootstrap': [True]
}

grid_search = GridSearchCV(clf, param_grid, cv=5, verbose=1, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_rf = grid_search.best_estimator_

cv_scores = cross_val_score(best_rf, X_train, y_train, cv=5)
print("Cross-validation scores:", cv_scores)
print("Mean CV score:", np.mean(cv_scores))

y_pred = best_rf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

