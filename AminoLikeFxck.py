import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.CADET_BLUE_1 + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("Aminolikefxck", font="fourtops"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]

blogs_count = int(input("Blogs Count >> "))

while True:
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for i in range(0, 20000, 250):
                recent_blogs = client.get_recent_blogs(
                    ndc_Id=ndc_Id, start=i, size=blogs_count).blog_Id
                for blog_id in recent_blogs:
                    _ = [executor.submit(client.vote, ndc_Id, blog_id)]
                    print(f"Liked >> {blog_id}")
    except Exception as e:
        print(e)
