**Researched by Suphawith Phusanbai**

<h1>Ghostfolio</h1>

<h2>About</h2>

Open Source Wealth Management Software. Angular + NestJS + Prisma + Nx + TypeScript

GitHub Repo: https://github.com/ghostfolio/ghostfolio

<h2>Tested on</h2>

-Ubuntu 22.04.5 LTS

-Ghostfolio 2.117.0

<h2>Findings</h2>

The web application is secured. Couldn't find any vulnerability


<h2>Details</h2>

**Security token(For testing): fbae5ab28f324f17ae690960176e0bad679667f9fcbb94b69d1e52e1916e167192228f4ffbe7fd7333531583557c71efbfde0aa4c95086b3914faca446300e32**

**API Endpoints**



```
POST /api/v1/user HTTP/1.1
```
**-Profile**

```
GET /api/v2/portfolio/performance?range=max HTTP/1.1
```

**-Login with Security Token**

```
POST /api/v1/auth/anonymous HTTP/1.1
```
**-Place orders**

```
POST /api/v1/order HTTP/1.1
```
**-Place orders queries**

```
GET /api/v1/order?sortColumn=date&sortDirection=desc&take=50 HTTP/1.1
```


```
GET /api/v2/portfolio/performance?range=max HTTP/1.1
```
**-Search**
```
GET /api/v1/portfolio/holdings?query=a&range=1d HTTP/1.1
```
When trying to insert XSS script in input

![image](https://github.com/user-attachments/assets/3f3b634f-c910-4e28-bafa-51b1c1b60371)


Results

![image](https://github.com/user-attachments/assets/aa9883c3-a631-4fcf-9267-2507860d8d34)

The input is sanitized. This is a great example.


<h1>Performance API Test</h1>

| Attack                     | Payload                 | Result | 
| ------------------------ | --------------------- | ------------- | 
| `SQL`      | `max;%20select%20pg_sleep(10);--%20-`              |      :x:         | 
| `XSS`      | `<script>alert('XSS')</script>`              |      :x:         | 
| `LFI`      | `%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd`              |      :x:         |



/api/v2/portfolio/performance?range=max;%20select%20pg_sleep(10);--%20-




-The systen uses JWT session which means XSS is worth checking.

<h1>XSS test(Invulnerable)</h1>

![image](https://github.com/user-attachments/assets/a5ec684c-7bc3-4099-9a15-02ad0da2ee45)

**Result**

![image](https://github.com/user-attachments/assets/79cab867-dbaf-4da8-9867-91bf3e3c787d)

The output indicates that the web app is not vulnerable as it removes and sanitizes special character such as a double quote.

