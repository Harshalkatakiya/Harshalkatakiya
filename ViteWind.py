import os

app_name = "my-app"

while True:
    app_name = input("\n? Project/App name : ")
    if not input("Do you want to Edit?(y = Yes, Enter = No):").lower() == "y":
        break

os.system(f"npm create vite@latest {app_name}")
os.system(f"cd {app_name} && npm install -D tailwindcss@latest postcss@latest autoprefixer@latest")
os.system(f"cd {app_name} && npx tailwindcss init -p")

try:
    file_name = f"./{app_name}/tailwind.config.js"
    file_contents = None
    with open(file_name, 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace(r"content: []", r'content: [ "./index.html", "./src/**/*.{js,ts,jsx,tsx}", ]')
    try:
        with open(file_name, 'w') as file:
            file.write(file_contents)
    except Exception as e:
        exit("Error:", str(e))
except:
    exit("Somthing went wrong!")

try:
    with open(f"./{app_name}/src/index.css", 'w') as file:
        file.write("\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")
except Exception as e:
    exit("Error:", str(e))

try:
    file_name = f"./{app_name}/vite.config.js"
    file_contents = None
    with open(file_name, 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace(
        r"})",
        r'''
  base: './',
  build: {
    outDir: "./dist"
  },
  // server: {
  //   host: ["localhost", "192.168.1.244", "192.168.1.243"],
  //   port: 80,
  // },
})''')
    try:
        with open(file_name, 'w') as file:
            file.write(file_contents)
    except Exception as e:
        exit("Error:", str(e))
except:
    exit("Somthing went wrong!")

os.system(f"cd {app_name} && npm run dev")
