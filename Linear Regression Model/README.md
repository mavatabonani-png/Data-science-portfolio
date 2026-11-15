# Ames Housing Price Prediction — Multiple Linear Regression

## Project overview

This project uses **Python** and **multiple linear regression** to explore and predict residential property sale prices in **Ames, Iowa**. It investigates how above-ground living area and garage area relate to house prices and evaluates a predictive model on a held-out test set.

The analysis is documented in the Jupyter Notebook [`Linear_Regression_Ames.ipynb`](Linear_Regression_Ames.ipynb), using the dataset [`ames.csv`](ames.csv).

## Objectives

- Explore the distribution of property sale prices, living area, and garage area.
- Examine correlations between the two predictors and sale price.
- Train a multiple linear regression model using **living area** and **garage area**.
- Evaluate the model using mean squared error (MSE), root mean squared error (RMSE), and residuals.
- Interpret the estimated coefficients and generate a sample property-price prediction.

## Dataset

The provided dataset contains **2,930 observations and 14 variables**, drawn from the Ames, Iowa housing data. The notebook describes property sales between **2006 and 2010** and references De Cock (2011).

The model uses three columns:

| Column | Meaning | Role |
| --- | --- | --- |
| `Gr_Liv_Area` | Above-ground living area, in square feet | Predictor |
| `Garage_Area` | Garage area, in square feet | Predictor |
| `Sale_Price` | House sale price, in US dollars | Target |

Other available columns include year built, year remodelled, basement size, floor areas, bathrooms, bedrooms, rooms, kitchens, and fireplaces.

## Methodology

1. **Inspect the data:** Load the CSV using Pandas; check missing values, duplicate records, data types, and descriptive statistics.
2. **Explore relationships:** Plot distributions of sale price, living area, and garage area, plus a correlation heatmap and living-area-versus-price scatter plot.
3. **Prepare the model:** Select `Gr_Liv_Area` and `Garage_Area` as input features and `Sale_Price` as the target.
4. **Split the data:** Use a reproducible **75% training / 25% testing** split (`random_state=42`), yielding 2,197 training observations and 733 test observations.
5. **Fit and evaluate:** Train scikit-learn's `LinearRegression`, compare predicted and actual prices, calculate MSE and RMSE, and inspect the residual plot.
6. **Interpret the model:** Examine estimated coefficients and predict a price for a property with median-sized living and garage areas.

## Key findings

| Measure | Result |
| --- | ---: |
| Mean sale price | Approximately **$180,796** |
| Median sale price | **$160,000** |
| Correlation: living area and sale price | Approximately **0.707** |
| Correlation: garage area and sale price | Approximately **0.640** |
| Test-set MSE | **2,634,371,879.69** |
| Test-set RMSE | **$51,326.13** |
| Predicted price at median living and garage areas | **$176,165.61** |

The fitted model estimates an increase of about **$78.69** in predicted sale price for an additional square foot of living area, holding garage area constant, and **$141.15** for an additional square foot of garage area, holding living area constant. These coefficients describe *associations in this model*, not causal effects.

The residual analysis suggests that prediction errors become more variable for higher-priced houses. This indicates that the two-feature model has important limitations and could benefit from additional predictors.

## Tools and libraries

- **Python 3**
- **Jupyter Notebook**
- **Pandas** — data loading and inspection
- **NumPy** — numerical calculations
- **Matplotlib** and **Seaborn** — visualisations
- **scikit-learn** — train/test split, regression, and model evaluation

## Project files

| File | Description |
| --- | --- |
| [`ames.csv`](ames.csv) | Housing dataset used in the analysis. |
| [`Linear_Regression_Ames.ipynb`](Linear_Regression_Ames.ipynb) | Complete analysis, plots, model, evaluation, and interpretation. |
| `README.md` | Project overview and instructions. |

## How to run

1. Download or clone the GitHub repository.
2. Keep `ames.csv` and `Linear_Regression_Ames.ipynb` in the **same folder**.
3. Install the required packages, if necessary:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn notebook
   ```

4. Open the notebook in **Jupyter Notebook** or **VS Code** with the Jupyter extension.
5. Run the cells in order to reproduce the data exploration, model training, graphs, and predictions.

## Limitations and potential improvements

- Only two explanatory variables are used. Property age, condition, location, and other attributes may explain additional variation in sale prices.
- The residual plot suggests **heteroscedasticity** and outliers, particularly among more expensive properties.
- The notebook **checks for seven duplicate rows** but does not remove them. It checks for missing values and drops rows missing the selected modelling variables; the notebook output reports no missing values.
- The model is an introductory predictive exercise and is **not a property valuation service**.

Potential next steps include comparing additional predictors, investigating outliers, trying regularised regression, and using cross-validation.

## Data reference

De Cock, D. (2011). *Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project*. **Journal of Statistics Education, 19**(3).

---

*This project is part of a data science learning portfolio and demonstrates exploratory analysis, predictive modelling, evaluation, and interpretation using Python.*
