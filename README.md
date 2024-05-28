### NOTE: This is a sterilized version that does not contain proprietary data as with the original repository

# Notre Dame/Boeing Natural Language Processing for Aircraft Maintenance Project
This project was created for Notre Dame's EG 35101 Industry and Community-Based Innovation Projects in collaboration with Boeing Co. The goal of the project was to create a tool that can take in a description of performed aircraft maintanence and output the correct log information for the maintenance log.

Contributers: Dagny Brand (dbrand@nd.edu), Jaylen Choi (jchoi22@nd.edu), Vinny Galassi (vgalassi@nd.edu), Gabby Klee (gklee@nd.edu), Richard Montoya (rmontoya@nd.edu), Joseph Park (jpark29@nd.edu), Tram Trinh (htrinh@nd.edu), Anthony Tsiantis (atsianti@nd.edu), Kevin Xue (kxue2@nd.edu), and Swindar Zhou (kzhou3@nd.edu)

# Working with our Classifiers

This project uses a Scalable Linear Support Vector Machine (SVC) classifier from the [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) library. The classifier is originally laid out in [classifer_colab](classifier_colab.ipynb). The data used to train the model is located in the [data](data) folder and was provided by Boeing. 

To use text as input to a classifier, the text must first be embedded, which changes the text data into a numerical vector representation. We use [Google's Universal Sentence Encoder](https://www.kaggle.com/models/google/universal-sentence-encoder/frameworks/tensorFlow2/variations/universal-sentence-encoder/versions/2?tfhub-redirect=true) to embed the text input. The model is downloaded and used in the "Text Embedding" section of the Colab notebook. The "SVC Classifier - one column input" section of the Colab contains our classifier model. input_data is set to the desired input column (we use descrep_narrative) and output_data is set to the desired output column (for the model classifier, this is the "wuc" column, which is column C of the data set). The train_test_split() function from sklearn splits the given input and output data into 70% training data used to train the model and 30% testing data used to test the model's accuracy. We then declare our SVC model using sklearn.svm.svc() and use the .fit() method with our training data to train the classifier. We test the accuracy using the .score() method on the testing data. The "SVC Classifier - all input columns" uses all three given input columns as input data.

The [backend_python](backend_python) folder contains Python files with our methods outlined in the colab and used by our final API tool. These include an Embedder class and a Classifier class. Our .predict() method takes in the user's input and returns the classifier's classification for each column required by the data log.


# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
