# read data
t = pd.read_csv(find_path("transactions.csv"))
u = pd.read_csv(find_path("users.csv"))

# join and filter
f = pd.merge(t, u, on="user_id", suffixes=('_trxn', '_user'))
f = f.loc[(f.is_blocked_user == False) & (f.is_blocked_trxn == False)]


# group and agregate
res = (
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
