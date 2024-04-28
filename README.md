## Setup 

### Installazione di Terraform con Choco su Windows

1. Installa Choco and Terraform 

```console
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

```console
choco install terraform
```

### Installazione del Serverless Framework e del plugin serverless-python-requirements

```console
npm install -g serverless
```

```console
serverless plugin install --name serverless-python-requirements
```

### Lancio Terraform 

```console
terraform init --upgrade
terrafrom apply
```

### Aggiorna le funzioni lambda

Contenute nella cartella `serverless/functions`

### Update serverless.yml file

1. Aggiorna il file `serverless.yml` inserendo i riferimenti corretti per i parametri SSM e le funzioni lambda 

2. Deploy con Serverless

```console
serverless deploy 
```

## Postman collection

[Link](https://weaving360.postman.co/workspace/near~42e56a0b-ec05-411f-ab0d-10d1782c515b/collection/25830852-c6d2b7c3-30ca-4488-8639-c982c82d752b?action=share&creator=25830852)

## References 

* [Serverless and SQL with Python](https://medium.com/analytics-vidhya/serverless-and-sql-with-python-on-aws-9967554c1283)