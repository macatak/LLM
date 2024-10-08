Commands

```shell
sudo curl -L https://ollama.com/download/ollama-linux-amd64 -o /usr/bin/ollama
sudo chmod +x /usr/bin/ollama
sudo useradd -r -s /bin/false -m -d /usr/share/ollama ollama
``` 
Create a service file in /etc/systemd/system/ollama.service:   
```text
[Unit] 
Description=Ollama Service 
After=network-online.target 
 
[Service] 
ExecStart=/usr/bin/ollama serve 
User=ollama 
Group=ollama 
Restart=always 
RestartSec=3 
 
[Install] 
WantedBy=default.target 
```

```shell
sudo systemctl daemon-reload  
sudo systemctl start ollama  

ollama run llama2  
ollama run tinyllama  
ollama run codellama
```

Uninstall
```shell
Remove the ollama service: 
sudo systemctl stop ollama 
sudo systemctl disable ollama 
sudo rm /etc/systemd/system/ollama.service
```

Remove the ollama binary from your bin directory (either /usr/local/bin, /usr/bin, or /bin):
```shell
sudo rm $(which ollama)
```

Remove the downloaded models and Ollama service user and group:
```shell
sudo rm -r /usr/share/ollama
sudo userdel ollama
sudo groupdel ollama
```
