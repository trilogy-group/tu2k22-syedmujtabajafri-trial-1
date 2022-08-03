# TU’22 Tracks syedmujtabajafri

## Docker, git and devspaces
![Image](/screenshots/curl.png?raw=true&sanitize=true)

## Proxy API
![Image](/screenshots/proxy_api.png?raw=true&sanitize=true)

### Devspaces: Sometimes it throws an error (connection refused). So here's a screenshot just in case
![Image](/screenshots/gitpod.png?raw=true&sanitize=true)
### Git commands I used:
```bash
sudo rm -rf .git
git log
git status
git fetch origin
git checkout -b <new-branch> origin/<remote-branch>
git push -u origin main
git pull origin main
git merge <branch-name>
git rebase -i HEAD~<number of commits to be squashed>
```

### Docker commands I used:
```bash
docker exec -it <container-id>
docker rmi <image-id>
docker rm <container-id>
docker-compose up
docker-compose up -d
docker-compose up --build ## All 3 are really important to me
docker container ls
docker container ls -a
docker ps
docker create
docker inspect
docker create
docker start
```