def opensrc(src: str) -> list[str|int]:
    file_exts: list[str] = ["mdpp", "mdd", "md++"]
    if (src.split(".")[-1] not in file_exts):
        print("Please use a file with a valid extension.")
        return [1]
    with open(src, "r") as s:
        sread: list[str] = s.readlines()
        s.close()
    return sread
