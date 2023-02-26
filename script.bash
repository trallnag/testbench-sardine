query=$(
  gh api graphql \
    -F repoOwner="{owner}" \
    -F repoName="{repo}" \
    -F discussionCategorySlug="Announcements" \
    -F query=@assets/gh-category.graphql \
)
echo "query=$query"

repositoryId=$(echo "$query" | jq -r .data.repository.id)
echo "repositoryId=$repositoryId"

categoryId=$(echo "$query" | jq -r .data.repository.discussionCategory.id)
echo "categoryId=$categoryId"
