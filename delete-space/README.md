# Delete spaces
 
[![python39](https://img.shields.io/badge/python-3.9-green?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 
## Table of Contents

- [Delete spaces](#delete-spaces)
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
 
---
 
## About

This module is used to delete spaces - that are marked for deletion at least 7 days ago from a database.

## Getting Started
 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Install Python > 3.
* A running [organizationmanager](https://github.com/EFS-OpenSource/superb-data-kraken-organizationmanager)-instance
* A running OIDC/OAuth2 provider instance with a confidential Client, having a Service Account with permissions to delete indices from OpenSearch

### Installing

Execute the following steps to setup your local environment for development and testing:

- Clone the repository
- Install the required packages via ```pip install -r requirements.txt```

 
## Usage

Commands that are required in order to use the service.

Use the module in another python script with ```pip install -r requirements.txt```


## Built With

Links to tools used for building. 

* Python v3.9 (see this [Link](https://www.python.org/))


## Deployment

### Environment Variables

The following environment variables are required:

* `ACCESS_TOKEN_URI`: Token-Uri
* `ORGANIZATIONMANAGER_URL`: Url to access the organization manager

## Contributing

See the [Contribution Guide](/CONTRIBUTING.md).

## Changelog
 
See the [Changelog](/CHANGELOG.md).

## Documentation

If a space should be deleted, it is merely marked for deletion, which means, that the space should be deleted, however it is not done immediately, therefore a user has a couple of days, to undo this action. If a certain amount of time is passed (at least 7 days), the space will be deleted. This includes the space itself and all connected resources (like roles, storage, analysis, metadata etc.). 