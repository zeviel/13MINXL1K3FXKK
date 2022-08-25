import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.CADET_BLUE_1 + style.BOLD}
Script by zeviel
Github : https://github.com/zeviel"""
)
print(figlet_format("13MINXL1K3FXKK", font="fourtops"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)

while True:
    try:
        with ThreadPoolExecutor(max_workers=20) as executor:
            for i in range(0, 2500, 15000):
                recent_blogs = sub_client.get_recent_blogs(
                    start=i, size=100).blogId
                for blog_id in recent_blogs:
                    executor.submit(sub_client.like_blog, blog_id)
                    print(f"-- Liked::: {blog_id}")
    except Exception as e:
        print(e)
