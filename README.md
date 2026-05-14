[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

<br />
<div align="center">
  <h3 align="center">Library Manager</h3>

  <p align="center">
    A very good FastAPI project that helps you to organize your books
    <br />
    <a href="https://github.com/geekmanesh/library-manager-fastapi"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/geekmanesh/library-manager-fastapi">View Demo</a>
    &middot;
    <a href="https://github.com/geekmanesh/library-manager-fastapi/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/geekmanesh/library-manager-fastapi/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

Library Management API is a RESTful web service built with FastAPI for managing book collections in a library system.
It provides a clean, efficient interface to perform CRUD operations on books, track availability, and manage library inventory.

### Built With

Python
FastAPI
SQLite3

## Getting Started

### Prerequisites

First, you need to install/have these tools
```sh
python
pip
```

### Installation

Let's install and run the project

1. Clone the repo
```sh
git clone https://github.com/geekmanesh/library-manager-fastapi.git
```

2. Move to project directory
```sh
cd library-manager-fastapi
```

3. Install dependencies with pip
```sh
pip install -r requirements.txt
```

4. Run the project
```sh
uvicorn run main:app --reload
```

5. Now you can go to http://127.0.0.1:8000/ on your favorite browser

## Usage

When you run the project successfully, you can go to /docs or /redoc page and exploring in endpoints

Key Features:
- login and register
- full CRUD for your books
- search in you books

## Contributing

You can contribute to this project with suggest features, report bugs and issues or even write code for this project
for more information you can take look at my [contributing guidelines](/CONTRIBUTING.md)

## License

Distributed under the [MIT](/LICENSE) License.

## Contact

Hamid Geekmanesh - dimah.code@gmail.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/geekmanesh/library-manager-fastapi.svg?style=for-the-badge
[contributors-url]: https://github.com/geekmanesh/library-manager-fastapi/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/geekmanesh/library-manager-fastapi.svg?style=for-the-badge
[forks-url]: https://github.com/geekmanesh/library-manager-fastapi/network/members
[stars-shield]: https://img.shields.io/github/stars/geekmanesh/library-manager-fastapi.svg?style=for-the-badge
[stars-url]: https://github.com/geekmanesh/library-manager-fastapi/stargazers
[issues-shield]: https://img.shields.io/github/issues/geekmanesh/library-manager-fastapi.svg?style=for-the-badge
[issues-url]: https://github.com/geekmanesh/library-manager-fastapi/issues
[license-shield]: https://img.shields.io/github/license/geekmanesh/library-manager-fastapi.svg?style=for-the-badge
[license-url]: https://github.com/geekmanesh/library-manager-fastapi/blob/master/LICENSE
