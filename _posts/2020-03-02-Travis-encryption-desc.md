---
layout: post
current: post
cover:  assets/images/travis.png
navigation: True
title: Travis 中的几类数据加密
date: 2020-03-01 20:01:01
tags: [dev git]
class: post-template
subclass: 'post dev git'
author: dexfire
---

# travis-ci 中的几类数据加密

travis-ci 是一个托管构建平台，可以检测 Github 项目的 Commit 并随时构建，推送编译测试结果。

Travis-ci 使用类似 Docker 的组织方式，使用时仅仅需要在项目目录下包含一个 `.travis.yml` 写入编译环境配置，平台支持众多编译环境的编译。

一个仓库中的 `.travis.yml` 文件可以包含加密变量，通常为环境变量，敏感设置值，apikeys等，这些加密值可以由任意用户加密上传，但仅仅可以由Travis CI读取，且加密时用户不需要保留任何私钥。

值得注意的是，加密环境变量不适用于forks项目下的pull request。

## 加密协议

Travis CI 使用非对称式加密，对于每一个注册的仓库，Travis CI生成一个RSA密钥对。Travis CI保留私钥，但对访问仓库用户开放公钥。

开放的公钥可以为任何人所用，用于加密对应于该密钥对的数据，但这些数据只有Travis CI可以访问。

### 获取公钥

获取公钥的方式因项目位置，以及仓库使用的API版本而异。

此外，获取公钥的请求可能需要通过“用户：口令”方式进行认证，这同样取决于仓库的位置、可见性以及采用的API版本。

<table>
  <caption><tt>Authorization</tt> header requirement</caption>
  <tr>
    <th rowspan="2">Repository visibility and location</th>
    <th rowspan="2">API server</th>
    <th>API v1</th>
    <th>API v3</th>
  </tr>
  <tr>
    <td><tt>/repos/OWNER/REPO/key</tt></td>
    <td><tt>/v3/repo/OWNER%2fREPO/key_pair/generated</tt></td>
  </tr>
  <tr>
    <td>.org</td>
    <td><a href="https://api.travis-ci.org">https://api.travis-ci.org</a></td>
    <td>no</td>
    <td>yes</td>
  </tr>
  <tr>
    <td>public on .com</td>
    <td><a href="https://api.travis-ci.com">https://api.travis-ci.com</a></td>
    <td>yes<br></td>
    <td>yes<br></td>
  </tr>
  <tr>
    <td>private on .com</td>
    <td><a href="https://api.travis-ci.com">https://api.travis-ci.com</a></td>
    <td>yes<br></td>
    <td>yes</td>
  </tr>
</table>

> 注意：第三版的仓库位置会显示为 `%2f` 字符。

如果您需要 `Authorization: token` 请求头， 您可以通过一以下账户页面获取：
- [travis-ci.org](https://travis-ci.org/account/preferences)
- [travis-ci.com](https://travis-ci.com/account/preferences)

### 加密实例

以下是采用 `curl` 命令获取公钥的例子：

1. A public repository on travis-ci.org using API v1

       curl https://api.travis-ci.org/repos/travis-ci/travis-build/key

1. A public repository on travis-ci.org using API v3

       curl -H "Authorization: token **TOKEN**" https://api.travis-ci.org/v3/repo/travis-ci%2ftravis-build/key_pair/generated

1. A private repository on travis-ci.com using API v3

       curl -H "Authorization: token **TOKEN**" https://api.travis-ci.com/v3/repo/OWNER%2fREPO/key_pair/generated

## 使用方式

最简单的用公钥加密的方式是采用Travis CLI工具，采用Ruby编写且已发布为gem项目，您需要首先安装这一工具：

```bash
gem install travis
```

如果您使用的是 [travis-ci.com](https://travis-ci.com) 而非 [travis-ci.org](https://travis-ci.org), 你需要使用如下方式登录:

```bash
travis login --pro
```

此后，你可以使用 `encrypt` 命令来加密数据 (假设你在项目目录下运行，否则情添加参数 `-r owner/project`指明仓库路径):

```bash
travis encrypt SOMEVAR="secretvalue"
```

如果使用[travis-ci.com](https://travis-ci.com), 请添加 `--pro` 参数:

```bash
travis encrypt --pro SOMEVAR="secretvalue"
```

通常输出如下:

```yaml
secure: ".... encrypted data ...."
```
{: data-file=".travis.yml"}

现在你可以将其添加到 `.travis.yml` 文件中.

你也可以使用参数 `--add` 自动完成上一步.
```bash
travis encrypt SOMEVAR="secretvalue" --add
```

Please note that the name of the environment variable and its value are both encoded in the string produced by "travis encrypt." You must add the entry to your .travis.yml with key "secure" (underneath the "env" key). This makes the environment variable SOMEVAR with value "secretvalue" available to your program.

You may add multiple entries to your .travis.yml with key "secure." They will all be available to your program.

Encrypted values can be used in
[secure environment variables in the build matrix](/user/environment-variables#defining-encrypted-variables-in-travisyml)
and [notifications](/user/notifications).


### Detailed Discussion

The secure var system takes values of the form `{ 'secure' => 'encrypted string' }` in the (parsed YAML) configuration and replaces it with the decrypted string.

So

```yaml
notifications:
  campfire:
    rooms:
      secure: "encrypted string"
```
{: data-file=".travis.yml"}

becomes

```yaml
notifications:
  campfire:
    rooms: "decrypted string"
```
{: data-file=".travis.yml"}

while

```yaml
notifications:
  campfire:
    rooms:
      - secure: "encrypted string"
```
{: data-file=".travis.yml"}

becomes

```yaml
notifications:
  campfire:
    rooms:
      - "decrypted string"
```
{: data-file=".travis.yml"}

In the case of secure env vars

```yaml
env:
  - secure: "encrypted string"
```
{: data-file=".travis.yml"}

becomes

```yaml
env:
  - "decrypted string"
```
{: data-file=".travis.yml"}

## Fetching the public key for your repository

You can fetch the public key with Travis API, using `/repos/:owner/:name/key` or
`/repos/:id/key` endpoints, for example:

```
https://api.travis-ci.org/repos/travis-ci/travis-ci/key
```

You can also use the `travis` tool for retrieving said key:

```bash
travis pubkey
```

Or, if you're not in your project directory:

```bash
travis pubkey -r owner/project
```

Note, travis uses `travis.slug` in your project to determine the endpoints if it exists (check by using `git config --local travis.slug`), if you rename your repo or move your repo to another user/organization, you might need to change it.