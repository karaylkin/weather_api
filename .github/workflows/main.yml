name: weather_api52

on:
  push:
    branches:
      - main  # Запускать процесс публикации при пуше в ветку main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
        
    - name: Build package
      run: python -m build --no-isolation

    - name: Publish to Test PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.pypi-AgENdGVzdC5weXBpLm9yZwIkMjNiZTc3NWMtY2QzNy00MzAxLWE1M2EtOWRlMGNiNWI4NTYyAAIqWzMsIjdlZjI1OTViLTE4ODYtNDg1My1hZjdiLWI5MDkyYzgwZDI4OSJdAAAGIIFKUyt6FTpRsl5LwNDJYeO2s3w4xsWT5SJcJnH96cmn }}
      run: twine upload --repository testpypi dist/*

