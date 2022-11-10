# dashboard-streamlit
HHA-507 // Assignment #10



---

# Installing & Setting Up Streamlit:
## Install Pipenv

```
python -m ensure pip --upgrade

pip3 install pipenv
```

## Create a new environment with Streamlit

```
cd myproject

pipenv shell

pipenv install streamlit

streamlit hello
```

## Use your new environment

```
pipenv shell

streamlit run myfile.py
```
```
# Running
$ python -m streamlit run your_script.py

# is equivalent to:
$ streamlit run your_script.py
```