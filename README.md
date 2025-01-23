# LSEG Interview

### Run app
```
python3 app/app.py
```

### Run test
```
python3 -m unittest discover -s tests
```

### Github action diagram
![diagram](./diagram.png)

### App
http://18.141.183.168:5000/

http://18.141.183.168:5005/

### Bonus Points
- **Secure way to use secrets**: Use GitHub Actions secrets that can be written to but cannot read back or modified
- **Quality gate to pass/fail build on scan results**: Added Trivy for security scanning. If the scan passes, the build will automatically proceed to deploy-dev; if not, the run will fail.
- **Standard branch environment deployment control**: The `main` branch is used for storing production-ready code, and our workflow is triggered every time there is a commit. We also use short-lived `feature/xxxyyy` branches for feature development. Additionally, we have workflows for shift-left unit tests and Trivy scans before merging into `main`.