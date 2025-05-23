**Github Dork**

If you know you know.

**Special thanks to dub-flow source: https://github.com/dub-flow/github-dorks/tree/main**
```
PHP XSS: /\becho\b.*\$_GET\b/ or /echo\s+\$_REQUEST/

PHP XSS: /^.*\becho\s+\$_GET\b.*$/

PHP XSS (most FP-prone): /^.*\becho\s+\$\b.*$/

PHP SQL Injection: /(SELECT|INSERT|UPDATE|DELETE)\s(.*\$_POST|.*\$_GET|.*\$_REQUEST)/

PHP OS Command Injection: /(exec\(|system\(|shell_exec\(|passthru\()(.*\$_POST|.*\$_GET|.*\$_REQUEST)/

Host Header Injection (Node.js & PHP): req.headers.host path:*pass* and /\$_SERVER\['host'\]|gethostname\(\).*(reset|forgot)/

.NET Host Header Injection: /(Request\.Headers\["Host"\]|Request\.Host\.Value|HttpContext\.Current\.Request\.Headers\["Host"\]|HttpContext\.Request\.Host\.Value)/ forgot

Host Header Injection generic: host path:**/*forgot*/**

Insecure Deserialization in PHP: /(unserialize\()(.*\$_POST|.*\$_GET|.*\$_REQUEST)/
```
**Useful Query**

```
"eval(" OR "exec(" OR "os.system(" OR "subprocess.call(" OR "subprocess.run(" OR "os.popen(" OR "pickle.load(" OR "os.remove(" OR "os.unlink(" OR "os.rmdir(" OR "shutil.rmtree(" OR "compile(" "open-source" "python"
```

**CVE Response time**

Fast = notionally 1-3 days

Normal = notionally 1-3 weeks

Slow = notionally, time permitting

(Sometimes MITRE can send several CVE IDs in one reply. that's why if you keep sending the CVE request and haven't received any of CVE ID. it is possible that you will get those altogether in one reply.)

Reference: https://cve.mitre.org/data/board/archives/2011-10/msg00003.html
