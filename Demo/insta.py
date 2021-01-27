import instaloader


mod = instaloader.Instaloader()
a = input("enter profile")
mod.download_profile(profile_name=a, profile_pic_only=True)
