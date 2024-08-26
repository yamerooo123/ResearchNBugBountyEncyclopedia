Researched by: Suphawith Phusanbai (Security Researcher)

**WP Job Manager Plugin v.2.4.0**

Manage job listings from the WordPress admin panel, and allow users to post jobs directly to your site.

Sourcecode: https://github.com/Automattic/WP-Job-Manager/releases/tag/2.4.0

**Details**

The plugin function sourcecode can be found in **wp-job-manager-functions.php**

- The plugin is required WordPress version 6.4 at minimum. 

- The plugin uses raw sql command in seach bar but with **esc_sql()** and **$wpdb->prepare** to avoid sql injection risk.

**esc_sql() Example**

| Example   |
| -------------  |
| $unsafe_variable = "'; DROP TABLE wp_users; --";|
| $query = "SELECT * FROM wp_posts WHERE post_title = '$unsafe_variable'";|

Without esc_sql(), the $unsafe_variable which is the user input will be query as string which is not sanitized, leading to sql injection.
By applying esc_sql(), this Wordpress function escape the special characters that could lead to sql injection such as "". 

The result is the query command contains only text and no escaping characters, making sql injection payloads are likely to fail.

However, since esc_sql() doesn't considered % as escaping characters, the attacker can still use encoding technique. But with the help of **$wpdb->prepare**, it completely mitigates sql injection. The earlier function assign placeholders to query input, these placeholders tell the database to treat the query input using the following placeholders;


| Placeholder(s)   | Definition |
| -------------  | -------------  |
| Strings (%s)| esc_sql() query input(sanitized) |
| Integers (%d  | Only numeric values are accepted|
| Floating-Point (%f)  | Only floating values are accepted |

![image](https://github.com/user-attachments/assets/a4c38111-a61e-4895-bed3-80bfb229efc8)

- The file upload function **job_manager_prepare_uploaded_files** checks MIME type using **wp_check_filetype**. This means it can be bypass by manipulating **Content-Type** in the request using Burp Suite.

![image](https://github.com/user-attachments/assets/0f142dd2-7ef8-4b25-9cca-6ea2f5d420ac)


Normally the image couldn't be executed. Plus, there is **wp_check_filetype** which checks the file extension.

![image](https://github.com/user-attachments/assets/b49ec8a0-b33e-49f1-831d-6fc42ae8bde2)


-------------------------------------------------------------WILL BE MORE DETAIL AFTER I GOT MY CVE PUBLISH------------------------------------------------------------------
  
 
