# SSH-Login-Brute-Forcing
## Brute Forcing an SSH connection credentials

**Requriements:**
- SSH Enabled on the SSH Server Virtual Machine
- Virtual Env if needed

# 
### To enable SSH:
- **`sudo systemctl enable ssh`** view status from **`sudo systemctl status ssh`**
- Enable PasswordAuthenticaton from **`/etc/ssh/sshd_config`**, uncomment this line in the text file **`PasswordAuthentication yes`**
  

### Launch Virtual Env from Python:
- Make sure to install it **`sudo apt install python3-venv`**
- Create the venv via **`python3 -m venv myenv`**
- Start the venv **`source myenv/bin/activate`**
#

### Problems related to the number of attepmts
This issue is related to the *`MaxAuthTries`* variable on the **`/etc/ssh/sshd_config`** text file, decreasing the number is just a security wise.


![image](https://github.com/AwsGhanem/SSH-Login-Brute-Forcing/assets/123994471/bf7ac522-b699-48f2-805a-7e796291b328)

# Real Experiment
![image](https://github.com/AwsGhanem/SSH-Login-Brute-Forcing/assets/123994471/02ce5632-83fc-4706-a3f7-d9ea5142ce31)

![image](https://github.com/AwsGhanem/SSH-Login-Brute-Forcing/assets/123994471/01d826e2-e787-4522-ad08-74228aa2ceb8)

## Connecting from a Remote Machine (Same Domain)

![image](https://github.com/AwsGhanem/SSH-Login-Brute-Forcing/assets/123994471/9cd358fd-ec2c-4c92-95fe-7d111919ba14)


## Security Concerns
Getting credentials for an authorized user in some organization or whatever, may lead to a problem with accessing confidential data, the main problem is `Whats the access rights for every user?`, when it comes to remote access there must be **Access Control**, or what we call **`Authorization`**.

##
As i provided the experiment, when i connected from a remote machine to the SSH Server, i could make anything withing the data contained on the server (read,write,execute,delete,etc...), and i could run any tool and view the machine information, or maybe i can access other users information.

## 
Specifing the access rights for every user (or groups) and making only the admins to be authorized to access the most important data and tools, will solve the majority of this problem. 

