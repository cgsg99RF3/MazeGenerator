class Params:
    def __init__(self, glob_sz):
        self.glob_sz = glob_sz
        print("Save to file after generating? (Y/N)")
        ans = input()
        self.width = 0
        self.height = 0
        if ans == 'Y':
            print("File name:")
            self.file_to = input()
        else:
            self.file_to = ""

        print("Get maze from file? (Y/N)")
        ans = input()

        if ans == 'Y':
            self.type = 0
            print("File name:")
            self.file_from = input()
        else:
            print("Set width and height:")
            self.width, self.height = [int(x) for x in input().split()]

            print("Choose generator type(DFS/MST):")
            ans = input()
            if ans == "DFS":
                self.type = 1

            elif ans == "MST":
                self.type = 2
