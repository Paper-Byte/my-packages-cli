from models.package import Package
from models.language import Language
from rich import print


def list_packages():
    packages = Package.get_all()
    for package in packages:
        print(package)


def find_package_by_name():
    name = input("Enter the emloyee's name: ")
    package = Package.find_by_name(name)
    print(package) if package else print(f"Package {name} not found")


def find_package_by_id():
    id_ = input("Enter the package's ID: ")
    package = Package.find_by_id(id_)
    print(package) if package else print(f"Package {id_} not found")


def create_package():
    try:
        name = input("Enter new package's name: ")
        command = input("Enter new package's command: ")
        language_id = input("Enter new package's language ID: ")
        package = Package.create(name, command, language_id)
        print(f"Success: {package}")
    except Exception as exc:
        print(f"Failed to create package: ", exc)


def update_package():
    id_ = input("Enter package's ID: ")
    if package := Package.find_by_id(id_):
        try:
            name = input("Enter package's new name: ")
            package.name = name
            command = input("Enter package's new command: ")
            package.command = command
            language_id = input("Enter package's new language ID: ")
            package.language_id = language_id

            package.update()
            print(f"Success: {package}")

        except Exception as exc:
            print("Failed to update package: ", exc)
    else:
        print(f"Package {id_} not found")


def delete_package():
    id_ = input("Enter package ID: ")
    if package := Package.find_by_id(id_):
        package.delete()
        print(f"Package {id_} deleted")
    else:
        print(f"Package {id_} not found")


def list_language_packages():
    language_id = input("Enter language ID: ")
    if language := Language.find_by_id(language_id):
        packages = language.packages()
        for package in packages:
            print(package)
    else:
        print(f"Language {language_id} not found")
