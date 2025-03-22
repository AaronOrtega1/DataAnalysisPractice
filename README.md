# Online Retail Exploratory Data Analysis

## Overview

This project focuses on performing exploratory data analysis (EDA) on an online retail dataset sourced from [Kaggle](https://www.kaggle.com/datasets/rohitmahulkar/online-retails-sale-dataset/data). The goal is to preprocess the data, analyze it, and gain insights into customer behavior and sales trends.

The analysis is inspired by a [Kaggle notebook](https://www.kaggle.com/code/ahmedhammad01/beginner-friendly-eda-fp-growth-algorithm), but with modifications and additional insights based on my knowledge from data analysis course I took in my university.

---

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Docker Compose**: Docker Compose is usually included with Docker Desktop.

### Running the Project with Docker

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Build and start the Docker container:

```bash
docker compose up -d --build
```

**In this step is important to wait a little bit for docker to build the container and install the required dependencies**

3. In Linux you can use the following command to get the token, which you can use to connect in VsCode to the python kernel used in the container, or copy the full URL to open jupyter notebooks in any browser.

```bash
docker container logs jupyter_python 2>&1 | grep "token"
```

You should get a link like the following if everything is already installed if not wait a little bit and try again:

```
http://127.0.0.1:8888/?token=your_token_here
```

4. To remove the container you run:

```bash
docker compose down
```
