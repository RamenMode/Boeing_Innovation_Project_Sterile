# reference: https://www.analyticsvidhya.com/blog/2021/10/beginners-guide-on-how-to-train-a-classification-model-with-tensorflow/

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import matplotlib as plt
from matplotlib import rcParams
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import roc_auc_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# read data (still needed)
datfile = 'blank.csv'
df = pd.read_csv(datfile)

# hopefully the training classification is easy given the data set
df['maintanence_type_1'] = []
df['maintanence_type_2'] = []

X = df.drop('maintanence_type_1', axis=1)
y = df['maintanence_type_1']

# choose split for how much is type 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

# the above is all part of creating the training set --> hopefully this won't be too hard given the Boeing data


# we need to scale the data so the model can use it as input
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# I also learned that we can use an existing classification model one the data
# building a neural network is actually unnecessary
# so we can use LinearDiscriminationAnalysis for linear classification or another model from sklearn
lda = sklearn.discriminant_analysis.LinearDiscriminantAnalysis()

# .fit trains the classification model
lda.fit(X_train_scaled, y_train)

# .score gets an accuracy off the test data
accuracy = lda.score(X_test_scaled, y_test)

# .predict gets a prediction
prediction = lda.prediction(X_test_scaled[0])


# sklearn is super easy!!!

# see my initial thoughts about a NN below
# we can use Tensorflow to train the classification model
tf.random.set_seed(42)

# we need to pick what layers we want in our model
# this model goes 12 input --> 128 --> 256 --> 256 --> 1 output
# PS i always have trouble running tensorflow on mac
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    loss=tf.keras.losses.binary_crossentropy,
    optimizer=tf.keras.optimizers.Adam(lr=0.03),
    metrics=[
        tf.keras.metrics.BinaryAccuracy(name='accuracy'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]
)

history = model.fit(X_train_scaled, y_train, epochs=100)

# then, we can test our model for accuracy
rcParams['figure.figsize'] = (18, 8)
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False
plt.plot(
    np.arange(1, 101), 
    history.history['loss'], label='Loss'
)
plt.plot(
    np.arange(1, 101), 
    history.history['accuracy'], label='Accuracy'
)
plt.plot(
    np.arange(1, 101), 
    history.history['precision'], label='Precision'
)
plt.plot(
    np.arange(1, 101), 
    history.history['recall'], label='Recall'
)
plt.title('Evaluation metrics', size=20)
plt.xlabel('Epoch', size=14)
plt.legend()


# we can use our model to get classification predictions
# this model would take in the description and output the type of maintenance
predictions = model.predict(X_train_scaled)

def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()
# Computing manually fpr, tpr, thresholds and roc auc 
fpr, tpr, thresholds = roc_curve(y_test, predictions)
roc_auc = auc(fpr, tpr)
print("ROC_AUC Score : ",roc_auc)
print("Function for ROC_AUC Score : ",roc_auc_score(y_test, predictions)) # Function present
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]
print("Threshold value is:", optimal_threshold)
plot_roc_curve(fpr, tpr)

prediction_classes = [
    1 if prob > optimal_threshold else 0 for prob in np.ravel(predictions)
]
prediction_classes[:20]