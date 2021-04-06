# Report

## Task 1
**READ COMMITTED**
Terminal 1:
```postgres=# begin;
BEGIN
postgres=# select user_name, balance from pre_exercise;
                 user_name                  | balance 
--------------------------------------------+---------
 bitdiddl                                   |      65
 mike                                       |      73
 bbrown                                     |     100
 alyssa                                     |      79
 jones                                      |      82
(5 rows)

postgres=# 
```

Terminal 2:
```postgres=# begin;
BEGIN
postgres=# update pre_exercise set user_name = 'ajones' where user_name = 'jones';
UPDATE 1
postgres=# select user_name, balance from pre_exercise;
                 user_name                  | balance 
--------------------------------------------+---------
 bitdiddl                                   |      65
 mike                                       |      73
 bbrown                                     |     100
 alyssa                                     |      79
 ajones                                     |      82
(5 rows)

postgres=# 
```

- They show the same info. Terminal 2 hasn’t committed the transaction, the changes is not visible to other transactions


**REPEATABLE READ**
- They do show the same info. Terminal 2 hasn’t committed the transaction. Attempt to update balance from the first terminal gets an error.

## Task 2
**READ COMMITED**
- Only bob’s balance was updated
**REPEATABLE REA**
- Haven't tried

## Task 3
**REPEATABLE READ**
- Mike’s balance was doubled.
- T1 works only with mike’s account.

**SERIALIZABLE**
- ...   


