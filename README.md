# PROG8850 Assignment 4 - Suman Jakhar

## Description
This project shows how to use Flyway with Ansible and GitHub Actions to manage a MySQL database migration for a subscribers database.

## Technologies
- Flyway
- Ansible
- GitHub Actions
- MySQL
- Python + unittest

## How to Run Locally
1. Install Flyway
2. Run:
```bash
flyway -url=jdbc:mysql://localhost:3306/subscribersdb -user=root -password=pass -locations=filesystem:migrations migrate
