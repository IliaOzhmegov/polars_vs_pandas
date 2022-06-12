# Polars vs Pandas: convenience

There are a lot of [awesome dataframe libraries]{https://github.com/jcmkk3/awesome-dataframes},
and in this post I would like to draw attention to their ergonomics by comparing of Pandas and 
Polars Python libraries.


It seems when we compare one of the most flexible and powerful data analysis Pandas library 
with Polars, the last one can boast of its speed 
[H2O.ai]{https://h2oai.github.io/db-benchmark/}. Is it really true?

Well, as the main purpose of both libraries is a work with rectangular type of data (dataframes).
Let's take a SQL query and implement it in Python with the use of those libs and look at the code.

