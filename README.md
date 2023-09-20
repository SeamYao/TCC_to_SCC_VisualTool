# Visual tool for converting traditional Chinese characters to simplified Chinese characters

# 一、Pip Install
### 1. Core library for traditional and simplified Chinese conversion
```bash
pip install zhconv
```
### 2. GUI library
```bash
pip install PyQt5
```
### 3. EXE generation library
Used for generating an executable file, optional installation
```bash
pip install pyinstaller
```
If you want to generate an EXE file, navigate to the file directory in the command prompt and enter the following code:
```bash
pyinstaller -F -w  TCC_to_SCC_VisualTool.py --add-data="resource;."
```

# 二、Special File Explanation

### 1. "resource/zhcdict.json" Retrieved from the zhconv library's zhcdict.json
