# DocumentSharingSystemInSwimmy
SwimmyProject No.1: DocumentSharingSystemInSwimmy(DSSS)


## Objective
このプロジェクトはSwimmyの共有業務を効率化することを目的としています。

2025/05/30：
- 生徒名と授業時間から自動的に共有業務を進行する。

## Requirement
- 生徒名と授業時間から、対象データフォルダ内の該当のデータを抽出
- 該当データを適当なGoogleDrive共有フォルダへUpload

## Design

### Structure


DSSS  
共有業務効率化ライブラリ

- \_\_init__.py  

- Application
DSSS core system
  - \_\_init__.py  
  - Setting.py  
  - Main.py  

- HumanIO  
Human interface packages
  - \_\_init__.py  
  - Structure
    - \_\_init__.py
    - Event.py
    - Main.py
  - Pygame  
  Use pygame library I/O
    - \_\_init__.py  
    - Setting.py  
    - Main.py  

- FileIO  
File control packages
  - \_\_init__.py  
  - Local
  Local file system package
    - \_\_init__.py  
    - Setting.py  
    - Main.py  
  - GoogleDrive  
  Google drive file package
    - \_\_init__.py
