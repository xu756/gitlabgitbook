### 第一节

REST API 所有级别
使用 GitLab 的 REST API，通过任何兼容的 REST API 客户端来获取数据。

构造 REST API 请求
要构造 REST API 请求：

通过使用 REST API 客户端向 API 端点提交请求。
极狐GitLab 实例响应请求。它返回一个状态码，如果适用，则返回请求的数据。状态码表示请求的结果，在故障排除时很有用。
一个 REST APi 请求必需以根端点（root endpoint）和路径（path）开始。

根端点是极狐GitLab 主机名。
路径必须以 /api/v4 开始（v4 代表 API 版本）。
在以下示例中，API 请求从极狐GitLab 主机 jihulab.com 获取所有项目列表：

curl "https://jihulab.com/api/v4/projects"

访问某些端点需要认证。有关详细信息，请参阅认证。

速率限制
REST API 请求受速率限制的约束。这些设置降低了极狐GitLab 实例过载的风险。

更多详情，可以参阅速率限制。
有关 JihuLab.com 的速率限制设置，请参阅JihuLab.com 特定的速率限制。
响应格式
REST API 响应以 JSON 格式返回。某些 API 端点还支持纯文本格式。要确认某个端点支持哪种内容类型，请参阅REST API 资源。 ## 请求要求

有些 REST API 请求有特定需求，包括数据格式和使用的编码方式等。

请求负载
API 请求可以使用以查询字符或负载体发送的参数。GET 请求通常使用查询字符，而 PUT 和 POST 请求则通常使用负载体：

查询字符：

curl --request POST "https://gitlab/api/v4/projects?name=<example-name>&description=<example-description>"

请求负载 (JSON)：

curl --request POST --header "Content-Type: application/json" \
     --data '{"name":"<example-name>", "description":"<example-description>"}' "https://gitlab/api/v4/projects"

URL 编码的请求字符有长度限制。请求过长的结果会收到 414 Request-URI Too Large 错误消息。这可以通过使用请求负载来解决这个问题。

路径参数
如果端点有路径参数，文档会在它们前面加上冒号。

例如：

DELETE /projects/:id/share/:group_id

:id 路径参数需要替换为项目 ID，并且 :group_id 需要替换为群组的 ID。冒号 : 不应该包括在内。

对于 ID 为 5 且群组 ID 为 17 的项目，生成的 cURL 请求如下：

curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/share/17"

必须遵循要求进行 URL 编码的路径参数。如果不遵循，则它不匹配 API 端点并以 404 响应。如果 API 前面有东西（例如 Apache），请确保它不会解码 URL 编码的路径参数。

id vs iid
某些资源有两个名称相似的字段。例如，议题、合并请求和项目里程碑。 这些字段是：

id：所有项目中唯一的 ID。
iid：附加的内部 ID（显示在 Web UI 中），在单个项目中唯一。
如果资源同时具有 iid 字段和 id 字段，则 iid 字段通常用来代替 id 来获取资源。

例如，假设 id: 42 的项目有 id: 46 和 iid：5 的议题，在这种情况下：

检索议题的有效 API 请求是 GET /projects/42/issues/5。
检索议题的无效 API 请求是 GET /projects/42/issues/46。
并非所有带有 iid 字段的资源都由 iid 获取。 有关使用哪个字段的更多内容，请参阅特定资源的文档。

编码
当构建 REST API 请求时，某些内容必须进行编码以考虑特殊字符和数据结构。

命名空间路径
如果使用命名空间 API 端点，请确保 NAMESPACE/PROJECT_PATH 是 URL 编码的。

比如，/ 由 %2F 表示：

GET /api/v4/projects/diaspora%2Fdiaspora

项目的 路径 不一定是它的 名称。项目的路径可以在项目的 URL 或项目的设置中找到，在 通用 > 高级 > 修改路径 下。

文件路径、分支和标签名称
如果文件路径、分支或标签名称包含 /，请确保对其进行 URL 编码。

比如，/ 由 %2F 表示：

GET /api/v4/projects/1/repository/files/src%2FREADME.md?ref=master
GET /api/v4/projects/1/branches/my%2Fbranch/commits
GET /api/v4/projects/1/repository/tags/my%2Ftag

数组或哈希类型
您可以使用 array 和 hash 参数类型来发送 API 请求：

array
import_sources 是一个 array 类型的参数：

curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
-d "import_sources[]=github" \
-d "import_sources[]=bitbucket" \
"https://gitlab.example.com/api/v4/some_endpoint"

