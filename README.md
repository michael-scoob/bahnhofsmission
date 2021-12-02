# README 

## Create a Virtual Python Environment
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
## Get python path
Run python.exe and script ...

```python
>>> import os
>>> import sys
>>> os.path.dirname(sys.executable)
```

Open CMD and do ..

```bash
cd my-project
virtualenv --python C:\Path\To\Python\python.exe venv
```

## Activate the Environment
```bash
.\venv\Scripts\activate
```
## Doc Streamlit

https://docs.streamlit.io/library/get-started/installation