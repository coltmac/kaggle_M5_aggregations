# M5 Competition: Aggregation Levels

Creates the 12 aggregations levels described in the M5 guide.


|     Level        id    |     Aggregation   Level                                                       |     Number of series    |
|------------------------|-------------------------------------------------------------------------------|-------------------------|
|     1                  |     Unit sales of all products, aggregated for all stores/states              |     1                   |
|     2                  |     Unit sales of all products, aggregated for each State                     |     3                   |
|     3                  |     Unit sales of all products, aggregated for each store                     |     10                  |
|     4                  |     Unit sales of all products, aggregated for each category                  |     3                   |
|     5                  |     Unit sales of all products, aggregated for each department                |     7                   |
|     6                  |     Unit sales of all products, aggregated for each State and   category      |     9                   |
|     7                  |     Unit sales of all products, aggregated for each State and   department    |     21                  |
|     8                  |     Unit sales of all products, aggregated for each store and   category      |     30                  |
|     9                  |     Unit sales of all products, aggregated for each store and   department    |     70                  |
|     10                 |     Unit sales of product x,   aggregated for all stores/states               |     3,049               |
|     11                 |     Unit sales of product x,   aggregated for each State                      |     9,147               |
|     12                 |     Unit sales of product x,   aggregated for each store                      |     30,490              |
|     Total              |                                                                               |     42,840              |

As much information as possible, given the aggregation, is kept in each dataframe.