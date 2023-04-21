# Functional Requirements

1. **Connect with any external API** (johnathon)
2. Edit User Profiles
3. Login account
4. **Add ability to attach images to emails/ chat** (phillip)
5. Send/unsend email
6. Create items for checklist
7. **Visualize Email Transmissions** (dorian)
8. Change Account
9. Create account
10. **Advance search items with regular expressions or filters by categories** (ryan)
11. Search Messages
12. Change Password

## Non-functional Requirements

1. Only expected to work on Google Chrome
2. **Multilingual Support**

## Use Cases

### **Use Case: Update User Profile Using Github API**

- **Pre-conditions:**

  - The user is logged into the chat site
  - The system is connected to the Rest API

- **Trigger:**

  - The user clicks "Connect to Github" to connect their accouct

- **Primary Sequence:**

  1. The user navigates to their profile
  2. The user selects the option "Connect to Github"
  3. The system sends a GET request to the GitHub REST API, passing the user's GitHub username as a parameter
  4. The GitHub API processes the request and returns information about the user's GitHub profile, including their name, bio, number of followers, and other details
  5. The chat site displays this information to the user by updating their profile

- **Primary Post-conditions:**

  - The user is able to view/edit their GitHub profile information on the chat site.

- **Alternate Sequence:**

  1. If the GitHub API is unavailable or returns an error, the chat site displays an error message and prompts the user to try again later.
  2. If the user enters an invalid or non-existent GitHub username, the chat site displays an error message and prompts the user to enter a valid username.

### **Use Case: Edit User Profiles**

- **Pre-condition:**

  - The user has already created an account
  - The user is logged into their account

- **Trigger:**

  - The user initiates the change using a "Edit Profile" button

- **Primary Sequence:**

  1. The user navigates to their profile
  2. The user selects the option "edit their profile"
  3. Chatmail displays a form with the user's current information pre-populated in the fields
  4. The user updates their profile information as desired, such as changing their name or profile picture
  5. The user saves their changes by clicking a save button
  6. Chatmail saves it to the database
  7. Chatmail application displays the new information

- **Primary Postconditions:**

  - The user's profile information has been updated with the new information.

- **Alternate Sequence:**

  1. If Chatmail is unable to save the information due to conflicts such as username conflict, it will display an error message saying "username already taken"

### **Use Case: Login/Logout Account**

- **Pre-condition:**

  - There are multiple accounts in database
  - The user's account information is stored in the database.

- **Trigger**

  - The user initiates the process by clicking "Login"

- **Primary Sequence**

  1. The user opens the login page of the system.
  2. The system prompts the user to enter their username and password.
  3. The user enters their username and password.
  4. The system validates the user's credentials by checking them against the account information stored in the database.
  5. If the credentials are valid, the system logs the user into their account and redirects them to the homepage of the system.

- **Primary Postconditions:**

  - The user successfully logs into their account is now able to chat and use all the other features.

- **Alternate Sequence:**

  1. If the credentials are invalid, the system displays an error message to the user and prompts them to try again.
  2. If the system cannot validate the user's credentials due to a database error or other issue, it displays an error message to the user and prompts them to try again later.
  3. If the user enters incorrect credentials multiple times, the system may lock their account or temporarily prevent them from attempting to log in again for security reasons. The system may also prompt the user to reset their password.

### **Use Case: Visualize Email Transmissions**


- **Pre-condition:** User has sent an Email

- **Trigger:** The User has sent an email

- **Primary Sequence:**

  1. The user selects the option to send a message
  2. The system confirms that the message has been sent
  3. An animation plays to show the user that the sending was successful
  4. The Animation ends and closes the draft of the message that was sent

- **Primary Postconditions:** The User is returned to the page they were on before drafting the email

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>

  1. If the Message send doesnt go through, an alternate animation will play
  2. Then an error prompt will pop up to let the user know that the message was unable to send


### **Use Case: Log Out of Account**


- **Pre-condition:** The User is signed in to their account.

- **Trigger:** The User selects the option to log out.

- **Primary Sequence:**

  1. The user is prompted to confirm that they want to log out.
  2. Once logged out, the user is sent to the home page of the website.

- **Primary Postconditions:**

  1. The user is signed out and able to sign into other accounts
  2. The user is able to sign into other accounts

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>

  1. if there is an issue logging the user out, the system can show an error method

