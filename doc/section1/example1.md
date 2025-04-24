# 在 Linux 上搭建 GitLab 并集成 GitBook 实现自动化 Wiki 系统

本文将指导您在 Linux 服务器上搭建 GitLab，集成 GitBook 并通过 GitLab CI 实现一个企业级或个人 Wiki 系统，实现提交代码时自动刷新部署 GitBook 内容。

## 环境准备

1. 一台 Linux 服务器（推荐 Ubuntu Jammy）
2. 安装 Node.js 及 npm 环境（推荐 v12.16.3，版本过高可能导致 GitBook 安装报错）

## 安装 Node.js 环境

### 方法一：使用 NVM（推荐）

NVM（Node Version Manager）可以方便地管理多个 Node.js 版本：

```shell
# 下载并安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash

# 立即加载 nvm
\. "$HOME/.nvm/nvm.sh"

# 下载并安装指定版本的 Node.js
nvm install 12.16.3

# 验证安装
node -v
npm -v
```

### 方法二：手动安装

1. 创建并进入 node 目录：
   ```shell
   mkdir node
   cd node
   ```

2. 下载并解压 Node.js：
   ```shell
   wget https://nodejs.org/dist/v12.16.3/node-v12.16.3-linux-x64.tar.xz
   tar xf node-v12.16.3-linux-x64.tar.xz
   ```

3. 移动并重命名目录：
   ```shell
   mkdir /usr/local/lib/node
   mv node-v12.16.3-linux-x64 /usr/local/lib/node/nodejs
   ```

4. 设置环境变量：
   ```shell
   sudo vim /etc/profile
   ```
   在文件底部添加：
   ```shell
   export NODEJS_HOME=/usr/local/lib/node/nodejs
   export PATH=$NODEJS_HOME/bin:$PATH
   ```
   保存后刷新配置：
   ```shell
   source /etc/profile
   ```

## 安装 Git

```shell
sudo apt install git
git --version
```

## 安装 GitLab

1. 添加 GitLab 仓库密钥：
   ```shell
   curl -fsSL https://packages.gitlab.com/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/gitlab_gitlab-ce-archive-keyring.gpg
   ```

2. 添加清华镜像源：
   ```shell
   echo 'deb [signed-by=/usr/share/keyrings/gitlab_gitlab-ce-archive-keyring.gpg] https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu jammy main' | sudo tee /etc/apt/sources.list.d/gitlab-ce.list
   ```

3. 安装 GitLab：
   ```shell
   sudo apt-get update
   sudo apt-get install gitlab-ce
   ```

4. 配置 GitLab：
   ```shell
   sudo vim /etc/gitlab/gitlab.rb
   ```
   修改 `external_url` 为您的服务器地址，例如：
   ```shell
   external_url "http://192.168.0.1:20001"
   ```

5. 重新配置并重启 GitLab：
   ```shell
   sudo gitlab-ctl reconfigure
   sudo gitlab-ctl restart
   ```

6. 获取初始密码：
   ```shell
   sudo cat /etc/gitlab/initial_root_password
   ```

## 安装 GitBook

1. 设置 npm 镜像源：
   ```shell
   npm config set registry https://registry.npmmirror.com
   ```

2. 安装 GitBook CLI：
   ```shell
   npm install gitbook-cli -g
   ```

## 安装 GitLab Runner

1. 添加 GitLab Runner 仓库密钥：
   ```shell
   curl -L https://packages.gitlab.com/runner/gitlab-runner/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/gitlab-runner.gpg
   ```

2. 添加清华镜像源：
   ```shell
   echo 'deb [signed-by=/usr/share/keyrings/gitlab-runner.gpg] https://mirrors.tuna.tsinghua.edu.cn/gitlab-runner/ubuntu jammy main' | sudo tee /etc/apt/sources.list.d/gitlab-runner.list
   ```

3. 安装 GitLab Runner：
   ```shell
   sudo apt-get update
   sudo apt-get install gitlab-runner
   sudo chmod +x /usr/local/bin/gitlab-runner
   ```

4. 安装并启动 Runner：
   ```shell
   sudo gitlab-runner install --user=root
   sudo gitlab-runner start
   ```

## 配置 GitLab Runner

1. 注册 Runner：
   ```shell
   sudo gitlab-runner register
   ```
   按照提示输入：
   - GitLab 实例 URL
   - 注册令牌（从 GitLab 项目的 Settings > CI/CD > Runners 获取）
   - 描述（如 "my-runner"）
   - 标签（如 "gitbook"）
   - 执行器（选择 "shell"）

2. 验证 Runner 是否注册成功：
   在 GitLab 项目的 Settings > CI/CD > Runners 中查看 Runner 状态。

## 配置 GitBook 自动化部署

1. 在 GitBook 项目根目录创建 `.gitlab-ci.yml` 文件：
   ```yaml
   stages:
     - build
   wiki-deploy:
     tags:
       - gitbook  # 与注册 Runner 时设置的标签一致
     stage: build
     script:
       - pwd
       - gitbook install
       - gitbook build
       - setsid nohup sh startup.sh > nohup.out 2>&1 &
   ```

2. 创建 `startup.sh` 脚本：
   ```shell
   #!/bin/bash
   for i in `ps -ef | grep gitbook | grep serve`; do kill -9 $i ; done;
   gitbook serve
   ```
   并赋予执行权限：
   ```shell
   chmod +x startup.sh
   ```

## 验证部署

1. 将项目推送到 GitLab 仓库
2. 在 GitLab 的 CI/CD > Pipelines 中查看构建状态
3. 访问 `http://服务器IP:4000` 查看实时更新的 Wiki 内容

至此，您已成功搭建了一个自动化的 Wiki 系统，每次推送代码到 GitLab 都会自动构建并更新 GitBook 内容。