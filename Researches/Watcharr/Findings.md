**Watcharr V.1.43.0**

Open source, self-hostable watched list for all your content (movies, tv series, anime, games) with user authentication, modern and clean UI and a very simple setup.

Repository: https://github.com/sbondCo/Watcharr

**Findings**

1. Login Page : User enumeration
2. Account takover : Insufficient Session Expiration
3. Privilege escalation through crafted JWT token

**Bugs**

-Web app allows users to create account with spacebar. For example **" admin"**. This bug creates another account that imitate the existing **admin** account user

**API endpoints**

-Registration: username, password
```
/api/auth/register
```
-Login: username, password
```
/api/auth/
```
-Change password: validate with token
```
/api/auth/change_password
```
-Change notifications: privateThoughts or private or automateShowStatuses or includePreviouslyWatched
```
/api/user/update
```
-Get User profile
```
/api/profile
```
-Follow users & Unfollow users = POST and DELETE
```
/api/follow/<ID>
```





**Details:**

API technology = JWT 

Default database = SQLite3

![image](https://github.com/user-attachments/assets/65cde707-938a-4634-8a00-e57b74c00072)

**JWT Testing(Vulnerable)**

The web app doesn't utilize JWT session. This allows attackers to reuses token to change password.

![image](https://github.com/user-attachments/assets/79bd7932-7004-4bca-bf36-cdc97a82da1a)

![image](https://github.com/user-attachments/assets/c1120f0d-1926-4be4-8c1e-04a70d3ff59a)

**JWT token doesn't have secret key**

![image](https://github.com/user-attachments/assets/64c7e775-82cf-4a6b-88ac-00616daa2222)


**Testing with blank password** 

![image](https://github.com/user-attachments/assets/cf7cfbab-d8cb-4439-a87a-997da21e76e3)

**Use crafted JWT token to verify usability**

![image](https://github.com/user-attachments/assets/8cc1e396-e31b-44c1-a308-e286e8e511b9)

Exploited!

![image](https://github.com/user-attachments/assets/737f551f-50b6-4673-8315-7ca05af3c789)


**Testing on different functions**



In login page, the authenthication mechanism can be abuse to enumerate valid usernames.

**Testing scenario:**

**Valid username but invalid password case**

![image](https://github.com/user-attachments/assets/f20ad2dd-d808-4a1d-ba76-7eecfa91b0b3)

**Invalid username but valid password or invalid password case**

![image](https://github.com/user-attachments/assets/c2a24afd-c6ff-422a-ba79-f617bbcd11e6)

**Valid username and password**

![image](https://github.com/user-attachments/assets/45ae6955-6e3e-4ac5-bb84-3d794cfd3156)





