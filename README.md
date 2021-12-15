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

### Instatlatio
https://docs.streamlit.io/library/get-started/installation

### API Ref
https://docs.streamlit.io/library/api-reference

## Page setup 
https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/

https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config

## Widgets
https://docs.streamlit.io/library/api-reference/widgets

# Connect Streamlit to PostgreSQL
https://docs.streamlit.io/knowledge-base/tutorials/databases/postgresql

# How to Add A Login & Sign-up Section 
https://blog.jcharistech.com/2020/05/30/how-to-add-a-login-section-to-streamlit-blog-app/

# How to Streamlit in Docker
https://www.section.io/engineering-education/how-to-deploy-streamlit-app-with-docker/