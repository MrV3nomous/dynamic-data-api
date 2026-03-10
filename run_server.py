import os

print("Select API framework:")
print("1 FastAPI")
print("2 Flask")

choice = input("Choice: ")

if choice == "1":
    os.system("uvicorn fastapi_server.main:app --reload")

elif choice == "2":
    os.system("python flask_server/main.py")

else:
    print("Invalid choice")
