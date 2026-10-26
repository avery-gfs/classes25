# READ THIS FIRST!!!!!!

# this problem concerns a fake social media site in the terminal, named EVILMEDIA
# you post on EVILMEDIA by printing to the terminal

# users on EVILMEDIA have a username, and a list of posts
# they can make posts and can get the number of posts they've made
# when posts are made, usernames are added to the front of the post (see the reference at the bottom)
# when posts are made, posts are also saved in the posts lists, which should be an attribute of User
# when posts are saved, usernames should NOT be saved in the post string

# admins on EVILMEDIA have a username, a list of posts, and an admin number
# admins can do everything that users can
# when admins post, their admin number, with their username is added to the front of their post
# when posts are saved, usernames and admin numbers should NOT be saved in the post string
# admins can delete another user's post

# now look at the bottom of the file

class User:
    def __init__(self, username, posts):
        # the user should take in a username, and a list of posts, and store it
        # you should be able to access a user's posts with an attribute named "posts"
        # this __init__ function should look simmilar to the ones you've seen already
        pass 

    def make_post(self, post):
        # given a string, "post" (print) the string
        pass

    def get_number_of_posts(self):
        # get the number of posts a user has made; use their list of posts as reference
        pass


class Admin(User):
    def __init__(self, username, posts, admin_number):
        pass

    # SOME OF THE BELOW FUNCTIONS MIGHT NOT BE NEEDED
    # SOME OF THEM MIGHT NEED TO BE OVERRIDED
    # figure out which ones... 
    
    def make_post(self, post):
        # given a string, post (print) the string, along with the username
        # admin posts should be formatted as such
        # admin_number - admin_username: admin_post
        pass

    def get_number_of_posts(self):
        # get the number of posts a user has made; use their list of posts as reference
        pass

    def delete_user_post(self, user, post):
        # given a user, remove a post from their list of posts
        pass


user1 = User("joe27", ["i HATE social media", "i HATE the admins"])
admin1 = Admin("sergei", [], 1)

print("The posts should be below here:")
user1.make_post("Hello everyone!") # should print out "joe27: Hello everyone!"
admin1.make_post("I am having a bad day.") # should print out "1 - sergei: I am having a bad day."

print("\nThe number of posts should be below here")
print(user1.get_number_of_posts()) # 2
print(admin1.get_number_of_posts()) # 1

print("\nThe admin should delete a post here, but it won't print anything")
admin1.delete_user_post(user1, "i HATE the admins") # should delete user1's post

print("Since the admin has deleted a post, the user should only have one now")
print(user1.get_number_of_posts()) # 1
