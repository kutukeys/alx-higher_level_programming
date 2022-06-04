#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
<<<<<<< HEAD
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)
=======
    all_dir = dir(hidden_4)
    for i in range(0, len(all_dir)):
        if "__" != all_dir[i][:2]:
            print(all_dir[i])
>>>>>>> 16e9d86c3499321734fd426121a4e8f3bca23384
