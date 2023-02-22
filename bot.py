from instagrapi import Client

IG_USERNAME = "YOUR IG USERNAM"
IG_PASSWORD = "YOUR IG INSTAGRAM"

unfollowed = []
# Set up your InstaPy instance with your username and password
client = Client()

# Log in using the configured proxy
client.login(username=IG_USERNAME, password=IG_PASSWORD, relogin=True)

# Get your followers
followers = client.user_followers(client.user_id)

# Get the users you follow
following = client.user_following(client.user_id)

# Find the users who don't follow you back
not_following_back = [user for user in following if user not in followers]

# Print the list of users who don't follow you back
for user in not_following_back:
    unfollowed.append(client.username_from_user_id(user))

print(unfollowed)