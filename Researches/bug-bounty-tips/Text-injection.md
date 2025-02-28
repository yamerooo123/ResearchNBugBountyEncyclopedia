Text Injection/Content Spoffing
---

1. Visit a NASA Subdomain: Start by visiting a subdomain, for example, https://example.nasa.gov.
2. Add an Invalid Directory: Append an invalid directory to the URL, such as /demo. The full URL would be https://example.nasa.gov/demo.
3. Observe the Response: The URL will most likely redirect to a 404 error page. However, our targeted vulnerability might also appear.
4. Test with a .txt Extension: If the URL redirects to a 404 page, try adding .txt at the end of the URL, like this: https://example.nasa.gov/demo.txt.
5. Inject Content: At this point, you can inject any content into the page, which could easily be used to confuse a victim.
6. Examble : https://example.nasa.gov/-----------<your_content>------------.txt

Credited to Rajkumar Shanmugam

Source: https://medium.com/@rajkumarshanmugam/how-to-easily-get-the-hall-of-fame-on-nasas-vulnerability-disclosure-program-833b75ba72be
