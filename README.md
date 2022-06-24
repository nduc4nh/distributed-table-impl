# distributed-table-impl
Distributed Hashing &amp; Round robin for table design in DWH. This repo is created just for learning purpose.


# SQL Pool

`Azure Synapse`, a service in `Azure Platform`, uses SQL pools as a data warehouse solution. The service provide users with many features: data ingestion, data analytics wrapping around Azure SQL pool. Integrated with Data Storage solution and such sub-services, Azure Synapse follows the modern lakehouse approach in data processing

There are 2 types of SQL pool: `dedicated SQL` pool & `serverless SQL` pool, they're both deployed in distributed manner.

* Dedicated SQL pool: this pool is provisioned when Azure Synapse is first created. with deterministic infrastructure, the cost and workload are predictable and easy to manage

* Serverless SQL pool: this pool is truely a pay as you go service with auto scaling shit and also serve many ad-hoc query in this environment 

# Distributed Table

When data come to SQL dedicated pool, they can be distributingly organized in 3 ways:

1. Hashing
2. Round robin
3. Replicate

Hasing provides good query performance. Rows' locations are deterministic 

Roud robin, well, at least It's good at loading the data

Replicate is the best way when the volume of data is small

# About this repo

I simulated the distributed environment with scalable "nodes" (actually folders). The controller node monitors other nodes and act as a client to execute queries. 

In fact, the deployment architecture of both SQL dedicated & serverless service has 2 components: the control node and a bunch of compute nodes for TSQL execution and also file assginment


```
# load in distributed hash 
python main.py "load"

# save
python main.py "save"
```