### **Use Case: Create Account**

- **Pre-condition:** The User has a valid username and password

- **Trigger:** The User selects the option to create an account

- **Primary Sequence:**

  1. The user is prompted to enter their username and password that will be used for their account
  2. The user confirms their information by pressing create account
  3. The system will create an empty account with their login credentials
  4. The system will open up the home page after logging in to their account

- **Primary Postconditions:**

  1. The user is signed in to their account and can email other users
  2. The user is able to sign back out

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>

  1. If there is an issue with either the username or password provided, the system will show an error
  2. If there is another user with the same username, the system will ask if they are an already existing user.

### **Use Case: Attaching Images to Emails/Chat**

- **Pre-condition:**

  - User has an account and is logged in

- **Trigger:**

  - User has selected the option to “Compose” an email or to “Chat”

- **Primary Sequence:**

  1. The user opens the option to compose an email or chat with user(s)
  2. User selects the attach image option
  3. System prompts user to copy paste the image’s URL in a text box or to insert a file of the image
  4. If the user selects the file insertion option, the system will open the user’s file explorer for them to select a file of the image
  5. System checks if the URL or file is valid
  6. System uploads the image in the email or chat if the URL or file is valid

- **Primary Post-conditions:**

  - User can delete the image or file or upload the image through email or chat

- **Alternate Sequence:**

  1. If the URL does not generate an image, the system will display an error message regarding the validation of the URL
  2. If the file is not the correct type (JPEG, JPG, PNG), the system will display an error message regarding the file type
  3. If the size of the file is too large, the system will display an error message regarding the size of the file and the maximum capacity

### **Use Case: Sending Email**

- **Pre-conditions:**

  - User has an registered account and is logged in

- **Trigger:**

  - User has selected the “Compose” email option

- **Primary sequence:**

  1. User opens up the email composition text box
  2. User types in the recipient’s email address
  3. User enters in the contents of the email message
  4. User clicks “Send” to send the email to the recipient

- **Primary Post-conditions:**

  - The recipient can see the email that was sent to them in their box
  - The user can check if their email was sent or not

- **Alternate Sequence:**

  - If the email address entered for the recipient does not exist, the system will display an error message regarding the mismatched email input

### **Use Case: Create Items for Checklist**

- **Pre-condition:**

  - User has an registered account and is logged in

- **Trigger:**

  - User has selected “Checklist” option

- **Primary Sequence:**

  1. User arrives at the Checklist page
  2. User can navigate through a calendar to select a month and day for their checklist
  3. User can type things to do in a list format
  4. User can also input extra notes in a text box at the top of the list
  5. After finishing the items for the checklist, user can save the list or choose to cancel it
  6. If user chooses to save the checklist, system will prompt user to name the checklist

- **Primary Post-conditions:**

  - User has created and named a checklist on a calendar
  - User can access that checklist and place or remove check markings on each item
  - User can access checklist and add or remove items
  - User can delete checklists from the calendar

- **Alternate Sequence:**

  - If the user’s item or title exceeds the maximum number of characters, the system will prompt an error message stating that the maximum number of characters has been reached

### **Use Case: Search Messages**

- **Pre-conditions:**

  - The user is logged into the chat site

- **Trigger:**

  - The user selects the search field

- **Primary Sequence:**

  1. User enters String or Regex they want to search for
  2. User selects any additional filters
  3. Website displays any messages that contain what the user inputted

- **Primary Post-conditions:**

  - The user is able to view any of the messages that fit their search criteria

- **Alternate Sequence:**

  1. User searches for something not contained in any messages
  2. Website displays no messages

### **Use Case: Change Password**

- **Pre-condition:**

  - The user has already created an account
  - The user is logged into their account

- **Trigger:**

  - The user selects “Change Password” in their profile settings

- **Primary Sequence:**

  1. The system prompts the user to enter their previous password and a new password twice
  2. The user fills out the form, meeting whatever requirements the website has for password strength
  3. The user confirms their input when they have decided on a new password
  4. The system saves the users input as their new password

- **Primary Postconditions:**

  - The user's password has been changed

- **Alternate Sequence:**

  1. The user’s input for the new password is not the same in both text fields
  2. The system does not allow them to confirm their decision and change their password.
