import requests

# URL of the JSONPlaceholder API endpoint for posts
url = "https://jsonplaceholder.typicode.com/posts"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    posts = response.json()
    
    # Display the title of the first 5 posts
    for post in posts[:5]:  # Limiting to first 5 posts
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print('-' * 40)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
