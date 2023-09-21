print("hi")
print("""
We are the lion king
""")
user_name =input("username:")
user_type =input("animaltype:")
print("wellcome","the",(user_type),(user_name), "to the junger")
print("wellcome"+"the"+(user_type)+(user_name)+" "+"to the junger")
print(f"wellcome {user_type} {user_name} to the junger")
print("wellcome the {} {} to the junger ".format(user_type,user_name))