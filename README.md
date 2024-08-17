# Face Recognition

## Setup environment

- Python version: **3.12.5**
- Create new python environment
  ```bash
  python -m venv env
  ```
- Activate environment
  - Window:
  ```bash
  .\env\Scripts\activate
  ```
  - Ubuntu / Mac:
  ```bash
  source env/bin/activate
  ```
- Install packages
  ```bash
  pip install -r requirements.txt
  ```
- Setup Redis
  ```bash
  docker compose up
  ```

## Install packages

- To install insightface
- Install this file from link [resources](https://github.com/Gourieff/Assets/tree/main/Insightface)
  ```bash
  insightface-0.7.3-cp312-cp312-win_amd64.whl
  ```
- Active environment and run command
  ```bash
  pip install insightface-0.7.3-cp312-cp312-win_amd64.whl
  ```
