Researched by: Suphawith Phusanbai (Security Researcher)

**MONASH.EDU (PATCHED)**

Our academics, students, staff, alumni and donors make up a community of change makers. Using AI tools, we re-created a version of our community’s younger selves to listen to their stories, and help them answer the age-old question: would your younger self be proud?
Whether you want to change your life, your career, your community, or the future, it starts at Monash. Make your change at Monash.

Website: https://www.monash.edu/

**Findings**

1. Valid usernames can be enumerated through customed WordPress author URL parameter where the developer prevents the enumeration by simple mechanism. For example http://example.com/author=0 will redirect the request to the homepage to prevent the administrator username expose to the public. However, if we change the author query parameter to something else, it will return valid posts that display author names.

**Details**

The WordPress website implements REST API which API resouces that revealed users can be accessed through the following;

http://example.com/wp-json/wp/v2/users

http://example.com/wp-json/wp/v1/users

or 

http://example.com/author=1

![image](https://github.com/user-attachments/assets/c1494454-1808-42c6-9123-3ef50e80641e)


