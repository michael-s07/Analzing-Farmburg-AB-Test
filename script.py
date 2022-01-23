# Import libraries
#import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import binom_test
from scipy.stats import chi2_contingency

abdata = pd.read_csv('clicks.csv')
print(abdata.head())
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
is_significant = True
num_visits = len(abdata)
print(num_visits)
num_sales_needed_099 = 1000/0.99
p_sales_needed_099 = num_sales_needed_099/num_visits

print(p_sales_needed_099)
num_sales_needed_199 = 1000/1.99
p_sales_needed_199 = num_sales_needed_199/num_visits
print(p_sales_needed_199)
num_sales_needed_499 = 1000/4.99
p_sales_needed_499 = num_sales_needed_499/num_visits
print(p_sales_needed_499)

samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
print(samp_size_099)
print(sales_099)
samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))
print(samp_size_199)
print(sales_199)
samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 4.99 price point
print(samp_size_499)
print(sales_499)
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')

print(pvalueA)
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')

print(pvalueB)

pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')

print(pvalueC)
final_answer = '4.99'

print(final_answer)