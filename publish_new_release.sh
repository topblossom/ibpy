cat $GH_TOKEN  | docker login docker.pkg.github.com -u jpalczewski --password-stdin
ID=$(docker build -q -t icgbooks/topblossom .)
docker tag IMAGE_ID docker.pkg.github.com/topblossom/icgbooks/ibpy:$version
docker push docker.pkg.github.com/topblossom/icgbooks/ibpy:$version