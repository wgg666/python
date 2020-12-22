def xy_item(response):
    headers_list = {
        "内容类型": response.headers["Content-Type"],
        "编码": response.encoding,
        "响应时间": response.elapsed.total_seconds()
    }
    try:
        headers_list["状态码"] = response.status_code
    except:
        headers_list["状态码"] = response.status

    try:
        headers_list["服务器中间件"] = response.headers["Server"]
    except:
        headers_list["服务器中间件"] = None
    print('响应头：', headers_list)


if __name__ == '__main__':
    xy_item(response_get)
