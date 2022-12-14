# Technical Competency

Please provide brief explanations or answers to the following:

1. Briefly explain what is happening in the `.github/workflows/cfn-lint.yml` file.

On a git push to any branch (but not on tags), the code is checked out and then the python package  `cfn-lint` is used to validate that the `template.yml` in the root of this repository is a valid AWS Cloudformation config file using the [resource specification as a reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html). If this lint check fails, the build job will be marked as a failure.

2. How do you call the `hello_world` function in this repo on your local computer?

Using the SAM CLI, start a local server with `sam local start-api`. This will boot an API server on port 3000 by default, you can then load http://localhost:3000/hello in your browser to execute the function (or use curl, etc). This is also fairly easy to achieve on Github Codespaces using the base python3 image with the AWS SAM and Docker packages selected (which is how I tested this out to keep my local machine clean).

3. Briefly explain what these mysql queries do:

```mysql
mysql -u dbadmin \
  -h sam-hello-world-production.abcd1efg3hijk.us-east-1.rds.amazonaws.com \
  -p dbadminpw \
  -D sam_hello_world_production
```

This query connects to the `sam_hello_world_production` database on the `sam-hello-world-production.abcd1efg3hijk.us-east-1.rds.amazonaws.com` host, as the `dbadmin` user, using the password `dbadminpw`. It should start an interactive mysql shell with the database preselected, allowing you to make any queries possible for the given user.

```mysql
mysql select u.email \
  from users u inner join (select user_id, max(logged_in_at) \
  as latest from user_logins group by user_id) r \
  on u.id = r.user_id where r.latest > '2022-01-01 0:00:00' \
  order by email ASC
```

This is a select statement that is retrieving the email address (in ascending order) of all users who have logged in after the start of 2022.

4. Write out an aws cli command to retrieve an aws secret.

```bash
aws secretsmanager get-secret-value \
    --secret-id MyTestSecret
```
