# Deploying

This function could be deployed a number of ways, but given it is part of our CloudFormation template, we could use the aws cli to deploy from the template file:

```bash
aws cloudformation deploy \
  --template ./template.yml \
  --stack-name my-new-stack \
```
