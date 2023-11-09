# Combined Generator Tool by MAKHLWF

[![License](https://img.shields.io/github/license/makhlwf/Combo-generator-)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/makhlwf/Combo-generator-)](https://github.com/makhlwf/Combo-generator-/commits)

A powerful tool crafted by [@makhlwf](https://t.me/makhlwf) for seamless proxy and email/password pair generation.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [License](#license)

## Features

- **Proxy Generation:** Easily create a list of proxy IP addresses.
- **Email/Password Generation:** Generate secure email and password pairs with customizable password strength.
- **User-Friendly Menu:** Intuitive menu for selecting desired functionality.

## Prerequisites

- Python 3.x
- [tqdm](https://github.com/tqdm/tqdm) (for progress bars)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/makhlwf/Combo-generator-.git
   cd Combo-generator-
   ```

2. Install the required Python packages:

   ```shell
   pip install tqdm
   ```

## Usage

1. Start the tool by running the following command in the tool's directory:

   ```shell
   python Main.py
   ```

2. Choose between proxy generation, email/password generation, or exit the tool.

## Options

- **Proxy Generator**
  - Enter a filename to save the generated proxies.
  - Specify the number of proxies to generate.

- **Email and Password Generator**
  - Specify the number of email/password pairs to generate.
  - Set the desired password length.
  - Choose a filename to save the generated pairs.

- **Exit**
  - Select this option to gracefully exit the tool.

## License

This project is licensed under the [MIT License](LICENSE).