# AWS Lambda CI/CD with GitHub Actions

This repository contains an AWS Lambda function with two very simple **GitHub Actions** workflows for continuous integration and deployment.

## Workflows

### 1. Update Lambda Function

This workflow automatically updates the AWS Lambda function when changes are pushed to the main branch.

**Trigger:**
- Push to the `main` branch

**Actions:**
- Checks out the code
- Sets up Python
- Installs dependencies
- Zips the function code
- Authenticates with AWS
- Updates the Lambda function

### 2. Run Tests on Pull Requests

This workflow runs tests automatically when a pull request is opened or updated.

**Trigger:**
- Pull request to the `main` branch

**Actions:**
- Checks out the code
- Sets up Python
- Installs dependencies
- Runs pytest

## Setup

To use these workflows, ensure you have:

1. AWS credentials stored as GitHub secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_LAMBDA_FUNCTION_NAME`
2. The correct AWS region set in the workflows
3. The correct Lambda function name set in the update workflow