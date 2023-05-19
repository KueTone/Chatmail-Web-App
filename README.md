# CMPE131-Chatmail

Chatmail is a python email client with an integrated chat as well as a todo checklist.

## Requirements

1. **Connect with any external API** (johnathon)
2. Edit User Profiles (johnathon)
3. Login account (johnathon)
4. Delete chat messages (johnathon)
5. Send chat messages (phillip)
6. Create items for checklist (johnathon)
7. Delete Account (johnathon)
8. Block User (dorian)
9. Create account (dorian)
10. **Advance search items with regular expressions or filters by categories** (ryan)
11. Search Chat Messages (ryan)
12. Change Password (johnathon)


## Contributors

- Johnathon Lu (@KueTone) Team Lead
- Dorian Vail (@Dorianv5)
- Phillip Nguyen (@PhillipNguyenCMPE)
- Ryan Ayoubi (@ryanayoubi)

## Schedule
https://www.when2meet.com/?19639177-KJbMW

## Environment Setup

1. Install python3
2. Make a virtual environment (Venv)
```
python3 -m venv venv 
```
3. Activate Virtual Environment
- For Mac
```
source venv/bin/activate
```
- For Windows 
``` 
venv\Scripts\activate
```
4. Install necessary flask packages
```
pip install -r requirements.txt
```
5. For filling / resetting database
- Enter run.py
- Uncomment lines 10-12 to delete current database values, save, then comment back
- Uncomment line 7 to initiate with preset values, save, then comment back
          - Initial database passwords can be found in database.py

6. Generate a url
```
python run.py
```
## License

MIT
