import base64
import requests


def fetch_and_decode():
    url = "https://316.sub987.top/weibo/ipx/client/dy?token=230ed32d8d0bf90cbebfae979dc8db4e"

    try:
        # 1. 发送网络请求获取内容
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 如果状态码不是 200，会抛出异常
        raw_content = response.text.strip()

        print("成功获取密文，正在解码...")

        # 2. Base64 解码
        # 注意：有时候 Base64 字符串末尾可能会少 '='，这里做个简单的补全防御
        missing_padding = len(raw_content) % 4
        if missing_padding:
            raw_content += "=" * (4 - missing_padding)

        decoded_bytes = base64.b64decode(raw_content)
        # 尝试用 utf-8 解码成字符串，如果包含非文本数据则直接输出 bytes
        try:
            decoded_text = decoded_bytes.decode("utf-8")
            print("\n--- 解码后的内容 ---")
            print(decoded_text)
            return decoded_text
        except UnicodeDecodeError:
            print("\n--- 解码后的内容 (二进制数据) ---")
            print(decoded_bytes)
            return decoded_bytes

    except requests.exceptions.RequestException as e:
        print(
            f"网络请求失败，请检查 URL 或网络连接。错误信息: {e}"
        )
    except Exception as e:
        print(f"解码失败，可能返回的内容不是合法的 Base64 编码。错误信息: {e}")


if __name__ == "__main__":
    fetch_and_decode()