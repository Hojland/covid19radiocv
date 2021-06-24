image_name=docker.pkg.github.com/hojland/covid19radiocv/covid19radiocv

.PHONY: build_local_cpu, build_local_gpu, run_train

build_local_cpu:
	docker build -t ${image_name}:local-cpu --build-arg COMMIT_HASH=${commit_hash} --build-arg PROD_ENV=$(env) \
		--build-arg COMPUTE_KERNEL=cpu --build-arg IMAGE_NAME=python:3.8 -f Dockerfile .

build_local_gpu:
	make docker_login
	docker build -t ${image_name}:local-gpu --build-arg COMMIT_HASH=${commit_hash} --build-arg PROD_ENV=$(env) \
		--build-arg COMPUTE_KERNEL=gpu -f Dockerfile .
	docker push ${image_name}:local-gpu
	

run_train:
	@docker run \
		-it \
		-d \
		--rm \
		--gpus all \
		--name $(project)-train \
		--env-file .env \
		${image_name}:local-gpu \
		"python3 train.py"


docker_login:
	@echo "Requesting credentials for docker login"
	@$(eval export GITHUB_ACTOR=hojland)
	@$(eval export GITHUB_TOKEN=$(shell awk -F "=" '/GITHUB_TOKEN/{print $$NF}' .env))
	@docker login https://docker.pkg.github.com/hojland/ -u $(GITHUB_ACTOR) -p $(GITHUB_TOKEN)

get_dataset:
	kaggle competitions download -c siim-covid19-detection -p src/data/zip -f train/00086460a852/9e8302230c91/65761e66de9f.dcm
	unzip -q src/data/zip/65761e66de9f.dcm.zip -d src/data/radiographs/65761e66de9f.dcm
	kaggle competitions download -c siim-covid19-detection -p src/data/radiographs -f train_study_level.csv
	kaggle competitions download -c siim-covid19-detection -p src/data/zip -f train_image_level.csv
	unzip -q src/data/zip/train_image_level.csv.zip