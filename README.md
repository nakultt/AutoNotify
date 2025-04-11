# AutoNotify

**Expiry Reminder for Important Documents**

## Overview

AutoNotify is a Python-based project designed to help users keep track of important document expiration dates. By providing timely reminders, it ensures that users never miss critical deadlines for document renewals.

## Features

- Add and manage a list of important documents.
- Set custom expiration dates for each document.
- Receive notifications or reminders for approaching deadlines.
- Simple and efficient Python implementation.

## Runing

Users can provide their data by editing the `input_data.yaml` file after forking and adding github secrets(refer workflow yaml files for secrets), and the GitHub Actions workflow will automatically process the input and handle the rest of the tasks seamlessly.

## Input Data File

Provide your data in the `input_data.yaml` file using the following format:

```yaml
# Example of input_data.yaml
documents:
  - name: "Passport"
    expiry_date: "2025-12-31"
  - name: "Driver's License"
    expiry_date: "2024-06-15"
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and open a pull request.

## Contact

For any questions or suggestions, feel free to reach out through GitHub Issues.
