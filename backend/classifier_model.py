from sort_data import get_df
import sklearn

datapath = './../data'
df = get_df(datapath)

# data still needs to be embedded
input_data = df["corr_action", "descrep_narrative", "system_reason_desc"].copy()

# classifier for column C
output_data = df["wuc"].copy()

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(input_data, output_data, test_size = 0.3, random_state=42)

svc = sklearn.svm.SVC(random_state=42)

# train SVC model
svc.fit(X_train, y_train)

# test accuracy on SVC model
accuracy = svc.score(X_test, y_test)

