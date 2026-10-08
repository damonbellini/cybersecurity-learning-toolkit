# TryHackMe: Complimentary

## Overview

Room: Complimentary  
Platform: TryHackMe  
Category: Cloud Security  
Difficulty: Easy  
Focus: AWS Cognito, IAM misconfiguration and DynamoDB access

## What I learned

This lab demonstrates how a cloud application can expose data when authentication and authorization are designed incorrectly.

The application does not present a normal login flow. Instead, the important question is what AWS mechanism is quietly providing the application with credentials and what permissions those credentials receive.

The room focuses on tracing the AWS credential mechanism, understanding the permissions attached to the temporary credentials and checking whether the backend enforces access control correctly.

## Key concepts

### AWS Cognito

Amazon Cognito can provide application users with temporary AWS credentials. Those credentials can then be used to access AWS resources according to the permissions granted to the identity.

### IAM least privilege

Cloud identities should receive only the permissions required for their intended task. A credential that can read unrelated users' data represents an authorization failure and potentially a serious data exposure.

### DynamoDB

DynamoDB is a NoSQL database service on AWS. In this lab, the important security question is whether the application can access records beyond the currently authorised user.

### Authentication vs authorization

Authentication answers who the user is.

Authorization answers what that user is allowed to access.

A system can have a working authentication mechanism and still be vulnerable if authorization is missing or incorrectly enforced.

## Lab methodology

1. Inspect how the application obtains AWS credentials.
2. Identify the AWS identity and permissions associated with those credentials.
3. Determine which backend resource is accessible.
4. Test whether access is limited to the intended user's record.
5. Document the security impact and the required least privilege controls.

## Defensive takeaway

Cloud applications should enforce authorization at the backend and use narrowly scoped IAM policies. Client-side restrictions are not sufficient because an attacker can directly use credentials or API calls available to the application.

Only perform these tests against the authorised TryHackMe lab environment.

## Status

Completed study notes for the cloud security concepts demonstrated by this room.
