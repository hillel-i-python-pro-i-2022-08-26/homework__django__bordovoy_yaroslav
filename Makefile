.PHONY: homework-i-run
# Run homework
homework-i-run:
	@python manage.py runserver

.PHONY: homework-i-purge
homework-i-purge:
	@echo The end

.PHONY: init-dev
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate

.PHONY: generate-contacts
# Generates 10 contacts
generate-contacts:
	@python manage.py generate_contacts

.PHONY: delete-contacts
# Deletes all contacts
delete-contacts:
	@python manage.py delete_contacts --all

.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input