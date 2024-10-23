class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user

    def __str__(self):
        return f"{self.user}: {self.content}"

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = Post(content, self.username)
        self.posts.append(post)

class MiniFacebook:
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = User(username)
            print(f"User {username} registered successfully.")

    def create_post(self, username, content):
        if username in self.users:
            self.users[username].create_post(content)
            print("Post created successfully.")
        else:
            print("User not found.")

    def display_posts(self):
        print("\nAll Posts:")
        for user in self.users.values():
            for post in user.posts:
                print(post)

def main():
    facebook = MiniFacebook()

    while True:
        print("\nMini Facebook Menu:")
        print("1. Register User")
        print("2. Create Post")
        print("3. View Posts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            username = input("Enter username: ")
            facebook.register_user(username)
        elif choice == '2':
            username = input("Enter your username: ")
            content = input("Enter your post: ")
            facebook.create_post(username, content)
        elif choice == '3':
            facebook.display_posts()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
