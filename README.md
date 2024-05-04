# Setup 

1. Installa Choco and Terraform 

```console
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

```console
choco install terraform
```

2. Installazione del Serverless Framework e del plugin serverless-python-requirements

```console
npm install -g serverless
```

```console
serverless plugin install --name serverless-python-requirements
```

3. Deploy con Serverless

```console
serverless deploy 
```

4. Su Wix sotto *Automazioni* creare un'automazione che ha come target l'url degli API gateway generati.