hash
override_params 是一个 hash 类型测参数：

curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
--form "namespace=email" \
--form "path=impapi" \
--form "file=@/path/to/somefile.txt" \
--form "override_params[visibility]=private" \
--form "override_params[some_other_param]=some_value" \
"https://gitlab.example.com/api/v4/projects/import"

哈希数组
variables 是一个 array 类型的参数，包含键/值对的哈希 [{ 'key': 'UPLOAD_TO_S3', 'value': 'true' }]：

curl --globoff --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
"https://gitlab.example.com/api/v4/projects/169/pipeline?ref=master&variables[0][key]=VAR1&variables[0][value]=hello&variables[1][key]=VAR2&variables[1][value]=world"

curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
--header "Content-Type: application/json" \
--data '{ "ref": "master", "variables": [ {"key": "VAR1", "value": "hello"}, {"key": "VAR2", "value": "world"} ] }' \
"https://gitlab.example.com/api/v4/projects/169/pipeline"

在 ISO 8601 格式中编码 +
如果您需要在查询参数中包含 +，您可能需要使用 %2B，因为 W3 推荐使用 + 被解释为空格。例如，在 ISO 8601 日期中，您可能希望包含特定的时间，例如：

2017-10-17T23:11:13.000+05:30

查询参数的正确编码将是：

2017-10-17T23:11:13.000%2B05:30

评估响应
在某些场景下，API 响应可能和期望的不同。问题可能包括 null 值和重定向。如果您在响应中收到一个数字状态码，请参阅 状态码。

null vs false
在 API 请求中，有些布尔字段可能是 null。null 布尔值没有默认值，既不是 true 也不是 false。极狐GitLab 将 null 布尔值视为 false。

在布尔字段中，您应该只设置 true 或 false 值（而不是 null）。

重定向
引入于极狐GitLab 16.4，并使用名为 api_redirect_moved_projects 的功能标志。默认禁用。
在极狐GitLab 16.7 中 GA。功能标志 api_redirect_moved_projects 被移除。
在路径变更后，REST API 可能会响应一个消息，指出端点已移动。当这种情况发生时，使用 Location 头中指定的端点。

项目路径变更的示例：

curl --verbose "https://gitlab.example.com/api/v4/projects/gitlab-org%2Fold-path-project"

响应为：

...
< Location: http://gitlab.example.com/api/v4/projects/81
...
This resource has been moved permanently to https://gitlab.example.com/api/v4/projects/81


分页
极狐GitLab 支持以下分页方式：

基于偏移量的分页。这是默认方法，可用于所有端点。
基于键集的分页。添加到选定的端点。
对于大型集合，出于性能原因，您应该使用键集分页（可用时）而不是偏移分页。

基于偏移量的分页
有时，返回的结果会跨越很多页。列出资源时，您可以传递以下参数：

参数	描述
page	页码（默认：1）
per_page	每页列出的项目数（默认：20；最大：100）
在以下示例中，我们每页列出 50 个命名空间：

curl --request GET --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/namespaces?per_page=50"

偏移分页有一个允许的最大偏移量限制。您可以更改私有化部署实例中的限制。
分页 Link 标头
Link 标头随每个响应一起返回。它们将 rel 设置为 prev、next、first 或 last，并包含相关的 URL。请务必使用这些链接，而不是生成您自己的 URL。

对于 JihuLab.com 用户，某些分页标题可能不会返回。

在下面的 cURL 示例中，我们将输出限制为每页三个项目 (per_page=3) 并且我们请求 ID 为 8 的议题评论的第二页（page=2），它属于 ID 为 9 的项目：

curl --head --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/9/issues/8/notes?per_page=3&page=2"

响应为：

HTTP/2 200 OK
cache-control: no-cache
content-length: 1103
content-type: application/json
date: Mon, 18 Jan 2016 09:43:18 GMT
link: <https://gitlab.example.com/api/v4/projects/8/issues/8/notes?page=1&per_page=3>; rel="prev", <https://gitlab.example.com/api/v4/projects/8/issues/8/notes?page=3&per_page=3>; rel="next", <https://gitlab.example.com/api/v4/projects/8/issues/8/notes?page=1&per_page=3>; rel="first", <https://gitlab.example.com/api/v4/projects/8/issues/8/notes?page=3&per_page=3>; rel="last"
status: 200 OK
vary: Origin
x-next-page: 3
x-page: 2
x-per-page: 3
x-prev-page: 1
x-request-id: 732ad4ee-9870-4866-a199-a9db0cde3c86
x-runtime: 0.108688
x-total: 8
x-total-pages: 3

