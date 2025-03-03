Find Sourcemap 
---

1. Git dorking

```
ext:map intext:webpack intext:react -site:github.com -intitle:GitLab -inurl:(git|blob|repo|browse)
```

2. Install Sourcemapper

```
go install github.com/denandz/sourcemapper@latest
```

3. Extract content

```
sourcemapper -url https://example/minified.js.map -output srcmapper_output
```

4. Open the folder in VSCode and look for apikeys, creds, secrets and internal API endpoints. 
