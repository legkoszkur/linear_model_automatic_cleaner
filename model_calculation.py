from model_specification import x_egzo
from model_specification import y_endo
from data_input import the_data
import statsmodels.api as sm

new_model = sm.OLS(endog = the_data[y_endo],exog =  the_data[x_egzo]) # tutaj popełniałem taki błąd że zamiast OLS pisałem ols
results = new_model.fit()
print(results.summary())
print("Under p-values:")
p_values = results.pvalues
print(p_values)




