# Functional Requirements

1. **Connect with any external API** (johnathon)
2. Edit User Profiles
3. Login account
4. **Add ability to attach images to emails/ chat** (phillip)
5. Send/unsend email
6. Create items for checklist
7. **Visualize Email Transmissions** (dorian)
8. Change Account
9. Signup account
10. **Advance search items with regular expressions or filters by categories** (ryan)
11. Search Messages
12. Change Password

## Non-functional Requirements

1. **UI interactive interface (or using elements from bootstrap)**
2. Only expected to work on Google Chrome
3. **Multilingual Support**
4. Only expected to work on computer screen (not mobile compatible)

## Use Cases

### **Use Case: Connect with Github Rest API**

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

### **Use Case: Login Account**

- **Pre-condition:**

  - The user has an account with the system and the account information is stored in the database.

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
