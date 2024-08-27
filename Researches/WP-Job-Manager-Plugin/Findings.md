Researched by: Suphawith Phusanbai (Security Researcher)

**WP Job Manager Plugin v.2.4.0 (DUPLICATE)**

Manage job listings from the WordPress admin panel, and allow users to post jobs directly to your site.

Sourcecode: https://github.com/Automattic/WP-Job-Manager/releases/tag/2.4.0

**Findings**

1. **The_company_video** function may need to implement URL sanitization. The URL input doesn't validate URLs. This causes the attacker to be able to add XSS PDF files in the link instead of video files. If users accidentally click on the link, it could  trigger XSS vulnerability and lead to additional security issues such as social engineering, credential stealing, etc.

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

- The file upload function **job_manager_prepare_uploaded_files** checks MIME type using **wp_check_filetype**. This means it can be bypass by manipulating **Content-Type** in the request using Burp Suite. Howver, the plugin has allowed-MIME type list which will be compare again with WordPress function, this makes it impossible to upload other file variations. There is also data sanitization mechanism that detecting double extensions. For example **test.php.jpg**., upon detecting will be changed to **test.php_.jpg**. 

![image](https://github.com/user-attachments/assets/2191fd63-ad57-4522-98f1-c03d085e9ed4)
![image](https://github.com/user-attachments/assets/e5fa866c-6674-4e0a-b8f8-3e54580a795d)

- The plugin implemented **wp_oembed_get()**, the function allows WordPress to fetch embedded HTML in **the_company_video** function which the attacker could use this to trigger XSS or force a connection in the external link.

![image](https://github.com/user-attachments/assets/edbfb7d5-eba3-4e67-a08e-2b1d2005fede)

![image](https://github.com/user-attachments/assets/ae11a8e1-f671-4722-993d-e5dec4e58801)








  
 
