# Namacheko Pieces

- Looks at Namacheko website to see if there any new pieces
- You will need to change the `url` in the main for future seasons, currently it is `aw21`

## Instructions

- Remember to install selenium chrome driver

### Setup up a virtual environment in your root directory and run main script

  - `virtualenv ./venv`
  - `./venv/scripts/activate`
  - `python main.py`

- Install requirements

  - `pip install -r requirements.txt`

- Run main script
  - `python main.py`


- Set up Task Scheduler (Windows OS)
  - In a powershell file (.ps1)
    - `$Path = "root folder path here"`
    - `cd $Path`
    - `./venv/scripts/activate`
    - `python main.py`

  - After setting up generic settings in the Task Scheduler, IE (Run whether user is logged in or not, run a program, set up dates, etc), we need to setup the Actions.
  - Action: 
    - Start a program
  - Details:
      - Program/scripts: 
        - `"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"`
      - Add arguments (optional):  
        - -ExecutionPolicy Bypass 'my folder where the .ps1 file is', here you want locate the powershell script
      - Start in (optional): 
        - 'root folder' , here you want to locate the root folder for the script
