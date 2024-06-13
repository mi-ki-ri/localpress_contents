import os
import re
import requests


def upload_post(filepath):
    API_URL = os.environ.get("API_URL")
    API_KEY = os.environ.get("API_KEY")

    # check
    if not API_URL or not API_KEY:
        print("API_URL or API_KEY is not set")
        return

    HEADER = {"Authorization": f"Bearer {API_KEY}"}
    file_body = open(filepath, "r", encoding="utf-8").read()
    BODY = {"data": {"content": file_body}}

    response = requests.post(API_URL, headers=HEADER, json=BODY)
    print(response.json())


def update_frontmatter(file_path, published):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r"^---\n(.*?\n)?published:\s*(true|false)\n(.*?\n)?---\n"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if match:
        # published フィールドが存在する場合、値を更新
        updated_content = re.sub(
            pattern,
            f"---\n\\1published: {str(published).lower()}\n\\3---\n",
            content,
            flags=re.MULTILINE | re.DOTALL,
        )
        if match.group(2) == "true":
            print(f"{file_path} は既にpublished: true に設定されています。")
        else:
            print(f"{file_path} はpublished: true に設定されていません。")
            upload_post(file_path)

    else:
        # published フィールドが存在しない場合、新しく追加
        updated_content = f"---\npublished: {str(published).lower()}\n---\n{content}"
        upload_post(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)


# 使用例
markdown_folder = "posts"


def main():
    for filename in os.listdir(markdown_folder):
        if filename.endswith(".md"):
            file_path = os.path.join(markdown_folder, filename)
            update_frontmatter(file_path, True)  # published: true に設定


if __name__ == "__main__":
    main()
