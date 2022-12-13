import pytest

from main import create_posts
from db.models import User, Post


@pytest.mark.django_db
def test_empty_post() -> None:
    test_data = []

    assert (
        create_posts(test_data) == []
    ), "create_posts function should return `[]` if empty list was inputted."


@pytest.mark.django_db
def test_create_posts() -> None:
    test_data = [
        {
            "creator": 1,
            "title": "What is Python?",
            "content": "Python is a high-level, general-purpose programming language.",
        },
        {
            "creator": 2,
            "title": "When was Python created?",
            "content": "Python was created by Guido van Rossum, and first released on February 20, 1991.",
        },
    ]
    User.objects.create(first_name="Mariia", last_name="Vovk")
    User.objects.create(first_name="Mark", last_name="Fedoriv")

    created_posts_by_function = create_posts(test_data)

    posts = []
    for post_info in test_data:
        posts.append(
            Post.objects.get_or_create(
                creator=User.objects.get(pk=post_info["creator"]),
                title=post_info["title"],
                content=post_info["content"],
            )[0]
        )

    assert created_posts_by_function == posts, (
        f"create_posts function should return {posts} but actual returned data is "
        f"{create_posts(test_data)} "
    )
