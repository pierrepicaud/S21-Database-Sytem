# Lab 12 Report 

## Commands

ZADD orders 1005 "1005 4 12/15/09 565.00"
ZADD orders 1006 "1006 6 11/22/09 25.00"
ZADD orders 1007 "1007 6 10/8/09 85.00"
ZADD orders 1008 "1008 6 12/29/09 109.12"
ZADD orders 1001 "1001 2 10/10/09 250.85"
ZADD orders 1002 "1002 2 2/21/10 125.89"
ZADD orders 1003 "1003 3 11/15/09 1567.99"
ZADD orders 1004 "1004 4 11/22/09 180.92"

ZADD customers 1 "1 Jane Doe"
ZADD customers 2 "2 John Doe"
ZADD customers 3 "3 Jane Smith"
ZADD customers 4 "4 John Smith"
ZADD customers 5 "5 Jane Jones"
ZADD customers 6 "6 John Jones"


## Outputs

$ redis-cli -h redis-10173.c251.east-us-mz.azure.cloud.redislabs.com -p 10173 -a "5MYrDDYq2LdrB6yjYAkrDvBQHOx5Amoc"

redis-10173.c251.east-us-mz.azure.cloud.redislabs.com:10173>> ZRANGE orders 0 10000
1) "1001 2 10/10/09 250.85"
2) "1002 2 2/21/10 125.89"
3) "1003 3 11/15/09 1567.99"
4) "1004 4 11/22/09 180.92"
5) "1005 4 12/15/09 565.00"
6) "1006 6 11/22/09 25.00"
7) "1007 6 10/8/09 85.00"
8) "1008 6 12/29/09 109.12"

redis-10173.c251.east-us-mz.azure.cloud.redislabs.com:10173> ZRANGE customers 0 10000
1) "1 Jane Doe"
2) "2 John Doe"
3) "3 Jane Smith"
4) "4 John Smith"
5) "5 Jane Jones"
6) "6 John Jones"

redis-10173.c251.east-us-mz.azure.cloud.redislabs.com:10173>>
