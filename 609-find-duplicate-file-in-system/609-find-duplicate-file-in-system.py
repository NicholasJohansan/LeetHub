class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        for path in paths:
            split = path.split(" ")
            path = split[0]
            for i in range(1, len(split)):
                file = split[i]
                name, content = file.split("(")
                content = content.replace(")", "")
                curr_files = files.get(content, [])
                curr_files.append(f"{path}/{name}")
                files[content] = curr_files
        duplicates = []
        for values in files.values():
            if len(values) > 1:
                duplicates.append(values)
        return duplicates