import read

class MDPP:
    def __init__(self, file: str) -> None:
        if read.opensrc(file) == [1]:
            return
        self.file = file
        self.code = read.opensrc(file)
        self.out = ""

    def outi(self, string: str) -> None:
        self.out += f"{string}\n"

    def astr(self, obj: list[str]) -> str:
        return " ".join(obj)

    def evalexpr(self) -> None:
        for line in self.code:
            loc = line.split(" ")
            match loc[0]:
                case "t"|"title":
                    self.outi(f"# {self.astr(loc[1:])}")
                case "l"|"link":
                    self.outi(f"[{loc[1]}]({loc[2].strip("\n")})")
                case "h"|"header":
                    for i in range(int(loc[1])):
                        self.out += "#"
                    self.outi(f" {self.astr(loc[2:])}")
                case _:
                    self.outi(self.astr(loc[0:]))
