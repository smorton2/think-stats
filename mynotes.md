# Description
These are my notes, organized by chapter, from ThinkStats2.

# Quick Links
- [Book](http://greenteapress.com/wp/think-stats-2e/)
    - PDF of book at `~/Documents/learning/thinkstats2/thinkstats2.pdf`
- NSFG
    - [index](https://www.cdc.gov/nchs/nsfg/index.htm)
    - [codebooks](https://www.cdc.gov/nchs/nsfg/nsfg_cycle6.htm)
- Launch ipython notebook
    - `ipython notebook &`

# Chapter 1

## Data Frames
First, you need to read the data in as a DataFrame (df).  Find a way to read in
the data appropriately based on its type.  Enter df name to see truncated view.

*Note: Assume we've assigned our DataFrame the variable df*

### Useful Commands for DataFrames
Treat DataFrame like sql tables.  Here's how to access their columns.
- **List all columns:** df.columns
- **Access column:**
    - df.columns[*{column_index}*]
    - df['*{column_name}*']
    - df.*{column_name}*
        - Don't use this when creating new columns in a DataFrame
- **Transform columns:**
    - {column_name}**.replace**(*value_to_replace, desired_value, inplace=boolean*)
        - Replace specific values in a column with a specific value
        - e.g.: `df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)`
    - **df.loc**[*{label or condition}, {column_to_update}*] = *{value to enter}*
        - Enter a value in specific locations in a column.
        - e.g.: `df.loc[df.birthwgt_lb > 20, 'birthwgt_lb'] = np.nan`
- **Summarize data:**
    - {column_name}**.value_counts**(*sort=boolean*)

### Useful Commands for Series
DF columns are read as series.  Series are like arrays.
- **Get element from series:** series[*{index}*]
- **Get range from series:** series[*{start index}*:*{end index}*]

# Chapter 2

## Distributions

You can write a function to build a histogram
```
hist = {}
def build_hist(t):
    for x in t:
        hist[x] = hist.get(x, 0) + 1
```
Or use value_counts

## Histograms
In general, use matplotlib.pyplot()

To plot a histogram using thinkstats functions:
```
import thinkplot
thinkplot.Hist({histogram object})
thinkplot.Show(xlabel='value', ylabel='frequency')
```

[thinkplot documentation](http://bit.ly/1sgoj7V)

## Summary Statistics

**Mean~average**: Measure of central tendency

**Standard Dev**: Results within 1 standard dev are normal

**Variance**: StDev^2.  Usually not very useful.

### Effect size

Difference btwn Means is useful, but has no indication of if results matter:
`diff_means = group1.mean() - group2.mean()`

Cohen's d divides by standard dev to show if the effect size is consequential:
`cohens_d = (X1 - X2) / s` where `X1` and `X2` are the standard devs of the two groups and `s` is the pooled standard dev.

```
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
```
# Chapter 3

**Probability Mass Function (PMF)**
- Stores probability of occurrence of each value (SudoSQL: `COUNT_IF(value=x)/COUNT(1)`)
- Use [`pyplot.hist(x, density=True)`](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.hist.html) to plot PMF

**Manipulating DataFrames**

Create dataframe from numpy array and name the columns and indexes (rows)
```
{{import everything}}
array = np.random.randn(4, 2)
columns = ['A', 'B']
index = ['a', 'b', 'c', 'd']
df = pandas.DataFrame(array, columns=columns, index=index)
```

Index to pull values from a column `df['A']`

Use `df.loc['a']` to pull values from row 'a'

Use `ds.iloc[0]` to pull values from row by the index number

You can also use a slice to pull a range of rows by position or label
`df['a':'c']` OR `df[0:3]`

# Chapter 4

**Cumulative Distribution Functions (CDFs)** map from a value to its percentile rank.  They can help combat the issues of having too many or too few bins that happen when you have a large number of values in a histogram or PMF.  They also make it much easier to visually compare distributions.

`CDF(x)` computes the % of values <= x (i.e. probability a value will be less than or equal to x)

Graph of a CDF will be a step function.

# Chapter 5

You can use analytic distributions to model empirical distributions.

**Exponential Distribution**

- described by `1-e^(-lambda*x)`
- Lambda determines shape, big lambda = big curve
- If distribution follows exponential, then complementary CDF on a log scale will be a straight line.
- Remember `lambda` is a Python keyword

**Normal Distribution**

Use *normal probability plot* to determine if data follows a normal distribution
1. Sort values in sample
2. Generate random sample with same sample size & sort it (use mean = 0 & standard dev = 1)
3. Plot sorted values vs random values
Result is straight line with `intercept = mean` & `slope = standard dev`

**Lognormal Distribution**

When log of set of values has normal distribution.
- plot on logx scale, looks like normal distribution
- Test fit using normal probability plot of log of values.

**Pareto Distribution**

`1-(x/x_m)^(-alpha)`
- x_m = minimum possible value for x
- alpha = shape
- Complimentary CDF on a log-log scale looks like a straight line
