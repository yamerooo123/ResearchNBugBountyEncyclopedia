**Watcharr**

Open source, self-hostable watched list for all your content (movies, tv series, anime, games) with user authentication, modern and clean UI and a very simple setup.

Repository: https://github.com/sbondCo/Watcharr

Finding

1. Login Page : User enumeration


**Details:**

Default database = SQLite

![image](https://github.com/user-attachments/assets/65cde707-938a-4634-8a00-e57b74c00072)


In login page, the authenthication mechanism can be abuse to enumerate valid usernames.

**Testing scenario:**

**Valid username but invalid password case**

![image](https://github.com/user-attachments/assets/f20ad2dd-d808-4a1d-ba76-7eecfa91b0b3)

**Invalid username but valid password or invalid password case**

![image](https://github.com/user-attachments/assets/c2a24afd-c6ff-422a-ba79-f617bbcd11e6)

**Valid username and password**

![image](https://github.com/user-attachments/assets/45ae6955-6e3e-4ac5-bb84-3d794cfd3156)





