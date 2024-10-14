<h1>Unopim</h1>

**About**

A free and open source Laravel-based PIM software to help businesses organize, manage, and enrich their product data centrally.

GitHub repository: https://github.com/unopim/unopim

<h2>Findings</h2>

<h2>Details</h2>

**Techonogy stack**

-Database: Mysql **(root:password)**

-Framework: Laravel

-Postman API Documentation: https://www.postman.com/unopim/unopim-apis/collection/kzy03uh/official-unopim-apis?ctx=info

<h3>Default credentials</h3>

**johndoe@example.com**:**JohnDoe@123**
![image](https://github.com/user-attachments/assets/88a81be9-06dd-4a27-9589-c1f332265f72)


<h3>.htaccess</h3>

```
RewriteCond %{HTTP:Authorization} .

RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
```

The above rule checks for **Authorization** which is a session token.


```
<FilesMatch ".(jpg|jpeg|gif|png|svg|swf|webp)$">
    <IfModule mod_headers.c>
        Header set Cache-Control "max-age=604800, public"
    </IfModule>
</FilesMatch>
```

The above rule checks for specific media file extentions.

<h2>Test 1: Double extension</h2> 








