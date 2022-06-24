# Distributed Hashing Table

With large volume of data full of facts, DHT is recommended to store this type of table. In DHT, a row in the table will be stored in one distribution (node, SQL database). By using hashing function with a column of the table as an input, each rows in a table is assigned to a specific node.

The performance of DHT replies on the skewness of column distribution. It's because the query duration of DHT is as fast as the node storing the highest volume compared to others. 

