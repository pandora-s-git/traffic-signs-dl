## Utilisez : ./lazypush "message que vous souhaitez (optionnel)"

param(
    [string]$message = "update (lazy push)"
)

git add --all
git commit -m $message
git push