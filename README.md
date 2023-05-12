# CMPE131-Chatmail

Chatmail is a python email client with an integrated chat as well as a todo checklist.

## Contributors

- Johnathon Lu (@KueTone) Team Lead
- Dorian Vail (@Dorianv5)
- Phillip Nguyen (@PhillipNguyenCMPE)
- Ryan Ayoubi (@ryanayoubi)

## Schedule
https://www.when2meet.com/?19639177-KJbMW

## Environment Setup
For Mac devices
1. Install python3
2. Make a virtual environment (Venv)
    1. python3 -m venv venv 
    2. Activate venv
        - For Mac
    ```
        source venv/bin/activate
    ```
        - For Windows 
    ``` 
        venv\Scripts\activate
    ```
3. Install necessary flask packages
```
pip install flask_sqlalchemy
pip install flask_login
pip install flask_wtf
pip install flask_migrate
ip install flask_change_password
pip install requests
pip install PyGithub
```
4. Generate a url
```
    Python run.py
```
## License

MIT
