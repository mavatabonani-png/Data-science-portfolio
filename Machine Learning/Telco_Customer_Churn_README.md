# Telco Customer Churn Prediction

## Project overview

This project uses Python and supervised machine learning to predict **customer churn** for a telecommunications provider. Churn refers to customers leaving the service. By exploring customer characteristics and comparing classification models, the project investigates how accurately at-risk customers can be identified.

The analysis was conducted in a Jupyter Notebook and compares **Logistic Regression** with a **Random Forest Classifier**. The models are assessed using accuracy, precision, recall and confusion matrices.

## Project objectives

- Inspect and clean customer subscription and billing data.
- Explore relationships between customer characteristics and churn.
- Convert categorical variables into numeric features for modelling.
- Train and evaluate two classification algorithms.
- Compare the models, particularly their ability to identify customers who actually churned.

## Dataset

The source file, `Telco-Customer-Churn.csv`, contains **7,043 observations and 21 columns**. Variables include customer tenure, contract type, monthly and total charges, internet and phone services, support services, payment method and whether the customer churned (`Yes` or `No`).

The target variable is `Churn`, encoded as **1** for customers who left and **0** for customers who stayed. After handling missing values, **7,032 records** remain for the analysis.

## Methodology

### 1. Data cleaning and preparation

- Load and inspect the dataset with Pandas.
- Convert `TotalCharges` to numeric values, coercing invalid entries to missing values.
- Remove records containing missing values.
- Drop the `customerID` identifier.
- Encode the target variable and convert categorical predictors using `pd.get_dummies(..., drop_first=True)`.

### 2. Exploratory data analysis

The notebook includes:

- A horizontal bar chart of correlations between encoded features and churn.
- A histogram of customer tenure.
- A scatter plot of monthly charges versus total charges.
- A box plot comparing tenure for customers who stayed and customers who churned.

These visualisations explore patterns and associations; they do not establish causation.

### 3. Model training

The prepared data is split into **75% training** and **25% testing** subsets, using a stratified split and `random_state=42`. The notebook contains **5,274 training records** and **1,758 test records**.

A `MinMaxScaler` is fitted to the training features and then applied to the test features. Two models are trained:

- **Logistic Regression** (`max_iter=1000`)
- **Random Forest Classifier** (2,000 trees, out-of-bag scoring enabled, and a maximum of 50 leaf nodes)

### 4. Model evaluation

The notebook reports the following results on the held-out test set:

| Metric | Logistic Regression | Random Forest |
| --- | ---: | ---: |
| Accuracy | 80.60% | 79.18% |
| Precision | 65.4% | 65.1% |
| Recall | 57.2% | 46.7% |

The Random Forest's **out-of-bag (OOB) error** is approximately **20.08%**.

**Confusion matrices** (rows: actual values; columns: predicted values; class order 0 = stayed, 1 = churned):

| Model | True negatives | False positives | False negatives | True positives |
| --- | ---: | ---: | ---: | ---: |
| Logistic Regression | 1,150 | 141 | 200 | 267 |
| Random Forest | 1,174 | 117 | 249 | 218 |

## Key findings

- **Logistic Regression outperformed Random Forest** on accuracy, precision and recall for this experiment.
- Logistic Regression identified **267** actual churners, compared with **218** for Random Forest.
- Both models missed customers who churned, which is a significant limitation for a customer-retention use case.
- Recall is particularly relevant when the objective is to identify as many likely churners as possible for potential retention outreach.

These results describe the particular dataset, feature preparation and model settings used in the notebook; they should not be interpreted as guaranteed performance on other customer populations.

## Technologies and libraries

- Python 3
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn
- scikit-learn

## Project files

| File | Description |
| --- | --- |
| `telco_customer_churn.ipynb` | Notebook containing data preparation, exploratory analysis, model training and evaluation. |
| `Telco-Customer-Churn.csv` | Original telecommunications customer dataset. |
| `README.md` | Project overview, methodology, results and usage instructions. |

## How to run the project

1. Download or clone this repository.
2. Make sure `telco_customer_churn.ipynb` and `Telco-Customer-Churn.csv` are in the same folder.
3. Install the required libraries:

   ```bash
   pip install notebook pandas matplotlib seaborn scikit-learn
   ```

4. Open the notebook in Jupyter Notebook or VS Code with the Jupyter extension.
5. Select a Python environment with the required packages installed and run all cells in sequence.

## Limitations and potential improvements

- Accuracy alone may be misleading because customers who stayed outnumber customers who churned. Consider also reporting F1-score, ROC-AUC and PR-AUC.
- Recall could be improved through threshold tuning, model hyperparameter optimisation and methods for handling class imbalance.
- A separate validation or cross-validation process would help assess model robustness before deployment.
- Correlations and model predictions should not be interpreted as evidence that a customer characteristic causes churn.
- A real-world retention solution would also need to consider the costs of false positives and missed churners, plus privacy and fairness considerations.

## Conclusion

This project demonstrates the complete workflow of a foundational binary classification exercise: cleaning data, exploring patterns, engineering model-ready features, training two machine-learning algorithms and comparing their predictive performance. On the reported test-set metrics, **Logistic Regression was the stronger model for identifying customer churn**, although further development would be needed before practical use.
