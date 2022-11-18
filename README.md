# sam-hello-world

These are some basic tasks so we can assess you know some technologies needed for the role.

## Basic Tech Competancy

1. Create a public GitHub repo with this code
2. Create a feature branch called `techComp`
3. Add answers and explanations in the `tech-comp.md` file
4. Commit your code
5. Push up your branch and file a pull request (PR) with your answers

## Add a new function

1. Create a branch called `get_secret`
2. Add a new function called `GetSecretFunction`to the `template.yaml` file
  * Add code to your new `get_secret` function to make an API call to AWS to retrieve an AWS secret given the name of the secret.
  * The code should be valid python
    * We just want to read the code
    * It does not need to authenticate to any real AWS account, but should demonstrate making an API call to AWS api.
3. Create a `readme.md` file in the new directory for your function.
  * Outline in the `readme.md` file how you would deploy this new function.
    * It doesn't have to be an exhaustive document just a psuedo code list style of what you would do to deploy this new function to AWS infrastructure.
4. Add and commit your code to your feature branch.
5. Push up your code and file a pull request.


## AWS SAM Docs

Read the [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) docs.


## Write up an Architectural Decision Record (ADR)

Read the fictional scenario in the `adr/README.md` and write an ADR that we can potentially discuss in an interview.