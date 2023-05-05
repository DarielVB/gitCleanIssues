def repository_to_check(repository_name):
    name = repository_name.lower()
    return "-mngr" in name or "-function" in name or "-adapter" in name