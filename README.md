# Polars vs Pandas


## SQL query like a problem
Let's assume that the following SQL query that should be re-written in Python:
```SQL
SELECT
  t.transaction_category_id,
  sum(t.transaction_amount) AS sum_amount,
  count(DISTINCT t.user_id) AS num_users
FROM "transactions" t
JOIN "users" u USING (user_id)
WHERE t.is_blocked = False
  AND u.is_blocked = False
GROUP BY t.transaction_category_id
ORDER BY sum_amount DESC;
```

However, in the last few years a new python/rust library started to become a more popular choice when working with DataFrames. In order to install it it is required to run in command line `$ pip install polars`. 

Nevertheless, solutions for both libraries are presented in files `task 2 - pandas.py` and `task 2 - polars.py`. Both solutions consist of 4 main steps:
1. Read data
1. Join data
1. Filter data
1. Group and aggregate data.

The corresponding comments are given in the files. These actions are pretty much executed in the same order as in the query. The second solution deserves attention because it is faster and the solution may look nicer and easier to maintain.

The proof to be faster is provided by H2O.ai here https://h2oai.github.io/db-benchmark/.
The proof for the second statement can be found below via side by side comparison. 


### pandas
```Py
# join and filter
f = pd.merge(t, u, on="user_id")
f = f.loc[(f.is_active == True) & (f.is_blocked == False)] 


# group and agregate
(
    f
    .groupby("transaction_category_id", as_index=False)
    .agg(
        {
            'transaction_amount': "sum", 
            'user_id':            "nunique"
        }
    )
    .rename(columns=
        {
            'transaction_amount': 'sum_amount',
            'user_id':            'num_users'
        }
    )
    .sort_values(by=['sum_amount'], ascending=False)
)
```

### polars
```py
(
    t
    .join(u, on="user_id")
    .filter((pl.col("is_blocked") == False) & (pl.col("is_active")))
    
    .groupby("transaction_category_id")
    .agg(
        [
            pl.sum     ("transaction_amount").alias("sum_amount"),
            pl.n_unique("user_id")           .alias("num_users"),
        ]
    )
    .sort("sum_amount", reverse=True)
)
```



It can be seen that code for polaris looks simpler: it takes `t` transactions and `u` users tables joins them and filters out `blocked` and `inactive` users by referencing itself columns, while pandas makes to save some middle state data of **merging** and filtering out, which is okay. After that both code snippets do grouping by `category` and summarization action over corresponding `column`. However, `pandas` allows us to give it an alias or rename it. Sorting doesn’t not have much distinguishability that deserves attention. The most important feature for the current case is that polars doesn’t require creating a variable that keeps some middle term data, it brings some sort of immutability which in the current case is welcomed. 

It is also important to note that  the *advertised* new library has such clear caveats as lack of some functionality, which may be never discovered for some projects or companies, less developed community, which may mean significant lack of dummy questions on stackoverflow and etc. Nevertheless, it is just an alternative way of handling the provided task.

Thank you and I am happy to answer any questions! Feel free to reach me out:)
