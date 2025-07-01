import json
from django.contrib.auth.models import User
from blog.models import Post  # adjust path if needed

with open('posts.json') as f:
    data = json.load(f)

for item in data:
    try:
        user = User.objects.get(id=item['author_id'])
        Post.objects.create(
            title=item['title'],
            content=item['content'],
            author=user
        )
        print(f"Post created: {item['title']}")
    except User.DoesNotExist:
        print(f"User with id {item['author_id']} does not exist.")
