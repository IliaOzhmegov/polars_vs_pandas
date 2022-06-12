# read data
t = pl.read_csv(find_path("transactions.csv"))
u = pl.read_csv(find_path("users.csv"))


# join, filter, group and agregate
res = (
    t
    .join(u, on="user_id", suffix="_user")
    .filter((pl.col("is_blocked") == False) & (pl.col("is_blocked_user") == False))

    .groupby("transaction_category_id")
    .agg(
        [
            pl.sum     ("transaction_amount").alias("sum_amount"),
            pl.n_unique("user_id")           .alias("num_users"),
        ]
    )
    .sort("sum_amount", reverse=True)
)
