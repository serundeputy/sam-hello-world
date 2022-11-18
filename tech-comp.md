# Technical Competency

Please provide brief explanations or answers to the following:

1. Briefly explain what is happening in the `.github/workflows/cfn-lint.yml` file.

2. How do you call the `hello_world` function in this repo on your local computer?

3. Briefly explain what these mysql queries do:

```mysql
mysql -u dbadmin \
  -h sam-hello-world-production.abcd1efg3hijk.us-east-1.rds.amazonaws.com \
  -p dbadminpw \
  -D sam_hello_world_production
```

```mysql
mysql select u.email \
  from users u inner join (select user_id, max(logged_in_at) \
  as latest from user_logins group by user_id) r \
  on u.id = r.user_id where r.latest > '2022-01-01 0:00:00' \
  order by email ASC
```

4. Write out an aws cli command to retrieve an aws secret.