其他分页标题
极狐GitLab 还返回以下额外的分页标头：

标头	描述
x-next-page	下一页的索引
x-page	当前页的索引（从 1 开始）
x-per-page	每页的项目数
x-prev-page	上一页的索引
x-total	项目总数
x-total-pages	页码总数
对于 JihuLab.com 用户，某些分页标头可能不会返回。


基于键集的分页
基于键集的分页允许更有效地检索页面，并且与基于偏移量的分页相比，运行时独立于集合的大小。

此方法由以下参数控制。 order_by 和 sort 都是强制性的。

参数	是否必需	描述
pagination	yes	keyset（启用键集分页）
per_page	no	每页列出的项目数（默认：20；最大：100）
order_by	yes	排序依据的列
sort	yes	排序顺序（asc 或 desc）
在下面的示例中，我们每页列出 50 个项目，按 id 升序排列。

curl --request GET --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects?pagination=keyset&per_page=50&order_by=id&sort=asc"

响应标头包含指向下一页的链接。例如：

HTTP/1.1 200 OK
...
Link: <https://gitlab.example.com/api/v4/projects?pagination=keyset&per_page=50&order_by=id&sort=asc&id_after=42>; rel="next"
Status: 200 OK
...

下一页的链接包含一个额外的过滤器 id_after=42，排除已检索的记录。

作为另一个示例，以下请求使用键集分页按 name 升序列出每页 50 个群组：

curl --request GET --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups?pagination=keyset&per_page=50&order_by=name&sort=asc"

响应标头包含指向下一页的链接：

HTTP/1.1 200 OK
...
Link: <https://gitlab.example.com/api/v4/groups?pagination=keyset&per_page=50&order_by=name&sort=asc&cursor=eyJuYW1lIjoiRmxpZ2h0anMiLCJpZCI6IjI2IiwiX2tkIjoibiJ9>; rel="next"
Status: 200 OK
...

下一页的链接包含一个额外的过滤器 cursor=eyJuYW1lIjoiRmxpZ2h0anMiLCJpZCI6IjI2IiwiX2tkIjoibiJ9，排除已检索的记录。

过滤器的类型取决于使用的 order_by 选项，我们可以有多个额外的过滤器。

极狐GitLab 14.0 中删除了 Links 标头，以便与 W3C Link 规范保持一致。 Link 标头已在极狐GitLab 13.1 中添加，用户可以使用。
当到达集合末尾并且没有其他记录要检索时，Link 标头不存在并且结果数组为空。

您应该仅使用给定的链接来检索下一页，而不是构建您自己的 URL。除了显示的标头外，我们不会公开其他分页标头。

支持的资源
基于键集的分页仅支持以下资源：

资源	选项	可用性
群组审计事件	order_by=id, sort=desc only	仅限认证用户。
群组	order_by=name, sort=asc only	仅限认证用户。
实例审计事件	order_by=id, sort=desc only	仅限认证用户。
软件包流水线	order_by=id, sort=desc only	仅限认证用户。
项目作业	order_by=id, sort=desc only	仅限认证用户。
项目审计事件	order_by=id, sort=desc only	仅限认证用户。
项目	order_by=id only	认证和非认证用户。
用户	order_by=id, order_by=name, order_by=username	认证和非认证用户。引入于极狐GitLab 16.5。
镜像仓库标签	order_by=name, sort=asc, or sort=desc only.	仅限认证用户。
获取仓库树	N/A	认证和非认证用户。引入于极狐GitLab 17.1。

分页响应标头
出于性能原因，如果查询返回超过 10,000 条记录，极狐GitLab 不返回以下标头：

x-total.
x-total-pages.
rel="last" link
版本和弃用
REST API 版本遵循语义版本控制规范。主版本号是 4。向后不兼容的更改需要更改此版本号。

次版本号不是显式的，这允许稳定的 API 端点。
新功能添加到同一版本号的 API 中。
主要 API 版本更改和删除整个 API 版本与主要 GitLab 版本同时进行。
版本之间的弃用和更改在文档中记录。
以下内容在弃用过程中被排除，可以在任何时候删除而不通知：

在 REST API 资源中标记为 实验性或 Beta 的元素。
背后有一个功能标志并且默认禁用的字段。