# README 
This is an app for recording visitors to the station mission in Germany. The aim of the app is to simplify the manual recording of visitors and services on paper and to enable the data to be exported. 

## Information about the Bahnhofsmission
https://de.wikipedia.org/wiki/Bahnhofsmission


# Licence
## "THE BEER-WARE LICENSE" (Revision 42):
<michae@scoob-innovation.de> wrote this file. As long as you retain this notice you can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return 

# Dev Doc

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