# Description

This project is a serverless application built using the Serverless Framework and Infrastructure as Code (IaC) principles. It facilitates the seamless integration of new users from Wix into AWS services, such as DynamoDB or Cognito. By automating this process, it streamlines user management tasks and ensures efficient data synchronization between Wix and AWS.

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

# License

This project is licensed under the MIT License, allowing for unrestricted use, modification, and distribution.

# Disclaimer

This project is provided as-is without any warranties. Users are responsible for understanding and complying with the terms and conditions of the services utilized, such as AWS and Wix.