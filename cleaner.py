import pandas as pd
import statsmodels.api as sm
from model_calculation import p_values
from model_calculation import results
from data_input import the_data
from model_specification import y_endo
from clean_specification import significant_level

deleted_variables_list = []
while True:
    const_value = p_values['const']
    p_values = p_values.drop('const')
    temp_max_value = p_values.idxmax()
    if p_values[temp_max_value] < significant_level:
        print("")
        print("===================================INFO=======================================")
        print("All variables under significant level have been removed...")
        print("Your significant level was:", significant_level)
        print("List of deleted variables:",deleted_variables_list)
        print("This is your final model:")
        print("==============================================================================")
        print("")
        const = pd.Series([const_value], index=['const'])
        p_values = p_values.append(const)
        print(results.summary())
        break
    else:
        deleted_variables_list.append(temp_max_value)
        p_values = p_values.drop(temp_max_value)
        const = pd.Series([const_value], index=['const'])
        p_values = p_values.append(const)
        final_model = sm.OLS(endog = the_data[y_endo], exog = the_data[p_values.index])
        results = final_model.fit()
        p_values = results.pvalues







