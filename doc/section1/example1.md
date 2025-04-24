

```shell
curl -fsSL https://packages.gitlab.com/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/gitlab_gitlab-ce-archive-keyring.gpg
```

```shell
echo 'deb [signed-by=/usr/share/keyrings/gitlab_gitlab-ce-archive-keyring.gpg] https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu jammy main
' | sudo tee /etc/apt/sources.list.d/gitlab-ce.lis
```



```shell
sudo apt-get update
sudo apt-get install gitlab-ce
```

```shell
vim /etc/gitlab/gitlab.rb
## 修改以下内容并保存
external_url "http://192.168.0.1:20001"




## 依次执行下面命令 
gitlab-ctl reconfigure
gitlab-ctl restart

```

初始密码位置

```shell
/etc/gitlab/initial_root_password

```









```shell
export NVM_NODEJS_ORG_MIRROR=https://mirrors.tuna.tsinghua.edu.cn/nodejs-release/



 sudo vim /etc/profile


  source  /etc/profile
```

```shell
.bash_profile



export NVM_DIR="/root/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
 
```

```shell
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 12.16.3

# Verify the Node.js version:
node -v
nvm current 

# Verify npm version:
npm -v # Should print "10.9.2".

```

```shell
sudo apt install git
```

```shell
npm config set registry https://registry.npmmirror.com

npm install gitbook-cli -g
```

<h4 id="kEsaH"><font style="color:rgb(79, 79, 79);">GitLab Runner</font></h4>
```shell
curl -L https://packages.gitlab.com/runner/gitlab-runner/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/gitlab-runner.gpg



echo 'deb [signed-by=/usr/share/keyrings/gitlab-runner.gpg] https://mirrors.tuna.tsinghua.edu.cn/gitlab-runner/ubuntu jammy main
' | sudo tee /etc/apt/sources.list.d/gitlab-runner.list



sudo apt-get update
sudo apt-get install gitlab-runner

 sudo chmod +x /usr/local/bin/gitlab-runner


## 安装
gitlab-runner install --user=root 
## 启动
gitlab-runner start

```







<h2 id="BQeAI">开发</h2>
<h4 id="xEUIk">创建虚拟环境</h4>
```shell
python -m venv .venv

# 激活环境
.\.venv\Scripts\activate

```

<h4 id="UscKl">安装依赖</h4>
```shell
pip install -r requirements.txt


# 数据库=
# python manage.py makemigrations
# python manage.py migrate


```

<h4 id="vd3pN">导出所有依赖</h4>
```shell
pip freeze >requirements.txt

```

```shell
# 启动
python manage.py runserver      
```

