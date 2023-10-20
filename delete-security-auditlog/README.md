# Delete security-auditlog
 
[![python39](https://img.shields.io/badge/python-3.9-green?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
## Table of Contents

- [Delete security-auditlog](#delete-security-auditlog)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
  - [Usage](#usage)
  - [Built With](#built-with)
  - [Deployment](#deployment)
    - [Environment Variables](#environment-variables)
  - [Contributing](#contributing)
  - [Changelog](#changelog)
  - [Documentation](#documentation)

## About
 
This module may be used to delete outdated security-auditlogs from within OpenSearch.
 
## Getting Started
 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Install Python > 3.
* A running [OpenSearch](https://opensearch.org/)-instance
* A running OIDC/OAuth2 provider instance with a confidential Client, having a Service Account with permissions to delete indices from OpenSearch

### Installing

Execute the following steps to set up your local environment for development and testing:

- Clone the repository
- Install the required packages via ```pip install -r requirements.txt```

 
## Usage

Commands that are required in order to use the module.

## Built With

Tools used for building. 

* Python v3.10 (see this [Link](https://www.python.org/))

## Deployment

### Environment Variables

The following environment variables are required:
  
* `ACCESS_TOKEN_URI`: Token-Uri
* `CLIENT_ID`: id of the confidential oauth-client
* `CLIENT_SECRET`: secret of the confidential oauth-client
* `OPENSEARCH_URL`: Url of the OpenSearch-Installation
* `INDICES_TO_KEEP`: number of indices that should be kept

## Contributing

See the [Contribution Guide](./CONTRIBUTING.md).

## Changelog
 
See the [Changelog](./CHANGELOG.md).
 
## Documentation
 
In order to keep the number of indices at a reasonable number, this worker provides a functionality to delete auditlog-indices within OpenSearch.
